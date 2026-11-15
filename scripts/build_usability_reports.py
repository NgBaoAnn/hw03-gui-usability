"""Link supplied participant observations to separately reproduced UI evidence."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def main():
    supplied=json.loads((ROOT/'task2_usability/data/simulation.json').read_text())
    study=json.loads((ROOT/'usability/summary.json').read_text())
    recheck=json.loads((ROOT/'evidence/usability/recheck.json').read_text())
    observations={r['id']:r for r in recheck['results']}
    assert set(observations)=={f'U{i:02}' for i in range(1,6)}
    folder=ROOT/'bug-reports/usability';folder.mkdir(exist_ok=True)
    issues=json.loads((folder/'issues.json').read_text()) if (folder/'issues.json').exists() else {}
    steps={
        'U01':'Đăng nhập bằng tài khoản fixture; quan sát navbar và liên kết /profile. Kỳ vọng thiết kế: có lối vào Đơn hàng của tôi rõ nghĩa.',
        'U02':'Mở /login khi chưa đăng nhập. Kỳ vọng: tiêu đề mô tả chức năng đăng nhập.',
        'U03':'Đăng nhập tài khoản có đơn shipping; mở /profile; quan sát cột Thao tác. Kỳ vọng: không mời người dùng thực hiện hành động không phù hợp trạng thái shipping theo FR-10. Lượt này chưa click hủy đơn shipping.',
        'U04':'Ở /profile có đơn pending; bấm Hủy đơn đúng một lần; ghi mọi native dialog. Kỳ vọng heuristic: có xác nhận trước thao tác hủy khó hoàn tác.',
        'U05':'Ở /profile có bốn đơn khác trạng thái; đọc cột của bảng Lịch sử đơn hàng. Kỳ vọng thiết kế: có thông tin sản phẩm để nhận diện đơn; đây là đề xuất UX, không khẳng định yêu cầu FR bắt buộc.'}
    catalog=[];bodies=[]
    for f in supplied['findings']:
        uid=f['id'];r=observations[uid];severity='Major' if f['severity']==3 else 'Minor'
        sessions=[f"P{int(s['id'][1:])}" for s in supplied['sessions'] if any(e['finding']==uid for e in s['events'])]
        assert len(sessions)==study['finding_counts'][uid]
        kind='Lỗi nhãn cụ thể' if uid=='U02' else 'Affordance không khớp trạng thái' if uid=='U03' else 'Vấn đề thiết kế lặp lại / heuristic'
        body=f'''# {uid}: {f['title']}

Severity: **{severity}** (đề xuất, chờ human review). Loại: {kind}.

Ghi chú nghiên cứu do sinh viên cung cấp: {len(sessions)}/7 phiên ({', '.join(sessions)}). Không suy rộng tần suất ra ngoài mẫu này.

Môi trường tái hiện: Chrome {recheck['browser']}, macOS, localhost:5173; SUT `{recheck['sutCommit']}`. Thời điểm: {r['timestamp']}.

Tiền điều kiện: clone SUT riêng; tài khoản fixture và bốn đơn 28 triệu pending, 1,5 triệu confirmed, 45 triệu shipping, 30 triệu delivered. Dữ liệu fixture do agent tạo để tái hiện, không phải dữ liệu người tham gia.

Bước và kỳ vọng: {steps[uid]}

Thực tế: {r['observation']}

Đề xuất: {f['recommendation']}

Ảnh dưới đây do agent chụp khi tái hiện sau khi nhận hồ sơ, không phải ảnh/video phiên người tham gia. Tính xác thực phiên dựa vào xác nhận của sinh viên; ảnh này chỉ chứng minh trạng thái UI hiện tại.

GitHub Issue: {issues.get(uid,{}).get('url','Chờ đăng')}

![{uid} tái hiện](../../{r['evidence']})
'''
        (folder/f'{uid}.md').write_text(body)
        catalog.append({'id':uid,'title':f['title'],'severity':severity,'file':f'bug-reports/usability/{uid}.md','screenshots':[r['evidence']]})
        bodies.append(body)
        f['issue']=issues.get(uid,{}).get('url')
    (folder/'catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
    (folder/'BUG_REPORTS.md').write_text('\n\n'.join(bodies))
    (ROOT/'task2_usability/data/simulation.json').write_text(json.dumps(supplied,ensure_ascii=False,indent=2)+'\n')
    integration=f'''# Tích hợp Task 2 vào bài cá nhân 23120207

Nguyễn Bảo An xác nhận trong chat các phiên thật do mình điều phối và yêu cầu sửa thông tin sinh viên trong hồ sơ thành Nguyễn Bảo An – 23120207. Luồng Task 2 giữ nguyên quản lý đơn hàng; GUI Task 1 vẫn là G2.

Đã đối chiếu 70 câu trả lời giữa CSV/JSON và tính SUS độc lập: 75; 62,5; 37,5; 87,5; 55; 27,5; 67,5. Trung bình 58,93; trung vị 62,5; SD mẫu 20,91. Pilot không tính vào mẫu. Kết quả tác vụ và thời gian giữ nguyên dữ liệu cung cấp.

Tên file simulation.json và script build_simulation.py được giữ để truy vết nguồn; tên file không dùng làm bằng chứng xác thực phiên. SHA-256 bản trước khi chỉnh lưu trong usability/provenance.json; bản gốc giữ riêng, ngoài ZIP/public repo.

Mức 3 ánh xạ Major; mức 2 ánh xạ Minor theo rubric Blocker/Major/Minor của đề. U05 có trong timeline P01, P02, P05, P07; câu diễn giải cũ nhắc P04 không khớp timeline, dùng timeline làm nguồn tổng hợp.

Ảnh gốc được tham chiếu trong hồ sơ cũ không có trong folder. Đã thay bằng năm ảnh agent tái hiện và báo cáo riêng tại ../bug-reports/usability/. Ảnh tái hiện không thay video phiên. Danh sách liên hệ đã che chỉ đưa vào ZIP nộp, không public trên GitHub.

Giới hạn còn lại: hồ sơ ghi cả tám người từ chối ghi hình nên không có video phiên. §6 hướng dẫn ghi màn hình; §14 yêu cầu kèm bản quay khi có (screen recordings where available). Hồ sơ nộp ghi chú và nêu rõ giới hạn này. Các phiên được nhập cùng lúc, không có commit riêng được tạo ngay sau từng phiên.
'''
    (ROOT/'task2_usability/INTEGRATION.md').write_text(integration)
    links='\n\n## Đối chiếu với bằng chứng tái hiện\n\n| Mã | Severity đề xuất | Tần suất trong mẫu | GitHub Issue | Ảnh agent tái hiện |\n|---|---|---|---|---|\n'
    for b in catalog:
        uid=b['id'];url=issues.get(uid,{}).get('url','Chờ đăng')
        links+=f"| {uid} | {b['severity']} | {study['finding_counts'][uid]}/7 | {url} | [Ảnh](../{b['screenshots'][0]}) |\n"
    public=ROOT/'usability/FINDINGS.md'
    public.write_text(public.read_text().split('\n\n## Đối chiếu với bằng chứng tái hiện')[0]+links)
    integration+=links
    base=(ROOT/'task2_usability/Task2_Usability_Report.md').read_text().split('\n# Tích hợp Task 2 vào bài cá nhân 23120207')[0]
    (ROOT/'task2_usability/Task2_Usability_Report.md').write_text(base.rstrip()+'\n\n'+integration)
    print('Built five traceable usability reports; participant data remains local.')


if __name__=='__main__':
    main()
