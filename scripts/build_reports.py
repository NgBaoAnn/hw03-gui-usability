"""Build traceable Markdown/CSV reports from recorded GUI runs; never invent results."""
import csv
import json
from pathlib import Path
from collections import Counter
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]


def write(path, text):
    (ROOT / path).write_text(text.rstrip() + '\n', encoding='utf-8')


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' / ')


def main():
    demo=ROOT/'skills/gui-usability-evaluator/video/gui-g2-demo.mp4'
    assert demo.is_file(),'Record and verify the actual demo before building these reports'
    runs = {e: json.loads((ROOT / f'evidence/runs/{e}.json').read_text()) for e in ['chrome', 'firefox', 'safari']}
    assert runs['safari']['fullChecklist'], 'Safari must finish all criteria before publishing a full-platform report'
    chrome = runs['chrome']['results']
    firefox = runs['firefox']['results']
    safari_results = runs['safari']['results']
    assert len(chrome) == len(firefox) == len(safari_results) == len(json.loads((ROOT / 'checklists/items.json').read_text()))
    counts = {e: Counter(r['status'] for r in run['results']) for e, run in runs.items()}
    now = datetime.now(ZoneInfo('Asia/Ho_Chi_Minh')).isoformat(timespec='seconds')
    rows = []
    for a, b, c in zip(chrome, firefox, safari_results):
        assert a['id'] == b['id'] == c['id']
        rows.append([a['id'], a['aspect'], a['screen'], a['criterion'], a['reference'], a['status'], b['status'], c['status'], a['notes'], b['notes'], c['notes'], a['evidence'], b['evidence'], c['evidence']])
    with (ROOT / 'checklists/gui_checklist_g2.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['ID', 'IA', 'Screen', 'Expected', 'Reference', 'Chrome', 'Firefox', 'Safari', 'Chrome notes', 'Firefox notes', 'Safari notes', 'Chrome screenshot', 'Firefox screenshot', 'Safari screenshot'])
        writer.writerows(rows)
    md = ['# Checklist GUI G2 đã thực thi', '', '48 mục do Codex thiết kế và thực thi tự động trên Chrome, Firefox và Safari thật. Sinh viên chưa hoàn tất human review/tự bổ sung.', '', 'Bước thao tác: `scripts/run_gui.cjs` (Chrome/Firefox), `scripts/run_safari.py` (Apple WebDriver). Kết quả đầy đủ trong `evidence/runs/`. Notes được rút gọn; ảnh gốc có chú thích sau phép đo.', '', '| ID | IA | Màn hình | Tiêu chí | Nguồn | Chrome | Firefox | Safari | Notes Failed (rút gọn) | Ảnh Failed |', '|---|---|---|---|---|---|---|---|---|---|']
    for a,b,c in zip(chrome,firefox,safari_results):
        platform_rows=[('Chrome',a),('Firefox',b),('Safari',c)]
        pics='; '.join(f'[{e}](../{r["evidence"]})' for e,r in platform_rows if r['status']=='Failed')
        notes='; '.join(f'{e}: {r["notes"][:120]}' for e,r in platform_rows if r['status']=='Failed')
        md.append('| '+' | '.join(map(cell,[a['id'],a['aspect'],a['screen'],a['criterion'],a['reference'],a['status'],b['status'],c['status'],notes,pics]))+' |')
    write('checklists/gui_checklist_g2.md','\n'.join(md))
    groups = [
        ('B01','Home có hai h1 thay vì một','Minor',['G01'],'Mở danh sách sản phẩm. Kiểm tra heading trong main.','Chỉ có một h1 mô tả trang.','Số h1 thực tế là 2.'),
        ('B02','Giỏ hàng không có h1','Minor',['G03'],'Từ Home thêm một sản phẩm, mở Giỏ hàng.','Giỏ có một h1.','Giỏ có 0 h1.'),
        ('B03','Thẻ sản phẩm dùng VND thay cho ký hiệu ₫','Minor',['G04'],'Mở Home và so sánh giá trên thẻ với trang chi tiết.','Giá dùng ₫ nhất quán.','Danh sách dùng VND, chi tiết dùng ₫.'),
        ('B04','Ảnh vuông bị cắt trong khung ảnh danh sách','Minor',['G07'],'Mở Home, đối chiếu khung ảnh với ảnh gốc 300×300.','Giữ nội dung ảnh theo tiêu chí kiểm thử về tỷ lệ.','object-cover trong khung 281×192 cắt ảnh vuông. Đây là phát hiện heuristic cần sinh viên duyệt mức ảnh hưởng.'),
        ('B05','Nút thêm giỏ ở chi tiết dùng xanh lá thay vì xanh dương','Minor',['G11'],'Mở /product/1, quan sát màu nút thêm giỏ.','Hành động tích cực dùng xanh dương theo GUI §8.','Nút có nền rgb(22,163,74).'),
        ('B06','Tất cả ảnh sản phẩm danh sách có alt rỗng','Major',['G12'],'Mở Home, kiểm tra thuộc tính alt của 5 ảnh thẻ.','alt mô tả sản phẩm.','Cả 5 alt đều rỗng, ảnh bị coi là trang trí với công nghệ hỗ trợ.'),
        ('B07','Ô tìm kiếm và số lượng thiếu nhãn truy cập được liên kết','Major',['G13','G23'],'Mở Home và /product/1; kiểm tra labels, aria-label, aria-labelledby của input.','Mỗi trường có tên truy cập bền vững.','Tìm kiếm chỉ có placeholder; label Số lượng không liên kết input. Đây là kiểm tra DOM, chưa thay thế thử screen reader thật.'),
        ('B08','Ký tự & bị coi là dấu tách tham số trong từ khóa','Major',['G16'],'Nhập iPhone&limit=1 ở Home, nhấn Enter.','Tìm nguyên văn chuỗi; không sản phẩm nào khớp.','Vẫn trả iPhone vì query bị cắt tại &.'),
        ('B09','Số lượng không hợp lệ đi vào giỏ và sinh tổng âm hoặc NaN','Major',['G19','G20','G21','G22'],'Mỗi lần mở mới /product/1; nhập 0, -1, 1.5 hoặc bỏ trống; bấm Thêm hai lần do B18; mở giỏ.','Từ chối số lượng không phải số nguyên dương, hiển thị lỗi và không thay đổi giỏ.','Giỏ nhận 0, -1, làm tròn 1.5 thành 1, và ô trống thành NaN. Tổng âm hoặc NaN tương ứng.'),
        ('B10','Từ khóa tìm kiếm bị render thành HTML','Major',['G24'],'Nhập <b data-hw03-probe="1">HW03 probe</b> vào ô tìm kiếm. Không dùng payload script.','Hiển thị nguyên văn HTML như văn bản an toàn.','DOM tạo phần tử b và hiển thị chữ đậm. Đã xác nhận HTML injection; chưa thực thi script hoặc khẳng định khai thác XSS sâu hơn.'),
        ('B11','Browser Back làm mất từ khóa và tập kết quả','Minor',['G29'],'Tìm iPhone; mở chi tiết; dùng Browser Back.','Giữ từ khóa và một kết quả theo heuristic duy trì ngữ cảnh.','Từ khóa rỗng và hiện lại 5 sản phẩm.'),
        ('B12','Trang chi tiết và giỏ thiếu breadcrumb','Minor',['G30','G31'],'Mở /product/1 và giỏ có hàng.','Có breadcrumb theo GUI §8.','Không có vùng breadcrumb trên hai trang.'),
        ('B13','Navbar không highlight Giỏ hàng đang mở','Minor',['G32'],'Mở /cart, xem link Giỏ hàng.','Có trạng thái được chọn và chỉ báo truy cập phù hợp.','Chỉ có hover:underline, không có highlight trang hiện tại.'),
        ('B14','Thêm cùng sản phẩm hai lần tạo hai dòng giỏ','Major',['G36'],'Ở Home bấm Thêm vào giỏ hai lần trên cùng thẻ; mở giỏ.','Một dòng có số lượng 2.','Hai dòng cùng sản phẩm, mỗi dòng số lượng 1.'),
        ('B15','Danh sách thiếu loading khi đang chờ API','Minor',['G37'],'Giả lập trễ GET /api/products? 1600ms: Chrome/Firefox dùng Playwright route, Safari dùng XHR redirect tới fixture localhost; mở Home.','Có thông báo/loading indicator khi chờ.','Chỉ có tiêu đề và form tìm kiếm trong thời gian chờ. Điều kiện mạng được mô phỏng có kiểm soát.'),
        ('B16','Không có kết quả tìm kiếm nhưng thiếu empty-state message','Minor',['G38'],'Tìm HW03-no-such-product-731.','Thông báo thân thiện rằng không có kết quả.','Chỉ hiện dòng từ khóa, không có thông báo trạng thái rỗng.'),
        ('B17','Thêm từ thẻ không có phản hồi và giỏ không có badge','Major',['G39','G42'],'Từ Home bấm Thêm vào giỏ một lần, quan sát màn hình và navbar.','Toast/badge thông báo thêm thành công; link giỏ có số lượng.','Không có toast, vùng thông báo hoặc badge. Mở giỏ mới thấy sản phẩm đã được thêm.'),
        ('B18','Lần bấm Thêm vào giỏ đầu tiên ở chi tiết không làm gì','Major',['G40'],'Mở mới /product/1; bấm Thêm vào giỏ hàng đúng một lần; mở Giỏ hàng.','Giỏ có một sản phẩm ngay sau một lần bấm.','Giỏ trống. Bấm lần hai mới thêm và hiện Đã thêm.'),
        ('B19','Xóa sản phẩm khỏi giỏ ngay lập tức không có xác nhận','Major',['G43'],'Từ Home thêm sản phẩm; mở giỏ; bấm Xóa.','Hiện dialog xác nhận trước khi xóa.','Không có native dialog hay role=dialog; sản phẩm mất ngay.'),
        ('B20','Giỏ trống thiếu hình minh họa hoặc icon','Minor',['G44'],'Mở /cart trong context mới.','Có thông báo kèm hình/icon theo FR-07.','Có câu thông báo nhưng không có hình/icon.'),
        ('B21','Giỏ dùng nhãn Tổng tạm tính thay cho Tổng cộng','Minor',['G45'],'Thêm sản phẩm từ Home rồi mở giỏ.','Nhãn Tổng cộng theo FR-07.','Hiển thị Tổng tạm tính.'),
        ('B22','Lỗi API danh sách/chi tiết không có thông báo khôi phục','Major',['G47','G48'],'Giả lập HTTP 503 JSON cho GET products hoặc products/1; mở trang tương ứng.','Thông báo lỗi phù hợp, không chờ vô hạn và có cách tiếp tục.','Home trống dưới form; chi tiết kẹt Đang tải. Điều kiện lỗi mạng được mô phỏng có kiểm soát.'),
        ('B23','Firefox tràn ngang 8px ở viewport 390px','Minor',['G09'],'Dùng Firefox Playwright build, viewport 390×844, mở Home.','documentElement.scrollWidth <= innerWidth.','Firefox scrollWidth=398 khi innerWidth=390. Chrome cùng kích thước là 390. Đây là viewport mobile giả lập trên desktop, không phải điện thoại thật.')
    ]
    index = json.loads((ROOT/'bug-reports/issues.json').read_text()) if (ROOT/'bug-reports/issues.json').exists() else {}
    failed_count=sum(x['Failed'] for x in counts.values())
    catalog = ['# Báo cáo lỗi GUI G2', '', f'SUT commit: `{runs["chrome"]["sutCommit"]}`. 23 nhóm lỗi từ {failed_count} mục Failed của ba lượt chạy; không phải {failed_count} bug độc lập. Chưa có phát hiện từ người tham gia usability. Severity do AI đề xuất, chờ sinh viên rà soát.', '', 'Các phát hiện heuristic được ghi rõ, không diễn giải thành yêu cầu FR bắt buộc. Ảnh gốc đính kèm từng báo cáo; xem JSON của môi trường để biết quan sát đầy đủ.', '']
    bug_data=[]
    for bid,title,severity,ids,steps,expected,actual in groups:
        affected=[(e,r) for e,run in runs.items() for r in run['results'] if r['id'] in ids and r['status']=='Failed']
        assert affected, bid
        refs=sorted({r['reference'] for _,r in affected})
        envs=sorted({r['environment'] for _,r in affected})
        issue_url=index.get(bid,{}).get('url','Chưa đăng')
        body=f'''## {bid}: {title}

Severity: **{severity}** (đề xuất, chưa có human review). Checklist: {', '.join(ids)}.

Nguồn kỳ vọng: {'; '.join(refs)}.

Môi trường: {'; '.join(envs)}. SUT: `{runs['chrome']['sutCommit']}`.

Điều kiện: bản clone riêng, seed gốc, context mới, giỏ trống. Với case dữ liệu mạng, điều kiện giả lập được ghi trong bước.

Bước tái hiện: {steps}

Kỳ vọng: {expected}

Thực tế: {actual}

GitHub Issue: {issue_url}

Ảnh bằng chứng:

'''
        for e,r in affected:
            body+=f'- {e} {r["id"]}, {r["timestamp"]}: [ảnh gốc](../{r["evidence"]}).\n'
        primary=affected[0][1]['evidence']
        body+=f'\n![{bid} bằng chứng](../{primary})\n'
        write(f'bug-reports/{bid}.md',body)
        catalog.append(body)
        bug_data.append({'id':bid,'title':title,'severity':severity,'checks':ids,'file':f'bug-reports/{bid}.md','screenshots':[r['evidence'] for _,r in affected]})
    write('bug-reports/BUG_REPORTS.md','\n\n'.join(catalog))
    write('bug-reports/catalog.json',json.dumps(bug_data,ensure_ascii=False,indent=2))
    matrix=['# Ma trận cross-browser', '', 'Đã thực thi đầy đủ 48 mục trên 3 trình duyệt thật: Chrome, Firefox và Safari. Viewport hẹp là kiểm tra responsive, không tính thêm nền tảng.', '', '| Môi trường | Số mục | Passed | Failed | Blocked |', '|---|---:|---:|---:|---:|']
    for e,run in runs.items():
        matrix.append(f'| {run["environment"]} | {len(run["results"])} | {counts[e]["Passed"]} | {counts[e]["Failed"]} | {counts[e]["Blocked"]} |')
    differences=[]
    for i,a in enumerate(chrome):
        statuses={e:run['results'][i]['status'] for e,run in runs.items()}
        if len(set(statuses.values()))>1:differences.append(f'{a["id"]}: '+', '.join(f'{e} {s}' for e,s in statuses.items()))
    matrix+=['','Khác biệt kết quả: '+'; '.join(differences)+'.','', 'Ảnh chụp dùng chú thích có email, MSSV, họ tên, browser/version, OS, URL và timestamp. Chú thích nằm ngoài SUT và được thêm sau phép đo. Thuộc tính DOM và số liệu viewport cần đọc kèm JSON.','', '## Phương pháp Safari thật','',runs['safari']['method'],'','Safari dùng iframe cùng origin để đặt đúng viewport CSS 1280px/390px mà không thay đổi layout của SUT. Các mục G37/G47/G48 định tuyến XHR mục tiêu đến fixture localhost cho delay/HTTP 503, không đổi logic SUT. Native Option-Tab được dùng để đi qua mọi phần tử trong thiết lập bàn phím Safari mặc định.','', 'Sau khi nhập, SafariDriver đôi khi chỉ blur input mà không phát click. Bộ chạy đo số DOM click và chỉ lặp lệnh khi chưa có click nào được giao; log `click_delivery` ghi lại các lần này. Mỗi hành động logic giao đúng một click, không bấm thêm để che lỗi G40. Những mục bị ảnh hưởng đã được chạy lại; chỉ kết quả cuối mỗi ID được thống kê.']
    safari=ROOT/'evidence/gui/safari/observations.json'
    if safari.exists():
        native=json.loads(safari.read_text())
        matrix+=['','## Đối chiếu với kiểm tra Safari thủ công trước đó','',f'{native["environment"]}. Trước lượt WebDriver, đã quan sát {len(native["observations"])} mục qua native UI/CUA trong iframe cùng origin. Giữ nguyên bằng chứng lịch sử này để đối chiếu, không cộng lặp vào 144 lượt của ba browser.','', '| ID | Trạng thái | Quan sát | Ảnh gốc |','|---|---|---|---|']
        for r in native['observations']:
            matrix.append('| '+' | '.join(map(cell,[r['id'],r['status'],r['notes'],f'[ảnh](../evidence/gui/safari/{r["evidence"]})']))+' |')
    matrix+=['','## Định danh trong form SUT','', 'Ngoài overlay trên ảnh Failed, có ba ảnh form đăng ký EShop thật với họ tên, MSSV và email trong trường nhập: xem `IDENTITY.md` và `evidence/identity/`. Form chưa gửi, không tạo tài khoản. Đây là bằng chứng định danh bổ sung, không cộng vào số lượt GUI hoặc usability.']
    write('cross-platform/MATRIX.md','\n'.join(matrix))
    summary=f'''# Test summary G2

Cập nhật: {now}.

| Chỉ số | Kết quả đã xác minh |
|---|---|
| Màn hình chính | Home / Product List / Search |
| Màn hình đã bao phủ | 3: Home, Product Detail, Cart |
| Luồng GUI do agent thực thi | Tìm kiếm → chi tiết → thêm giỏ; giỏ dùng để kiểm tra kết quả |
| Luồng usability đã thiết kế / chạy với người thật | 1 / 0 |
| Mục checklist thiết kế | 48; mỗi IA 12 mục |
| Chrome | 48 executed; {counts['chrome']['Passed']} Passed; {counts['chrome']['Failed']} Failed; {counts['chrome']['Blocked']} Blocked |
| Firefox | 48 executed; {counts['firefox']['Passed']} Passed; {counts['firefox']['Failed']} Failed; {counts['firefox']['Blocked']} Blocked |
| Safari | 48 executed; {counts['safari']['Passed']} Passed; {counts['safari']['Failed']} Failed; {counts['safari']['Blocked']} Blocked |
| Tổng lượt kiểm tra | 144; {sum(x['Passed'] for x in counts.values())} Passed; {sum(x['Failed'] for x in counts.values())} Failed |
| Mục fail ít nhất một môi trường | {len({r['id'] for run in runs.values() for r in run['results'] if r['status']=='Failed'})} |
| Nhóm bug | 23; {sum(b['severity']=='Major' for b in bug_data)} Major; {sum(b['severity']=='Minor' for b in bug_data)} Minor; 0 Blocker theo đánh giá sơ bộ |
| Nền tảng chạy trọn checklist | 3/3: Chrome, Firefox, Safari thật |
| Pilot / phiên chính thức có bằng chứng | 0 / 0 |
| Người tham gia thật | 0/7 |
| SUS | Chưa có dữ liệu để tính |
| Video demo skill | Đã có MP4 thật 112,4 giây, có phụ đề; chờ sinh viên xem và URL YouTube |

Kết quả là thực thi tự động bởi Codex, chưa phải xác nhận của sinh viên. Không dùng số bug hay số lượt tự động để suy ra mức hài lòng, tần suất lỗi ở người dùng, hoặc SUS.
'''
    write('reports/TEST_SUMMARY.md',summary)
    report=f'''# HW03 - GUI & Usability: Báo cáo chính G2

**BẢN NHÁP - CHƯA ĐỦ ĐIỀU KIỆN NỘP CUỐI CÙNG**

Sinh viên: Nguyễn Bảo An. MSSV: 23120207. Email: 23120207@student.hcmus.edu.vn. Bài cá nhân; phạm vi G2 được sinh viên xác nhận trong chat.

## 1. Yêu cầu và phạm vi

Đề gốc: `2026.HW03.GUI Usability_En.pdf`, §5–§6 và §9–§15; bản tiếng Việt kèm theo. Moodle assignment 40418, module 129903: hạn và cutoff đều 13:00 ngày 16/11/2026, múi giờ Việt Nam. Cho phép 20 tệp, mỗi tệp tối đa 20 MB; chưa có bài nộp. Không có attachment ở link nộp. Đã đọc section Week07 và forum GUI/Usability; không thấy đính chính HW03 trong các thread truy cập được. API báo 12 module không có quyền ở khóa học, nên không khẳng định đã đọc được mọi tài liệu hạn chế.

SUT upstream: https://github.com/ttbhanh/eshop-sut. Revision kiểm thử: `{runs['chrome']['sutCommit']}`. Backend localhost:3000, web localhost:5173; clone riêng cho HW03. Không sửa logic SUT để làm test pass. `database.js` của SUT reseed khi server khởi động, chỉ tác động bản clone riêng này.

Màn hình chính Home/Search; bổ trợ Product Detail và Cart. Luồng: tìm sản phẩm, xem thông tin, thêm vào giỏ và kiểm chứng. Kế hoạch cũ giả định có bộ lọc/sắp xếp và tai nghe dưới 500.000 ₫; SUT không có các điều khiển đó, dữ liệu seed AirPods là 6 triệu. Kịch bản mới đặt ngân sách 7 triệu, không hướng dẫn cách bấm. Đây là chỉnh sửa của AI, chưa thay thế human review.

## 2. Task 1: thiết kế và thực thi GUI checklist

48 mục phân bổ IA-01/02/03/04 mỗi khía cạnh 12 mục, có tiêu chí và nguồn FR/heuristic. Mỗi lần dùng browser context mới; chờ route và dữ liệu trước phép đo. Kết quả Passed/Failed và Notes riêng từng môi trường nằm trong `checklists/gui_checklist_g2.xlsx`, `.csv`, `.md`. JSON lưu quan sát, browser, timestamp, revision và lỗi console.

Tiêu chí hỗ trợ tiếp cận, responsive và khôi phục ngoài FR được ghi là heuristic. RTL/dark mode chưa được xác định là tính năng bắt buộc, nên không báo thiếu chúng là bug. `checklists/HUMAN_REVIEW.md` còn trống: sinh viên cần phản biện và tự bổ sung những mục AI bỏ sót, có giải thích lý do.

Chrome: {counts['chrome']['Passed']} Passed, {counts['chrome']['Failed']} Failed. Firefox: {counts['firefox']['Passed']} Passed, {counts['firefox']['Failed']} Failed. Safari: {counts['safari']['Passed']} Passed, {counts['safari']['Failed']} Failed. Không còn Blocked trong bản JSON cuối. Đã sửa lỗi đồng bộ harness và xác minh click được giao khi SafariDriver chỉ blur input. Những mục bị ảnh hưởng được chạy lại; chỉ kết quả cuối mỗi ID được thống kê. Ảnh Failed là ảnh browser thật, không phải ảnh AI sinh.

23 nhóm bug được liệt kê trong `bug-reports/BUG_REPORTS.md`. Quan trọng nhất: click thêm giỏ lần đầu không thêm; số lượng 0/âm/thập phân/rỗng được nhận; giỏ trùng dòng; từ khóa render HTML; không xác nhận xóa. HTML injection chỉ được chứng minh bằng thẻ b vô hại, không tuyên bố đã khai thác script. Heuristic crop ảnh và mất ngữ cảnh khi Back đang chờ sinh viên xác nhận mức ảnh hưởng.

## 3. Task 2: moderated usability

Đã chuẩn bị mục tiêu, kịch bản hướng mục tiêu, protocol think-aloud, consent, câu hỏi về clarity/recovery/speed/trust, phiếu SUS và mẫu pilot/P1–P7. Xem `usability/PROTOCOL.md` và `SUS_QUESTIONNAIRE.md`.

Chưa diễn ra phiên nào, chưa có danh sách người tham gia, liên hệ, ghi chú, video hay điểm SUS thật. Các CSV và mẫu phiên là biểu mẫu trống. Không kết luận độ hài lòng, thời gian hoàn thành hay mức độ phổ biến của lỗi từ các test tự động. Tính điểm khi đủ dữ liệu bằng `python3 scripts/calculate_sus.py usability/sus_responses.csv`; chương trình từ chối dữ liệu thiếu/ngoài thang và pilot. Self-check đã kiểm tra điểm 0, 50, 100 và input không hợp lệ.

Sau khi có dữ liệu thật, phân tích từng người, nhóm pain point, tách bug cụ thể khỏi vấn đề thiết kế lặp lại và ghi severity theo ảnh hưởng quan sát. `usability/FINDINGS.md` hiện chưa có finding từ người dùng.

## 4. Task 3: cross-browser

Đã chạy trọn 48 mục trên Chrome và Firefox Playwright build, cùng Safari 26.2 thật qua Apple WebDriver ở macOS 26.2. Ba trình duyệt có JSON và ảnh gốc riêng. Safari dùng iframe cùng origin có viewport CSS chính xác, không đổi logic SUT. Viewport hẹp chỉ là kiểm tra responsive. Các ca trễ/lỗi API được mô phỏng có kiểm soát và ghi rõ phương pháp. Xem `cross-platform/MATRIX.md`.

Khác biệt giữa các môi trường: {'; '.join(differences)}. G09 Firefox tràn ngang 8 px ở viewport 390 px. Safari dùng Option-Tab để điều hướng tất cả phần tử theo thiết lập mặc định. Mọi ảnh Failed có email sinh viên, MSSV, họ tên, môi trường và localhost URL ở phần chú thích, thêm sau phép đo; ảnh đặc tính DOM phải đọc cùng JSON.

Đã bổ sung ba ảnh tại `evidence/identity/` cho Chrome, Firefox và Safari thật, hiển thị họ tên, MSSV và email ngay trong form đăng ký SUT chưa gửi. Đây là minh chứng định danh cho §11, không tạo tài khoản hoặc cộng thêm màn hình vào số liệu thực thi G2. Xem `cross-platform/IDENTITY.md`.

## 5. Agent skill, AI và Git

Skill trong `skills/gui-usability-evaluator/SKILL.md` hỗ trợ chọn phạm vi, thiết kế, thực thi có chứng cứ, chuẩn bị nghiên cứu và tính SUS thật. Đã kiểm tra frontmatter và self-check của script. Video `skills/gui-usability-evaluator/video/gui-g2-demo.mp4` dài 112,4 giây được Codex ghi từ browser Chrome thật, có phụ đề và không có âm thanh. Video cho thấy nội dung skill đã đọc, quan sát Home, tìm tai nghe, mở chi tiết, tái hiện lỗi click đầu, thử workaround, kiểm chứng giỏ và liên kết báo cáo B18. Log ghi hình có timestamp và hash skill. Chưa có YouTube URL, nên chưa tuyên bố hoàn tất tiêu chí công bố demo.

`reports/AI_AUDIT_REPORT.md` và bản transcript ghi lại AI dùng trong chat hiện tại. Đã khôi phục 14 lời nhắn lập kế hoạch ngày 03/11 từ session OpenCode đúng thư mục HW03 vào `reports/AI_AUDIT_RECOVERED.md`, kèm ba đầu ra nguyên gốc ở `reports/legacy/`. Timestamp/model được lấy đúng metadata cũ; không tự tạo prompt. Sinh viên cần bổ sung nếu còn tương tác khác ngoài các nguồn này. `AI_CRITIQUE.md` vẫn là bản AI soạn, chờ sinh viên sửa theo trải nghiệm thật và xác nhận.

Commit được tạo theo giai đoạn thực sự hoàn thành. Không tạo commit giả cho phiên usability chưa diễn ra. Nhật ký được xuất bằng `git log --graph --all --stat` vào `git_commit_log.txt`.

## 6. Việc còn thiếu trước khi nộp

- Sinh viên rà soát kết quả và tự bổ sung checklist; duyệt critique/audit, bổ sung nếu còn chat khác ngoài bản đã khôi phục.
- Một pilot và bảy phiên thật ngoài lớp, danh sách liên hệ đã che, ghi chú/SUS/bằng chứng; tính và tổng hợp kết quả.
- Xem video demo MP4 đã ghi và cung cấp YouTube URL để hoàn tất tiêu chí demo.
- Xác nhận người chấm truy cập được GitHub Issues của repo đang private.
- Sinh viên tự chấm theo rubric 30/40/20/10, xác nhận bài cuối, rồi đóng gói đúng tên và xác nhận Moodle “Em làm một mình”.

## 7. Tham chiếu

Đề và chính sách đi kèm trong thư mục `requirements/` của archive. Nguồn SUS: https://hell.meiert.org/core/pdf/sus.pdf. Tài liệu phân biệt browser/engine: https://playwright.dev/docs/browsers. GitHub homework: https://github.com/NgBaoAnn/hw03-gui-usability (hiện private; người chấm cần quyền truy cập nếu dùng link).

'''+summary.replace('# Test summary G2','## 8. Test summary')
    write('reports/MAIN_REPORT.md',report)
    write('README.md','''# HW03 - GUI & Usability (G2)

Nguyễn Bảo An - 23120207 - bài cá nhân.

**BẢN NHÁP, CHƯA PHẢI BÀI NỘP HOÀN CHỈNH.** Đã chạy đủ 3 trình duyệt, khôi phục audit cũ và ghi video demo MP4 thật. Còn thiếu pilot/7 phiên thật, human review/tự bổ sung, URL YouTube, quyền xem GitHub của người chấm và điểm tự chấm.

Bắt đầu từ [hướng dẫn hoàn tất](HUONG_DAN_HOAN_TAT.md): việc cần bạn làm, biểu mẫu tương ứng và dữ liệu gửi lại để Codex chốt hồ sơ.

## Tài liệu

- `reports/MAIN_REPORT.md` và PDF: phương pháp, kết quả và giới hạn.
- `checklists/gui_checklist_g2.xlsx`, `.md`, `.csv`: 48 mục trên Chrome, Firefox và Safari thật.
- `bug-reports/BUG_REPORTS.md`: 23 nhóm bug, ảnh gốc và Issue links.
- `evidence/runs/`: kết quả máy đọc được; `evidence/gui/`: ảnh gốc.
- `usability/`: protocol, SUS, CSV và mẫu phiên trống để thu dữ liệu thật.
- `reports/AI_AUDIT_REPORT.md`, `AI_CRITIQUE.md` và PDF.
- `skills/gui-usability-evaluator/`: skill, video demo MP4 và log ghi hình thật; chờ YouTube URL.
- `reports/AI_AUDIT_RECOVERED.md`: prompt/output cũ đã khôi phục, kèm các kế hoạch nguyên gốc.
- `git_commit_log.txt`: commit thật theo bước đã hoàn tất.

## Điểm tự đánh giá

Sinh viên chưa tự chấm. Không điền 000 thay cho điểm còn thiếu.

| Tiêu chí | Tối đa | Điểm sinh viên tự chấm |
|---|---:|---|
| Task 1 - GUI Checklist | 30 | Chưa chấm |
| Task 2 - Usability Evaluation | 40 | Chưa chấm |
| Task 3 - Cross-Browser | 20 | Chưa chấm |
| Agent Skills và demo | 10 | Chưa chấm |
| Tổng | 100 | Chưa chấm |

'''+summary+'''
## Đóng gói và nộp

Chạy `python3 scripts/validate_submission.py` để kiểm tra phần còn thiếu. Trình đóng gói chỉ tạo bản `23120207_HW03_AI_GUIUsability_DRAFT.zip` khi hồ sơ chưa đủ. Bản cuối cần tên `<MSSV>_HW03_AI_GUIUsability_<000-100>.zip`, có điểm do sinh viên xác nhận. Hạn Moodle: 13:00 ngày 16/11/2026 (Việt Nam), cutoff cùng giờ, tối đa 20 MB mỗi tệp.

Không đưa `usability/private/`, dữ liệu liên hệ gốc, token, node_modules, .git hoặc bản clone SUT vào zip. GitHub hiện private; các ảnh gốc và báo cáo cũng nằm trong zip để không phụ thuộc link.
''')


if __name__ == '__main__':
    main()
