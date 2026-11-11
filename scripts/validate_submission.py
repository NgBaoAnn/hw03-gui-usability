"""Check structural evidence and report missing final-submission prerequisites."""
import csv
import json
import re
import sys
from pathlib import Path
from calculate_sus import analyse, self_check

ROOT=Path(__file__).resolve().parents[1]


def check_files():
    items=json.loads((ROOT/'checklists/items.json').read_text())
    assert len(items)>40 and len({r[0] for r in items})==len(items)
    assert {r[1] for r in items}=={'IA-01','IA-02','IA-03','IA-04'}
    expected={r[0] for r in items};failed=set()
    for engine in ['chrome','firefox','safari']:
        assert (ROOT/f'evidence/identity/{engine}.png').is_file(),f'Missing SUT form identity evidence for {engine}'
        run=json.loads((ROOT/f'evidence/runs/{engine}.json').read_text())
        assert {r['id'] for r in run['results']}==expected
        assert len(run['results'])==len(expected)
        for row in run['results']:
            assert row['status'] in ['Passed','Failed'], f'Unexecuted {engine} {row["id"]}'
            if row['status']=='Failed':
                assert row['notes'].strip() and (ROOT/row['evidence']).is_file()
                failed.add(row['id'])
    bugs=json.loads((ROOT/'bug-reports/catalog.json').read_text())
    assert {i for bug in bugs for i in bug['checks']}==failed,'Some failures lack a bug or some bug checks did not fail'
    for bug in bugs:
        assert (ROOT/bug['file']).is_file()
        assert all((ROOT/p).is_file() for p in bug['screenshots'])
    for p in ['reports/MAIN_REPORT.pdf','reports/AI_AUDIT_REPORT.pdf','reports/AI_CRITIQUE.pdf','reports/AI_AUDIT_RECOVERED.md','checklists/gui_checklist_g2.xlsx','git_commit_log.txt','HUONG_DAN_HOAN_TAT.md','skills/gui-usability-evaluator/video/gui-g2-demo.mp4','skills/gui-usability-evaluator/video/recording-log.json']:
        assert (ROOT/p).is_file(),f'Missing deliverable {p}'
    self_check()
    words=len((ROOT/'reports/AI_CRITIQUE.md').read_text().split('\n\n',2)[2].split())
    assert 200<=words<=300,words
    return items,bugs


def missing_requirements():
    state=json.loads((ROOT/'submission_state.json').read_text());missing=[]
    if not state['human_review_complete'] or not state['human_added_check_ids']:
        missing.append('Sinh viên chưa rà soát và tự bổ sung checklist kèm lý do AI bỏ sót.')
    if not state['pilot_evidence'] or not (ROOT/state['pilot_evidence']).is_file():
        missing.append('Chưa có bằng chứng pilot thực tế.')
    try:
        analyse(ROOT/'usability/sus_responses.csv')
    except ValueError as error:
        missing.append(f'Chưa đủ dữ liệu SUS thật: {error}')
    with (ROOT/'usability/participants.csv').open(encoding='utf-8-sig') as f:people=list(csv.DictReader(f))
    if len(people)!=7 or any(not r['full_name'].strip() or not r['masked_contact'].strip() or r['outside_class_confirmed'].strip().lower() not in ['true','yes','có'] for r in people):
        missing.append('Chưa có danh sách 7 người thật ngoài lớp và liên hệ đã che.')
    if len(state['session_evidence'])!=7 or any(not (ROOT/p).is_file() for p in state['session_evidence']):
        missing.append('Chưa có đủ ghi chú và bằng chứng 7 phiên thực tế.')
    third=state['third_platform_full_run']
    if not third or not (ROOT/third).is_file():
        missing.append('Chưa có lượt chạy đủ checklist trên nền tảng thứ ba hợp lệ.')
    else:
        third_run=json.loads((ROOT/third).read_text())
        if third_run.get('engine')!='safari' or not third_run.get('fullChecklist') or len(third_run.get('results',[]))!=48:
            missing.append('Lượt Safari chưa thực thi đủ 48 mục với kết quả hợp lệ.')
    if not re.match(r'https://(?:www\.)?(youtube\.com/|youtu\.be/)',state['demo_youtube_url']):
        missing.append('Chưa có YouTube demo skill end-to-end.')
    if not state['earlier_ai_audit_complete']:
        missing.append('Audit các tương tác AI tạo kế hoạch cũ chưa đầy đủ.')
    score=state['self_assessment']
    if not isinstance(score,dict) or set(score)!={'task1','task2','task3','skill'} or any(type(score[k]) is not int or not 0<=score[k]<=m for k,m in [('task1',30),('task2',40),('task3',20),('skill',10)]):
        missing.append('Chưa có bảng tự chấm 30/40/20/10 được sinh viên xác nhận.')
    issues=ROOT/'bug-reports/issues.json'
    if not issues.exists() or len(json.loads(issues.read_text()))!=23:
        missing.append('Chưa có đủ GitHub Issue URLs cho 23 nhóm bug.')
    if not state.get('github_grader_access_confirmed'):
        missing.append('Repo GitHub đang private; chưa xác nhận người chấm có quyền xem Issues.')
    return missing


def main():
    try:items,bugs=check_files()
    except (AssertionError,FileNotFoundError) as error:
        print(f'Artifact check FAILED: {error}');return 2
    print(f'Artifact check OK: {len(items)} checklist items; {len(bugs)} bug groups; original failed screenshots present.')
    missing=missing_requirements()
    if missing:
        print('NOT READY FOR FINAL SUBMISSION:')
        for message in missing:print('- '+message)
        return 1
    print('Structural checks complete; human review of actual evidence and final Moodle confirmation still required.')
    return 0


if __name__=='__main__':sys.exit(main())
