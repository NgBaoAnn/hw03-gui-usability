"""Validate the student-supplied study and produce anonymous public analysis."""
import csv
import hashlib
import json
import statistics as st
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from calculate_sus import score, self_check

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'task2_usability'


def main():
    self_check()
    data = json.loads((SOURCE / 'data/simulation.json').read_text())
    sessions = data['sessions']
    assert [s['id'] for s in sessions] == [f'P{i:02}' for i in range(1, 8)]
    assert data['pilot']['id'] == 'P00'
    with (SOURCE / 'sus_responses.csv').open(encoding='utf-8-sig') as f:
        csv_rows = {r['participant']: r for r in csv.DictReader(f)}
    assert set(csv_rows) == {s['id'] for s in sessions}
    results = []
    for s in sessions:
        answers = [int(csv_rows[s['id']][f'q{i}']) for i in range(1, 11)]
        assert answers == s['sus_answers'], f"CSV/JSON mismatch: {s['id']}"
        seconds = [e['seconds'] for e in s['events']]
        assert seconds == sorted(seconds) and seconds[0] == 0
        assert seconds[-1] == s['task_time_seconds']
        assert set(s['tasks']) == {'T1', 'T2', 'T3', 'T4'}
        assert all(k in s['probes'] for k in ['clarity', 'recovery', 'speed', 'trust'])
        outcome = 'timeout' if any(v in ['failed', 'not_reached'] for v in s['tasks'].values()) else 'assisted' if s['assistance'] or 'assisted' in s['tasks'].values() else 'independent'
        results.append({'participant_id': f"P{int(s['id'][1:])}", 'source_id': s['id'], 'sus': score(answers), 'seconds': s['task_time_seconds'], 'outcome': outcome})
    scores = [r['sus'] for r in results]
    counts = Counter(r['outcome'] for r in results)
    findings = {f['id']: len({s['id'] for s in sessions if any(e['finding'] == f['id'] for e in s['events'])}) for f in data['findings']}
    summary = {'n': 7, 'pilot_count': 1, 'mean_sus': st.mean(scores), 'median_sus': st.median(scores), 'sample_sd_sus': st.stdev(scores), 'outcome_counts': dict(counts), 'completion_rate': (7-counts['timeout'])/7, 'duration_all_mean': st.mean(r['seconds'] for r in results), 'duration_success_mean': st.mean(r['seconds'] for r in results if r['outcome'] != 'timeout'), 'finding_counts': findings, 'participants': results}
    original = json.loads((SOURCE / 'data/summary.json').read_text())
    for key, value in [('sus_mean', summary['mean_sus']), ('sus_median', summary['median_sus']), ('sus_sample_sd', summary['sample_sd_sus']), ('completion_rate', summary['completion_rate']), ('duration_all_mean', summary['duration_all_mean']), ('duration_success_mean', summary['duration_success_mean'])]:
        assert abs(original[key]-value) < 1e-9, key
    assert original['outcome_counts'] == dict(counts) and original['finding_counts'] == findings
    backup = ROOT / 'usability/private/task2_original'
    if not backup.exists():
        import shutil
        shutil.copytree(SOURCE, backup)
    source_hashes = {str(p.relative_to(backup)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(backup.rglob('*')) if p.is_file() and '__pycache__' not in p.parts}
    now = datetime.now(ZoneInfo('Asia/Ho_Chi_Minh')).isoformat(timespec='seconds')
    old_privacy='Người điều phối tôn trọng quyền riêng tư của người tham gia (phù hợp với quy định *"Record the screen (and audio, with consent) ... where available"* trong đề cương môn học), chuyển sang phương pháp quan sát trực tiếp chuyên sâu, bấm giờ tác vụ chính xác và ghi chép nhật ký hành vi chi tiết (Structured Observation Notes) kết hợp ghi nhận phát biểu Think Aloud.'
    privacy='Người điều phối ghi nhận việc từ chối và sử dụng ghi chú có cấu trúc. Hồ sơ hiện không có video phiên. §6 hướng dẫn ghi màn hình; §14 của đề tiếng Anh quy định nộp screen recordings where available. Nêu rõ việc không ghi hình là giới hạn bằng chứng; không tạo video thay cho phiên đã diễn ra.'
    for p in SOURCE.rglob('*'):
        if p.is_file() and p.suffix in ['.md','.json','.py']:
            text=p.read_text().replace('Phạm Quang Vinh','Nguyễn Bảo An').replace('23120202','23120207').replace(old_privacy,privacy)
            text=text.replace('../bugs/screenshots/GUI-001.png','../evidence/usability/U02.png').replace('../bugs/screenshots/GUI-030.png','../evidence/usability/U03.png')
            text=text.replace('https://github.com/vinh-code/HW03-Software-Testing/issues/10','../bug-reports/usability/U03.md').replace('https://github.com/vinh-code/HW03-Software-Testing/issues/1','../bug-reports/usability/U02.md')
            text=text.replace('**Mức 2 (Moderate):**','**Mức 2 (Minor):**')
            text=text.replace('(ghi nhận ở P02, P04, P07)','(ghi nhận ở P01, P02, P05, P07 theo timeline)')
            p.write_text(text)
    data=json.loads((SOURCE/'data/simulation.json').read_text())
    for finding in data['findings']:
        finding['issue']=None
        finding['shot']=f"../evidence/usability/{finding['id']}.png"
    (SOURCE/'data/simulation.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    provenance = {'student_confirmation': 'Sinh viên xác nhận trong chat: Có, đây là các phiên thật tôi đã điều phối.', 'imported_at': now, 'source_directory': 'task2_usability', 'verification_scope': 'Đối chiếu số học, CSV/JSON và tính nhất quán; không xác minh độc lập danh tính hay việc diễn ra các phiên.', 'original_file_sha256': source_hashes, 'id_mapping': {r['source_id']: r['participant_id'] for r in results}, 'recordings_available': False, 'recording_limitation': 'Hồ sơ ghi tất cả người tham gia từ chối ghi hình. Chỉ có ghi chú; §14 yêu cầu bản quay khi có, nên giữ rõ giới hạn bằng chứng.'}
    (ROOT / 'usability/provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2)+'\n')
    (ROOT / 'usability/summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n')
    with (ROOT / 'usability/sus_responses.csv').open('w', newline='', encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['participant_id']+[f'q{i}' for i in range(1,11)])
        w.writerows([[r['participant_id']]+s['sus_answers'] for r,s in zip(results,sessions)])
    with (ROOT / 'usability/participants.csv').open('w', newline='', encoding='utf-8') as f:
        fields=['participant_id','full_name','masked_contact','outside_class_confirmed','background','session_datetime','consent_screen','consent_audio','evidence']
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for r,s in zip(results,sessions):
            w.writerow(dict(zip(fields,[r['participant_id'],s['name'],s['contact'],'yes',s['experience'],s['interview_datetime'],'no','not documented',f"usability/sessions/{r['participant_id']}.md"])))
    for s, name in [(data['pilot'],'PILOT')]+[(s,r['participant_id']) for s,r in zip(sessions,results)]:
        src='pilot.md' if name=='PILOT' else f"S{int(s['id'][1:]):02}.md"
        text=(SOURCE/'sessions'/src).read_text().replace(s['name'],name).replace(s['contact'],'Liên hệ đã che trong danh sách nộp riêng')
        text=text.replace(s['id'],name)
        text+='\n\nNguồn: hồ sơ sinh viên cung cấp ngày 15/11/2026; sinh viên xác nhận đã điều phối phiên thật trong chat. Không có video phiên trong hồ sơ. Bản công khai dùng mã thay họ tên/liên hệ.\n'
        (ROOT/'usability/sessions'/f'{name}.md').write_text(text)
    # Keep public analysis free of participant names and contacts.
    analysis=(SOURCE/'analysis.md').read_text()
    for s in [data['pilot']]+sessions:
        analysis=analysis.replace(s['name'], 'Pilot' if s['id']=='P00' else f"P{int(s['id'][1:])}")
        if s['id']!='P00':analysis=analysis.replace(s['id'],f"P{int(s['id'][1:])}")
    analysis+='\n\n## Nguồn và giới hạn bằng chứng\n\nDữ liệu do sinh viên cung cấp và xác nhận là các phiên thật do mình điều phối. Codex đối chiếu độc lập phép tính; không xác minh độc lập người tham gia. Pilot được loại khỏi thống kê. Task 2 dùng luồng quản lý đơn hàng, khác phạm vi GUI G2 của Task 1. Không có video phiên vì hồ sơ ghi người tham gia từ chối. §6 hướng dẫn ghi màn hình; §14 ghi bản quay khi có (screen recordings where available). Hồ sơ nộp ghi chú có cấu trúc và nêu rõ giới hạn không có video.\n'
    (ROOT/'usability/FINDINGS.md').write_text('\n'.join(line.rstrip() for line in analysis.splitlines())+'\n')
    protocol='\n\n'.join((SOURCE/p).read_text() for p in ['00_scope.md','01_plan_objectives_scenario.md','04_moderator_script.md','03_probe_questions.md'])
    (ROOT/'usability/PROTOCOL.md').write_text(protocol)
    (ROOT/'usability/SUS_QUESTIONNAIRE.md').write_text((SOURCE/'02_SUS_questionnaire.md').read_text())
    state=json.loads((ROOT/'submission_state.json').read_text())
    state.update(pilot_evidence='usability/sessions/PILOT.md',session_evidence=[f'usability/sessions/P{i}.md' for i in range(1,8)],usability_student_confirmed=True,usability_recordings_complete=False)
    (ROOT/'submission_state.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
