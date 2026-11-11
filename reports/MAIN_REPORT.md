# HW03 - GUI & Usability: Báo cáo chính G2

**BẢN NHÁP - CHƯA ĐỦ ĐIỀU KIỆN NỘP CUỐI CÙNG**

Sinh viên: Nguyễn Bảo An. MSSV: 23120207. Email: 23120207@student.hcmus.edu.vn. Bài cá nhân; phạm vi G2 được sinh viên xác nhận trong chat.

## 1. Yêu cầu và phạm vi

Đề gốc: `2026.HW03.GUI Usability_En.pdf`, §5–§6 và §9–§15; bản tiếng Việt kèm theo. Moodle assignment 40418, module 129903: hạn và cutoff đều 13:00 ngày 16/11/2026, múi giờ Việt Nam. Cho phép 20 tệp, mỗi tệp tối đa 20 MB; chưa có bài nộp. Không có attachment ở link nộp. Đã đọc section Week07 và forum GUI/Usability; không thấy đính chính HW03 trong các thread truy cập được. API báo 12 module không có quyền ở khóa học, nên không khẳng định đã đọc được mọi tài liệu hạn chế.

SUT upstream: https://github.com/ttbhanh/eshop-sut. Revision kiểm thử: `85af3ba875c88283615e22cb108f13e2fccaf0e9`. Backend localhost:3000, web localhost:5173; clone riêng cho HW03. Không sửa logic SUT để làm test pass. `database.js` của SUT reseed khi server khởi động, chỉ tác động bản clone riêng này.

Màn hình chính Home/Search; bổ trợ Product Detail và Cart. Luồng: tìm sản phẩm, xem thông tin, thêm vào giỏ và kiểm chứng. Kế hoạch cũ giả định có bộ lọc/sắp xếp và tai nghe dưới 500.000 ₫; SUT không có các điều khiển đó, dữ liệu seed AirPods là 6 triệu. Kịch bản mới đặt ngân sách 7 triệu, không hướng dẫn cách bấm. Đây là chỉnh sửa của AI, chưa thay thế human review.

## 2. Task 1: thiết kế và thực thi GUI checklist

48 mục phân bổ IA-01/02/03/04 mỗi khía cạnh 12 mục, có tiêu chí và nguồn FR/heuristic. Mỗi lần dùng browser context mới; chờ route và dữ liệu trước phép đo. Kết quả Passed/Failed và Notes riêng từng môi trường nằm trong `checklists/gui_checklist_g2.xlsx`, `.csv`, `.md`. JSON lưu quan sát, browser, timestamp, revision và lỗi console.

Tiêu chí hỗ trợ tiếp cận, responsive và khôi phục ngoài FR được ghi là heuristic. RTL/dark mode chưa được xác định là tính năng bắt buộc, nên không báo thiếu chúng là bug. `checklists/HUMAN_REVIEW.md` còn trống: sinh viên cần phản biện và tự bổ sung những mục AI bỏ sót, có giải thích lý do.

Chrome: 19 Passed, 29 Failed. Firefox: 18 Passed, 30 Failed. Không còn Blocked do công cụ trong bản JSON cuối. Đã sửa lỗi đồng bộ của harness sau lượt thử đầu rồi chạy lại cả hai môi trường; chỉ JSON cuối là nguồn thống kê. Ảnh Failed là ảnh browser thật có chú thích riêng, không phải ảnh AI sinh.

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

## 8. Test summary

Cập nhật: 2026-11-11T22:16:45+07:00.

| Chỉ số | Kết quả đã xác minh |
|---|---|
| Màn hình chính | Home / Product List / Search |
| Màn hình đã bao phủ | 3: Home, Product Detail, Cart |
| Luồng GUI do agent thực thi | Tìm kiếm → chi tiết → thêm giỏ; giỏ dùng để kiểm tra kết quả |
| Luồng usability đã thiết kế / chạy với người thật | 1 / 0 |
| Mục checklist thiết kế | 48; mỗi IA 12 mục |
| Chrome | 48 executed; 19 Passed; 29 Failed; 0 Blocked |
| Firefox | 48 executed; 18 Passed; 30 Failed; 0 Blocked |
| Tổng lượt kiểm tra | 96; 37 Passed; 59 Failed |
| Mục fail ít nhất một môi trường | 30 |
| Nhóm bug | 23; 10 Major; 13 Minor; 0 Blocker theo đánh giá sơ bộ |
| Nền tảng chạy trọn checklist | 2/3 |
| Pilot / phiên chính thức có bằng chứng | 0 / 0 |
| Người tham gia thật | 0/7 |
| SUS | Chưa có dữ liệu để tính |
| Video demo skill | Chưa quay, chưa có YouTube URL |

Kết quả là thực thi tự động bởi Codex, chưa phải xác nhận của sinh viên. Không dùng số bug hay số lượt tự động để suy ra mức hài lòng, tần suất lỗi ở người dùng, hoặc SUS.
