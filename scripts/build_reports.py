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
    runs = {e: json.loads((ROOT / f'evidence/runs/{e}.json').read_text()) for e in ['chrome', 'firefox']}
    chrome = runs['chrome']['results']
    firefox = runs['firefox']['results']
    assert len(chrome) == len(firefox) == len(json.loads((ROOT / 'checklists/items.json').read_text()))
    counts = {e: Counter(r['status'] for r in run['results']) for e, run in runs.items()}
    now = datetime.now(ZoneInfo('Asia/Ho_Chi_Minh')).isoformat(timespec='seconds')
    rows = []
    for a, b in zip(chrome, firefox):
        assert a['id'] == b['id']
        rows.append([a['id'], a['aspect'], a['screen'], a['criterion'], a['reference'], a['status'], b['status'], a['notes'], b['notes'], a['evidence'], b['evidence']])
    with (ROOT / 'checklists/gui_checklist_g2.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['ID', 'IA', 'Screen', 'Expected', 'Reference', 'Chrome', 'Firefox', 'Chrome notes', 'Firefox notes', 'Chrome screenshot', 'Firefox screenshot'])
        writer.writerows(rows)
    md = ['# Checklist GUI G2 đã thực thi', '', '48 mục do Codex thiết kế và thực thi tự động. Sinh viên chưa hoàn tất human review/tự bổ sung. Safari chưa chạy trọn bộ.', '', 'Bước thao tác tương ứng từng ID nằm trong `scripts/run_gui.cjs`; kết quả đầy đủ trong `evidence/runs/`. Đọc raw JSON khi Notes dưới đây được rút gọn. Ảnh là ảnh gốc từ lượt chạy, chú thích được thêm sau khi đo.', '', '| ID | IA | Màn hình | Tiêu chí | Nguồn | Chrome | Firefox | Notes Chrome (rút gọn) | Ảnh Failed |', '|---|---|---|---|---|---|---|---|---|']
    for a,b in zip(chrome,firefox):
        pics='; '.join(f'[{e}](../{r["evidence"]})' for e,r in [('Chrome',a),('Firefox',b)] if r['status']=='Failed')
        md.append('| '+' | '.join(map(cell,[a['id'],a['aspect'],a['screen'],a['criterion'],a['reference'],a['status'],b['status'],a['notes'][:180],pics]))+' |')
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
        ('B15','Danh sách thiếu loading khi đang chờ API','Minor',['G37'],'Giả lập trễ GET /api/products? 1600ms bằng Playwright, mở Home.','Có thông báo/loading indicator khi chờ.','Chỉ có tiêu đề và form tìm kiếm trong thời gian chờ. Điều kiện mạng được mô phỏng có kiểm soát.'),
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
    catalog = ['# Báo cáo lỗi GUI G2', '', f'SUT commit: `{runs["chrome"]["sutCommit"]}`. 23 nhóm lỗi từ 59 mục Failed của hai lượt chạy; không phải 59 bug độc lập. Chưa có phát hiện từ người tham gia usability. Severity do AI đề xuất, chờ sinh viên rà soát.', '', 'Các phát hiện heuristic được ghi rõ, không diễn giải thành yêu cầu FR bắt buộc. Ảnh gốc đính kèm từng báo cáo; xem JSON của môi trường để biết quan sát đầy đủ.', '']
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
    matrix=['# Ma trận cross-browser', '', 'Đã thực thi đầy đủ trên 2 môi trường. Chưa đủ yêu cầu 3 nền tảng. Viewport 390×844 là kiểm tra responsive trong cùng browser, không tính thêm nền tảng.', '', '| Môi trường | Số mục | Passed | Failed | Blocked |', '|---|---:|---:|---:|---:|']
    for e,run in runs.items():
        matrix.append(f'| {run["environment"]} | {len(run["results"])} | {counts[e]["Passed"]} | {counts[e]["Failed"]} | {counts[e]["Blocked"]} |')
    matrix+=['| Safari hoặc Android Chrome thật | Chưa chạy trọn bộ | Chưa có | Chưa có | Chưa có |','','Khác biệt: G09 Passed trên Chrome, Failed trên Firefox (398px/390px). Những Failed còn lại trùng nhau ở hai môi trường.','', 'Ảnh chụp dùng chú thích có email, MSSV, họ tên, browser/version, OS, URL và timestamp. Chú thích được thêm sau phép đo, không dùng nó làm bằng chứng về nội dung SUT. Ảnh DOM/alt và số liệu viewport cần đọc kèm JSON; screenshot không tự chứng minh thuộc tính ẩn.','', 'Để đóng Task 3: thực thi cả 48 mục trên Safari/Android Chrome thật, chụp riêng Failed với định danh. Không đổi nhãn WebKit thành Safari.']
    safari=ROOT/'evidence/gui/safari/observations.json'
    if safari.exists():
        native=json.loads(safari.read_text())
        matrix+=['','## Safari thật: kiểm tra nhanh, chưa đủ checklist','',f'{native["environment"]}. Đã quan sát {len(native["observations"])} mục qua native UI/CUA trong iframe cùng origin. Chú thích bên ngoài iframe không thay đổi logic SUT. Không cộng các mục này vào thống kê hai lượt chạy đầy đủ.','', '| ID | Trạng thái | Quan sát | Ảnh gốc |','|---|---|---|---|']
        for r in native['observations']:
            matrix.append('| '+' | '.join(map(cell,[r['id'],r['status'],r['notes'],f'[ảnh](../evidence/gui/safari/{r["evidence"]})']))+' |')
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
| Tổng lượt kiểm tra | 96; {sum(x['Passed'] for x in counts.values())} Passed; {sum(x['Failed'] for x in counts.values())} Failed |
| Mục fail ít nhất một môi trường | {len({r['id'] for run in runs.values() for r in run['results'] if r['status']=='Failed'})} |
| Nhóm bug | 23; {sum(b['severity']=='Major' for b in bug_data)} Major; {sum(b['severity']=='Minor' for b in bug_data)} Minor; 0 Blocker theo đánh giá sơ bộ |
| Nền tảng chạy trọn checklist | 2/3 |
| Pilot / phiên chính thức có bằng chứng | 0 / 0 |
| Người tham gia thật | 0/7 |
| SUS | Chưa có dữ liệu để tính |
| Video demo skill | Chưa quay, chưa có YouTube URL |

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

Chrome: {counts['chrome']['Passed']} Passed, {counts['chrome']['Failed']} Failed. Firefox: {counts['firefox']['Passed']} Passed, {counts['firefox']['Failed']} Failed. Không còn Blocked do công cụ trong bản JSON cuối. Đã sửa lỗi đồng bộ của harness sau lượt thử đầu rồi chạy lại cả hai môi trường; chỉ JSON cuối là nguồn thống kê. Ảnh Failed là ảnh browser thật có chú thích riêng, không phải ảnh AI sinh.

23 nhóm bug được liệt kê trong `bug-reports/BUG_REPORTS.md`. Quan trọng nhất: click thêm giỏ lần đầu không thêm; số lượng 0/âm/thập phân/rỗng được nhận; giỏ trùng dòng; từ khóa render HTML; không xác nhận xóa. HTML injection chỉ được chứng minh bằng thẻ b vô hại, không tuyên bố đã khai thác script. Heuristic crop ảnh và mất ngữ cảnh khi Back đang chờ sinh viên xác nhận mức ảnh hưởng.

## 3. Task 2: moderated usability

Đã chuẩn bị mục tiêu, kịch bản hướng mục tiêu, protocol think-aloud, consent, câu hỏi về clarity/recovery/speed/trust, phiếu SUS và mẫu pilot/P1–P7. Xem `usability/PROTOCOL.md` và `SUS_QUESTIONNAIRE.md`.

Chưa diễn ra phiên nào, chưa có danh sách người tham gia, liên hệ, ghi chú, video hay điểm SUS thật. Các CSV và mẫu phiên là biểu mẫu trống. Không kết luận độ hài lòng, thời gian hoàn thành hay mức độ phổ biến của lỗi từ các test tự động. Tính điểm khi đủ dữ liệu bằng `python3 scripts/calculate_sus.py usability/sus_responses.csv`; chương trình từ chối dữ liệu thiếu/ngoài thang và pilot. Self-check đã kiểm tra điểm 0, 50, 100 và input không hợp lệ.

Sau khi có dữ liệu thật, phân tích từng người, nhóm pain point, tách bug cụ thể khỏi vấn đề thiết kế lặp lại và ghi severity theo ảnh hưởng quan sát. `usability/FINDINGS.md` hiện chưa có finding từ người dùng.

## 4. Task 3: cross-browser

Đã chạy trọn 48 mục trên Chrome và Firefox Playwright build ở macOS 26.2. Đã thử viewport desktop và 390×844; đây không phải hai nền tảng khác nhau. Chưa chạy trọn trên Safari/Android Chrome thật nên Task 3 chưa hoàn tất. Xem `cross-platform/MATRIX.md`.

G09 khác nhau: Firefox tràn ngang 8 px ở 390 px; Chrome không tràn. Các phát hiện khác trùng nhau trong hai lượt ghi nhận. Mọi ảnh Failed có email sinh viên, MSSV, họ tên, môi trường và localhost URL ở phần chú thích, thêm sau khi đo; ảnh đặc tính DOM phải đọc cùng JSON.

## 5. Agent skill, AI và Git

Skill trong `skills/gui-usability-evaluator/SKILL.md` hỗ trợ chọn phạm vi, thiết kế, thực thi có chứng cứ, chuẩn bị nghiên cứu và tính SUS thật. Đã kiểm tra frontmatter và các self-check của script. `DEMO.md` là kịch bản video, chưa phải video hoặc YouTube link. Chưa tuyên bố hoàn thành tiêu chí demo.

`reports/AI_AUDIT_REPORT.md` và bản transcript ghi lại AI dùng trong chat hiện tại; đầu ra chính là các artifact được liên kết. Tương tác trước phiên hiện tại chưa có bản xuất đầy đủ, không gán ngày giờ/prompt giả cho các kế hoạch cũ. `AI_CRITIQUE.md` là bản AI soạn để sinh viên sửa theo trải nghiệm thật, chưa phải lời phản biện được sinh viên xác nhận.

Commit được tạo theo giai đoạn thực sự hoàn thành. Không tạo commit giả cho phiên usability chưa diễn ra. Nhật ký được xuất bằng `git log --graph --all --stat` vào `git_commit_log.txt`.

## 6. Việc còn thiếu trước khi nộp

- Sinh viên rà soát kết quả và tự bổ sung checklist; duyệt critique, hoàn thiện audit các tương tác cũ.
- Một pilot và bảy phiên thật ngoài lớp, danh sách liên hệ đã che, ghi chú/SUS/bằng chứng; tính và tổng hợp kết quả.
- Chạy trọn checklist trên nền tảng thứ ba hợp lệ.
- Quay demo skill end-to-end và cung cấp YouTube link nếu muốn hoàn tất tiêu chí skill.
- Sinh viên tự chấm theo rubric 30/40/20/10, xác nhận bài cuối, rồi đóng gói đúng tên và xác nhận Moodle “Em làm một mình”.

## 7. Tham chiếu

Đề và chính sách đi kèm trong thư mục `requirements/` của archive. Nguồn SUS: https://hell.meiert.org/core/pdf/sus.pdf. Tài liệu phân biệt browser/engine: https://playwright.dev/docs/browsers. GitHub homework: https://github.com/NgBaoAnn/hw03-gui-usability (hiện private; người chấm cần quyền truy cập nếu dùng link).

'''+summary.replace('# Test summary G2','## 8. Test summary')
    write('reports/MAIN_REPORT.md',report)
    write('README.md','''# HW03 - GUI & Usability (G2)

Nguyễn Bảo An - 23120207 - bài cá nhân.

**BẢN NHÁP, CHƯA PHẢI BÀI NỘP HOÀN CHỈNH.** Thiếu pilot/7 phiên thật, human review/tự bổ sung, nền tảng thứ ba chạy trọn checklist, demo YouTube và điểm tự chấm. Không nộp bản này như bài đã hoàn tất.

## Tài liệu

- `reports/MAIN_REPORT.md` và PDF: phương pháp, kết quả và giới hạn.
- `checklists/gui_checklist_g2.xlsx`, `.md`, `.csv`: 48 mục và hai lượt chạy.
- `bug-reports/BUG_REPORTS.md`: 23 nhóm bug, ảnh gốc và Issue links.
- `evidence/runs/`: kết quả máy đọc được; `evidence/gui/`: ảnh gốc.
- `usability/`: protocol, SUS, CSV và mẫu phiên trống để thu dữ liệu thật.
- `reports/AI_AUDIT_REPORT.md`, `AI_CRITIQUE.md` và PDF.
- `skills/gui-usability-evaluator/`: skill và kịch bản demo chưa quay.
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
