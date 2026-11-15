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

Chrome: 19 Passed, 29 Failed. Firefox: 18 Passed, 30 Failed. Safari: 19 Passed, 29 Failed. Không còn Blocked trong bản JSON cuối. Đã sửa lỗi đồng bộ harness và xác minh click được giao khi SafariDriver chỉ blur input. Những mục bị ảnh hưởng được chạy lại; chỉ kết quả cuối mỗi ID được thống kê. Ảnh Failed là ảnh browser thật, không phải ảnh AI sinh.

23 nhóm bug được liệt kê trong `bug-reports/BUG_REPORTS.md`. Quan trọng nhất: click thêm giỏ lần đầu không thêm; số lượng 0/âm/thập phân/rỗng được nhận; giỏ trùng dòng; từ khóa render HTML; không xác nhận xóa. HTML injection chỉ được chứng minh bằng thẻ b vô hại, không tuyên bố đã khai thác script. Heuristic crop ảnh và mất ngữ cảnh khi Back đang chờ sinh viên xác nhận mức ảnh hưởng.

## 3. Task 2: moderated usability

Sinh viên bổ sung hồ sơ `task2_usability/` ngày 15/11/2026 và xác nhận trong chat rằng đã tự điều phối một pilot và bảy phiên thật. Theo yêu cầu sinh viên, thông tin người nộp được đồng bộ Nguyễn Bảo An – 23120207. Luồng Task 2 là đăng nhập → tìm lịch sử → nhận diện trạng thái → hủy đơn pending → xác nhận kết quả, khác phạm vi GUI G2 ở Task 1. Đề cho phép chọn riêng màn hình GUI và luồng usability.

Hồ sơ có mục tiêu, kịch bản v0/v1 và điều chỉnh sau pilot, lời dẫn think-aloud, ghi chú bảy phiên, 10 câu SUS và bốn nhóm probe. Pilot không tính vào thống kê. Mã nguồn P01–P07 được ánh xạ P1–P7 trong CSV chuẩn; không thay câu trả lời. SUS = tổng (câu lẻ − 1, 5 − câu chẵn) × 2,5. Chạy `python3 scripts/calculate_sus.py usability/sus_responses.csv` để tái tính. Đã đối chiếu 70 câu trả lời giữa CSV/JSON, điểm từng người, kết quả tác vụ, thời gian và tần suất năm nhóm vấn đề. SUS là điểm thang 0–100, không phải phần trăm.

SUS trung bình **58.93**, trung vị **62.50**, SD mẫu **20.91**. Bốn ca hoàn thành độc lập, hai có trợ giúp, một timeout 600 giây: tỷ lệ hoàn thành 6/7 (85,7%). Thời gian trung bình toàn mẫu 324 giây; chỉ sáu ca hoàn thành là 278 giây. Không suy rộng mẫu nhỏ này thành toàn bộ người dùng.

`usability/FINDINGS.md` nhóm năm vấn đề: lối vào lịch sử khó nhận biết (5/7), tiêu đề đăng nhập sai (3/7), affordance hủy đơn đang giao (3/7), thiếu xác nhận trước hủy (3/7), thiếu thông tin sản phẩm trong danh sách đơn (4/7). U02 là lỗi nhãn cụ thể; U01/U04/U05 là vấn đề thiết kế lặp lại. Ảnh `evidence/usability/` là agent tái hiện sau khi nhận dữ liệu, không phải ảnh/video phiên người tham gia. Báo cáo và Issue riêng ghi rõ giới hạn này.

Hồ sơ nguồn ghi tất cả người tham gia từ chối ghi hình; không có video phiên. §6 hướng dẫn quay màn hình; §14 của đề tiếng Anh quy định nộp screen recordings where available (bản quay khi có). Hồ sơ vì vậy kèm ghi chú có cấu trúc, SUS/probe và nêu rõ giới hạn không có bản quay, không gán ảnh tái hiện thành bằng chứng phiên. Tính xác thực dựa trên xác nhận của sinh viên; Codex không xác minh độc lập danh tính hay việc diễn ra các phiên. Danh sách họ tên/liên hệ đã che chỉ nằm trong hồ sơ nộp, không đẩy lên repo public. Xem `usability/provenance.json`.

## 4. Task 3: cross-browser

Đã chạy trọn 48 mục trên Chrome và Firefox Playwright build, cùng Safari 26.2 thật qua Apple WebDriver ở macOS 26.2. Ba trình duyệt có JSON và ảnh gốc riêng. Safari dùng iframe cùng origin có viewport CSS chính xác, không đổi logic SUT. Viewport hẹp chỉ là kiểm tra responsive. Các ca trễ/lỗi API được mô phỏng có kiểm soát và ghi rõ phương pháp. Xem `cross-platform/MATRIX.md`.

Khác biệt giữa các môi trường: G09: chrome Passed, firefox Failed, safari Passed. G09 Firefox tràn ngang 8 px ở viewport 390 px. Safari dùng Option-Tab để điều hướng tất cả phần tử theo thiết lập mặc định. Mọi ảnh Failed có email sinh viên, MSSV, họ tên, môi trường và localhost URL ở phần chú thích, thêm sau phép đo; ảnh đặc tính DOM phải đọc cùng JSON.

Đã bổ sung ba ảnh tại `evidence/identity/` cho Chrome, Firefox và Safari thật, hiển thị họ tên, MSSV và email ngay trong form đăng ký SUT chưa gửi. Đây là minh chứng định danh cho §11, không tạo tài khoản hoặc cộng thêm màn hình vào số liệu thực thi G2. Xem `cross-platform/IDENTITY.md`.

## 5. Agent skill, AI và Git

Skill trong `skills/gui-usability-evaluator/SKILL.md` hỗ trợ chọn phạm vi, thiết kế, thực thi có chứng cứ, chuẩn bị nghiên cứu và tính SUS thật. Đã kiểm tra frontmatter và self-check của script. Video `skills/gui-usability-evaluator/video/gui-g2-demo.mp4` dài 112,4 giây là tài liệu tham khảo do Codex ghi từ Chrome thật, có phụ đề, không có âm thanh và có log timestamp/hash skill. Sinh viên đã chọn tự quay video dùng cho bài nộp; hiện chưa có video hoặc YouTube URL của sinh viên. Không gán video Codex thành bản quay của sinh viên hoặc tính hoàn tất tiêu chí demo.

`reports/AI_AUDIT_REPORT.md` và bản transcript ghi lại AI dùng trong chat hiện tại. Đã khôi phục 14 lời nhắn lập kế hoạch ngày 03/11 từ session OpenCode đúng thư mục HW03 vào `reports/AI_AUDIT_RECOVERED.md`, kèm ba đầu ra nguyên gốc ở `reports/legacy/`. Timestamp/model được lấy đúng metadata cũ; không tự tạo prompt. Sinh viên cần bổ sung nếu còn tương tác khác ngoài các nguồn này. `AI_CRITIQUE.md` vẫn là bản AI soạn, chờ sinh viên sửa theo trải nghiệm thật và xác nhận.

Commit được tạo theo giai đoạn thực sự hoàn thành. Hồ sơ tám phiên được nhập cùng lúc ngày 15/11/2026; không tạo hoặc lùi ngày commit như thể đã ghi từng phiên ngày 10/11. Đây là giới hạn tuân thủ yêu cầu nhật ký theo từng phiên. Nhật ký xuất bằng `git log --graph --all --stat` vào `git_commit_log.txt`.

## 6. Việc còn thiếu trước khi nộp

- Sinh viên rà soát kết quả và tự bổ sung checklist; duyệt critique/audit, bổ sung nếu còn chat khác ngoài bản đã khôi phục.
- Sinh viên tự quay demo dùng skill từ đầu đến cuối và cung cấp YouTube URL.
- Sinh viên tự chấm theo rubric 30/40/20/10, xác nhận bài cuối, rồi đóng gói đúng tên và xác nhận Moodle “Em làm một mình”.

## 7. Tham chiếu

Đề và chính sách đi kèm trong thư mục `requirements/` của archive. Nguồn SUS: https://hell.meiert.org/core/pdf/sus.pdf. Tài liệu phân biệt browser/engine: https://playwright.dev/docs/browsers. GitHub homework: https://github.com/NgBaoAnn/hw03-gui-usability (đã public theo xác nhận của sinh viên, người chấm truy cập được các Issues và ảnh).

## 8. Test summary

Cập nhật: 2026-11-15T23:41:55+07:00.

| Chỉ số | Kết quả đã xác minh |
|---|---|
| Màn hình chính | Home / Product List / Search |
| Màn hình đã bao phủ | 3: Home, Product Detail, Cart |
| Luồng GUI do agent thực thi | Tìm kiếm → chi tiết → thêm giỏ; giỏ dùng để kiểm tra kết quả |
| Luồng usability | Quản lý đơn hàng; 1 pilot + 7 phiên do sinh viên cung cấp và xác nhận |
| Mục checklist thiết kế | 48; mỗi IA 12 mục |
| Chrome | 48 executed; 19 Passed; 29 Failed; 0 Blocked |
| Firefox | 48 executed; 18 Passed; 30 Failed; 0 Blocked |
| Safari | 48 executed; 19 Passed; 29 Failed; 0 Blocked |
| Tổng lượt kiểm tra | 144; 56 Passed; 88 Failed |
| Mục fail ít nhất một môi trường | 30 |
| Nhóm bug | 23; 10 Major; 13 Minor; 0 Blocker theo đánh giá sơ bộ |
| Nền tảng chạy trọn checklist | 3/3: Chrome, Firefox, Safari thật |
| Pilot / phiên chính thức có ghi chú | 1 / 7; không có video phiên |
| Người tham gia | 7/7 theo dữ liệu sinh viên cung cấp, ngoài pilot |
| SUS | 58.93/100; trung vị 62.50; SD mẫu 20.91 |
| Hoàn thành tác vụ | 6/7 (85,7%): 4 độc lập, 2 có trợ giúp, 1 timeout |
| Thời gian tác vụ | 324 giây gồm timeout; 278 giây trong 6 ca hoàn thành |
| Phát hiện usability | 5 vấn đề U01–U05; tách khỏi 23 bug GUI |
| Video demo skill | MP4 do Codex ghi được giữ tham khảo; chờ video sinh viên tự quay và URL YouTube |

Kết quả GUI do Codex thực thi tự động. Kết quả usability lấy từ hồ sơ sinh viên cung cấp và xác nhận trong chat ngày 15/11/2026; phép tính được đối chiếu độc lập với CSV/JSON. Không suy ra SUS từ kiểm thử tự động. Không có video phiên; §14 yêu cầu kèm bản quay khi có, nên giữ rõ giới hạn này.
