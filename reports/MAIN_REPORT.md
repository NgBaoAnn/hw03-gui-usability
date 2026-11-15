# HW03 - GUI & Usability: Báo cáo chính G2

**HỒ SƠ CHUẨN BỊ NỘP - CÓ GIỚI HẠN HUMAN REVIEW NÊU TẠI §6**

Sinh viên: Nguyễn Bảo An. MSSV: 23120207. Email: 23120207@student.hcmus.edu.vn. Bài cá nhân; phạm vi G2 được sinh viên xác nhận trong chat.

## 1. Yêu cầu và phạm vi

Đề gốc: `2026.HW03.GUI Usability_En.pdf`, §5–§6 và §9–§15; bản tiếng Việt kèm theo. Moodle assignment 40418, module 129903: hạn và cutoff đều 13:00 ngày 16/11/2026, múi giờ Việt Nam. Cho phép 20 tệp, mỗi tệp tối đa 20 MB; chưa có bài nộp. Không có attachment ở link nộp. Đã đọc section Week07 và forum GUI/Usability; không thấy đính chính HW03 trong các thread truy cập được. API báo 12 module không có quyền ở khóa học, nên không khẳng định đã đọc được mọi tài liệu hạn chế.

SUT upstream: https://github.com/ttbhanh/eshop-sut. Revision kiểm thử: `85af3ba875c88283615e22cb108f13e2fccaf0e9`. Backend localhost:3000, web localhost:5173; clone riêng cho HW03. Không sửa logic SUT để làm test pass. `database.js` của SUT reseed khi server khởi động, chỉ tác động bản clone riêng này.

Màn hình chính Home/Search; bổ trợ Product Detail và Cart. Luồng: tìm sản phẩm, xem thông tin, thêm vào giỏ và kiểm chứng. Kế hoạch cũ giả định có bộ lọc/sắp xếp và tai nghe dưới 500.000 ₫; SUT không có các điều khiển đó, dữ liệu seed AirPods là 6 triệu. Kịch bản mới đặt ngân sách 7 triệu, không hướng dẫn cách bấm. Đây là chỉnh sửa của AI, chưa thay thế human review.

## 2. Task 1: thiết kế và thực thi GUI checklist

Bộ đầu có 48 mục, mỗi IA 12 mục. Sau phản biện, thêm G49–G51: tổng 51 mục, IA-01/02/03/04 = 14/13/12/12. items.json giữ nguyên bộ đầu; additions.json lưu phần thêm. Tất cả do AI thiết kế/thực hiện theo yêu cầu sinh viên. Bộ gốc dùng browser context mới theo case; phần bổ sung mở từng URL trong cửa sổ browser thật và chỉ đọc DOM/CSS. Chờ route và dữ liệu trước phép đo. Kết quả Passed/Failed và Notes riêng từng môi trường nằm trong `checklists/gui_checklist_g2.xlsx`, `.csv`, `.md`. JSON lưu quan sát, browser, timestamp, revision và lỗi console.

Tiêu chí hỗ trợ tiếp cận, responsive và khôi phục ngoài FR được ghi là heuristic. RTL/dark mode chưa được xác định là tính năng bắt buộc, nên không báo thiếu chúng là bug. `checklists/HUMAN_REVIEW.md` còn trống: sinh viên cần phản biện và tự bổ sung những mục AI bỏ sót, có giải thích lý do.

Codex đã thực hiện lượt rà soát bổ sung theo yêu cầu sinh viên, ghi tại `checklists/AI_REVIEW.md`: đối chiếu số liệu, nguồn kỳ vọng, phạm vi kết luận và giới hạn công cụ. Đây là rà soát của AI, chưa được gán thành phần sinh viên tự phản biện/bổ sung.

Chrome: 19 Passed, 32 Failed. Firefox: 18 Passed, 33 Failed. Safari: 19 Passed, 32 Failed. Không còn Blocked trong bản JSON cuối. Đã sửa lỗi đồng bộ harness và xác minh click được giao khi SafariDriver chỉ blur input. Những mục bị ảnh hưởng được chạy lại; chỉ kết quả cuối mỗi ID được thống kê. Ảnh Failed là ảnh browser thật, không phải ảnh AI sinh.

23 nhóm bug được liệt kê trong `bug-reports/BUG_REPORTS.md`. Quan trọng nhất: click thêm giỏ lần đầu không thêm; số lượng 0/âm/thập phân/rỗng được nhận; giỏ trùng dòng; từ khóa render HTML; không xác nhận xóa. HTML injection chỉ được chứng minh bằng thẻ b vô hại, không tuyên bố đã khai thác script. Heuristic crop ảnh và mất ngữ cảnh khi Back đang chờ sinh viên xác nhận mức ảnh hưởng.

## 3. Task 2: moderated usability

Sinh viên bổ sung hồ sơ `task2_usability/` ngày 15/11/2026 và xác nhận trong chat rằng đã tự điều phối một pilot và bảy phiên thật. Theo yêu cầu sinh viên, thông tin người nộp được đồng bộ Nguyễn Bảo An – 23120207. Luồng Task 2 là đăng nhập → tìm lịch sử → nhận diện trạng thái → hủy đơn pending → xác nhận kết quả, khác phạm vi GUI G2 ở Task 1. Đề cho phép chọn riêng màn hình GUI và luồng usability.

Hồ sơ có mục tiêu, kịch bản v0/v1 và điều chỉnh sau pilot, lời dẫn think-aloud, ghi chú bảy phiên, 10 câu SUS và bốn nhóm probe. Pilot không tính vào thống kê. Mã nguồn P01–P07 được ánh xạ P1–P7 trong CSV chuẩn; không thay câu trả lời. SUS = tổng (câu lẻ − 1, 5 − câu chẵn) × 2,5. Chạy `python3 scripts/calculate_sus.py usability/sus_responses.csv` để tái tính. Đã đối chiếu 70 câu trả lời giữa CSV/JSON, điểm từng người, kết quả tác vụ, thời gian và tần suất năm nhóm vấn đề. SUS là điểm thang 0–100, không phải phần trăm.

SUS trung bình **58.93**, trung vị **62.50**, SD mẫu **20.91**. Bốn ca hoàn thành độc lập, hai có trợ giúp, một timeout 600 giây: tỷ lệ hoàn thành 6/7 (85,7%). Thời gian trung bình toàn mẫu 324 giây; chỉ sáu ca hoàn thành là 278 giây. Không suy rộng mẫu nhỏ này thành toàn bộ người dùng.

`usability/FINDINGS.md` nhóm năm vấn đề: lối vào lịch sử khó nhận biết (5/7), tiêu đề đăng nhập sai (3/7), affordance hủy đơn đang giao (3/7), thiếu xác nhận trước hủy (3/7), thiếu thông tin sản phẩm trong danh sách đơn (4/7). U02 là lỗi nhãn cụ thể; U01/U04/U05 là vấn đề thiết kế lặp lại. Ảnh `evidence/usability/` là agent tái hiện sau khi nhận dữ liệu, không phải ảnh/video phiên người tham gia. Báo cáo và Issue riêng ghi rõ giới hạn này.

Hồ sơ nguồn ghi tất cả người tham gia từ chối ghi hình; không có video phiên. §6 hướng dẫn quay màn hình; §14 của đề tiếng Anh quy định nộp screen recordings where available (bản quay khi có). Hồ sơ vì vậy kèm ghi chú có cấu trúc, SUS/probe và nêu rõ giới hạn không có bản quay, không gán ảnh tái hiện thành bằng chứng phiên. Tính xác thực dựa trên xác nhận của sinh viên; Codex không xác minh độc lập danh tính hay việc diễn ra các phiên. Danh sách họ tên/liên hệ đã che chỉ nằm trong hồ sơ nộp, không đẩy lên repo public. Xem `usability/provenance.json`.

## 4. Task 3: cross-browser

Đã chạy bộ gốc 48 mục trên Chrome/Firefox Playwright build và Safari 26.2 qua Apple WebDriver ở macOS 26.2; thêm G49–G51 trên cả ba browser qua native CUA, tổng 51 mục/môi trường. Ba trình duyệt có JSON và ảnh gốc riêng. Safari dùng iframe cùng origin có viewport CSS chính xác, không đổi logic SUT. Viewport hẹp chỉ là kiểm tra responsive. Các ca trễ/lỗi API được mô phỏng có kiểm soát và ghi rõ phương pháp. Xem `cross-platform/MATRIX.md`.

Khác biệt giữa các môi trường: G09: chrome Passed, firefox Failed, safari Passed. G09 Firefox tràn ngang 8 px ở viewport 390 px. Safari dùng Option-Tab để điều hướng tất cả phần tử theo thiết lập mặc định. Mọi ảnh Failed có email sinh viên, MSSV, họ tên, môi trường và localhost URL ở phần chú thích, thêm sau phép đo; ảnh đặc tính DOM phải đọc cùng JSON.

Đã bổ sung ba ảnh tại `evidence/identity/` cho Chrome, Firefox và Safari thật, hiển thị họ tên, MSSV và email ngay trong form đăng ký SUT chưa gửi. Đây là minh chứng định danh cho §11, không tạo tài khoản hoặc cộng thêm màn hình vào số liệu thực thi G2. Xem `cross-platform/IDENTITY.md`.

## 5. Agent skill, AI và Git

Skill trong `skills/gui-usability-evaluator/SKILL.md` hỗ trợ chọn phạm vi, thiết kế, thực thi có chứng cứ, chuẩn bị nghiên cứu và tính SUS thật. Đã kiểm tra frontmatter và self-check của script. Video do sinh viên cung cấp: https://youtu.be/VGVm_V7L_ks (10:38 theo YouTube UI; metadata làm tròn 639 giây). Đã kiểm tra phát khi không đăng nhập. Bản skill thực sự dùng được giữ nguyên tại `skills/gui-usability-evaluator/demo-version/`, kèm checklist và SUS scorer; bản gốc của homework vẫn ở thư mục cha. Demo mở rộng từ tìm AirPods Pro 2 đến checkout và hậu kiểm đơn #9, không cộng lượt demo vào 153 kết quả cross-browser. Bằng chứng gốc tại `evidence/demo/`, transcript riêng tại `reports/AI_DEMO_TRANSCRIPT.md`; mô tả và giới hạn trong `skills/gui-usability-evaluator/DEMO.md`. File MP4 tham khảo cũ do Codex ghi đã được sinh viên loại khỏi hồ sơ; bài nộp dùng link video của sinh viên.

`reports/AI_AUDIT_REPORT.md` và bản transcript ghi lại AI dùng trong chat hiện tại. Đã khôi phục 14 lời nhắn lập kế hoạch ngày 03/11 từ session OpenCode đúng thư mục HW03 vào `reports/AI_AUDIT_RECOVERED.md`, kèm ba đầu ra nguyên gốc ở `reports/legacy/`. Timestamp/model được lấy đúng metadata cũ; không tự tạo prompt. Sinh viên cần bổ sung nếu còn tương tác khác ngoài các nguồn này. `AI_CRITIQUE.md` vẫn là bản AI soạn, chờ sinh viên sửa theo trải nghiệm thật và xác nhận.

Commit được tạo theo giai đoạn thực sự hoàn thành. Hồ sơ tám phiên được nhập cùng lúc ngày 15/11/2026; không tạo hoặc lùi ngày commit như thể đã ghi từng phiên ngày 10/11. Đây là giới hạn tuân thủ yêu cầu nhật ký theo từng phiên. Nhật ký xuất bằng `git log --graph --all --stat` vào `git_commit_log.txt`.

## 6. Việc còn thiếu trước khi nộp

- Sinh viên rà soát kết quả và tự bổ sung checklist; duyệt critique/audit, bổ sung nếu còn chat khác ngoài bản đã khôi phục.
- Demo đã được sinh viên cung cấp và kiểm tra phát công khai: https://youtu.be/VGVm_V7L_ks .
- Sinh viên đã chọn tự chấm 30/40/20/10 = 100. Điểm tự chấm không xác nhận phần human review đã hoàn tất. Sau khi đủ các mục còn thiếu, xác nhận bài cuối và Moodle “Em làm một mình”.

Điểm tự chấm do sinh viên lựa chọn; không phải điểm giảng viên hoặc xác nhận mọi yêu cầu đã hoàn tất.

| Tiêu chí | Tối đa | Điểm sinh viên tự chấm |
|---|---:|---:|
| Task 1 - GUI Checklist | 30 | 30 |
| Task 2 - Usability Evaluation | 40 | 40 |
| Task 3 - Đa trình duyệt | 20 | 20 |
| Agent Skills và demo | 10 | 10 |
| Tổng | 100 | 100 |

## 7. Tham chiếu

Đề và chính sách đi kèm trong thư mục `requirements/` của archive. Nguồn SUS: https://hell.meiert.org/core/pdf/sus.pdf. Tài liệu phân biệt browser/engine: https://playwright.dev/docs/browsers. GitHub homework: https://github.com/NgBaoAnn/hw03-gui-usability (đã public theo xác nhận của sinh viên, người chấm truy cập được các Issues và ảnh).

## 8. Test summary

Cập nhật: 2026-11-16T01:28:07+07:00.

| Chỉ số | Kết quả đã xác minh |
|---|---|
| Màn hình chính | Home / Product List / Search |
| Màn hình đã bao phủ | 3: Home, Product Detail, Cart |
| Luồng GUI do agent thực thi | Tìm kiếm → chi tiết → thêm giỏ; giỏ dùng để kiểm tra kết quả |
| Luồng usability | Quản lý đơn hàng; 1 pilot + 7 phiên do sinh viên cung cấp và xác nhận |
| Mục checklist thiết kế | 51: 48 gốc + G49–G51 bổ sung; IA-01/02/03/04 = 14/13/12/12 |
| Chrome | 51 executed; 19 Passed; 32 Failed; 0 Blocked |
| Firefox | 51 executed; 18 Passed; 33 Failed; 0 Blocked |
| Safari | 51 executed; 19 Passed; 32 Failed; 0 Blocked |
| Tổng lượt kiểm tra | 153: 144 gốc + 9 bổ sung; 56 Passed; 97 Failed |
| Mục fail ít nhất một môi trường | 33 |
| Nhóm bug GUI | 25: 23 gốc + B24/B25; 12 Major, 13 Minor; 0 Blocker theo đánh giá sơ bộ |
| Nền tảng chạy trọn checklist | 3/3: Chrome, Firefox, Safari thật |
| Pilot / phiên chính thức có ghi chú | 1 / 7; không có video phiên |
| Người tham gia | 7/7 theo dữ liệu sinh viên cung cấp, ngoài pilot |
| SUS | 58.93/100; trung vị 62.50; SD mẫu 20.91 |
| Hoàn thành tác vụ | 6/7 (85,7%): 4 độc lập, 2 có trợ giúp, 1 timeout |
| Thời gian tác vụ | 324 giây gồm timeout; 278 giây trong 6 ca hoàn thành |
| Phát hiện usability | 5 vấn đề U01–U05; tách khỏi 23 bug GUI |
| Video demo skill | Video sinh viên cung cấp: https://youtu.be/VGVm_V7L_ks ; 10:38; đã kiểm tra phát không đăng nhập |

Kết quả GUI do Codex thực thi tự động. Kết quả usability lấy từ hồ sơ sinh viên cung cấp và xác nhận trong chat ngày 15/11/2026; phép tính được đối chiếu độc lập với CSV/JSON. Không suy ra SUS từ kiểm thử tự động. Không có video phiên; §14 yêu cầu kèm bản quay khi có, nên giữ rõ giới hạn này.


## 9. Phản biện và bổ sung tiếp cận

### Bổ sung đã thực thi

Ba tiêu chí G49–G51 do Codex đề xuất/thực thi theo yêu cầu sinh viên. Giữ nguyên 48 tiêu chí đầu tại items.json; phần bổ sung ở additions.json. Tổng 51 tiêu chí, 153 kết quả trên ba browser: bộ gốc 144 kết quả (56 Passed, 88 Failed), bổ sung 9 Failed. Tổng 56 Passed, 97 Failed; 33 tiêu chí fail ít nhất một môi trường, 25 nhóm bug GUI. Năm finding usability tách riêng, tổng 30 GitHub Issues khi đã đăng hai bug mới.

## Vì sao bổ sung

- G49: bộ đầu đo alt và liên kết nhãn nhưng bỏ qua ngôn ngữ tài liệu. Prompt tập trung thành phần nhìn thấy; metadata phục vụ công nghệ hỗ trợ không nổi bật trong ảnh.
- G50: bộ đầu kiểm ký hiệu tiền và bố cục nhưng chưa tính tương phản. Nhận xét màu đẹp/nhìn rõ bằng mắt của AI không thay được phép đo định lượng.
- G51: G11 kiểm quy chuẩn màu xanh dương, G41 kiểm phản hồi thêm thành công. Cả hai không trả lời chữ nút có đủ tương phản hay không; việc thêm kiểm tra này tránh đánh đồng màu đúng chuẩn với dễ đọc.

## Kết quả thực thi

| ID | IA | Màn hình | Chrome | Firefox | Safari | Quan sát |
|---|---|---|---|---|---|---|
| G49 | IA-01 | Home | Failed | Failed | Failed | lang=en; nội dung tiếng Việt |
| G50 | IA-01 | Home | Failed | Failed | Failed | 3.7631:1 < 4.5:1; 16px, weight 700 |
| G51 | IA-02 | Detail | Failed | Failed | Failed | 3.2957:1 < 4.5:1; 16px, weight 400 |

## Bằng chứng và giới hạn

Đã mở các case qua native CUA trên ba browser; JSON gửi về collector localhost, ảnh chụp cửa sổ thật. Trang đo tự kiểm tra công thức trước khi gửi; collector chỉ lưu bản ghi thực tế. Không bật lại Safari Remote Automation. Không suy ra ngôn ngữ đọc thực tế của screen reader. Ảnh chụp có email/tên/MSSV và URL localhost; metadata môi trường đầy đủ ở JSON. Các tiêu chí là WCAG heuristic ngoài cam kết FR của SUT.

- [B24: Trang tiếng Việt khai báo ngôn ngữ mặc định en](../bug-reports/supplement/B24.md); Issue: https://github.com/NgBaoAnn/hw03-gui-usability/issues/29.
- [B25: Chữ giá và chữ nút thêm giỏ thiếu tương phản](../bug-reports/supplement/B25.md); Issue: https://github.com/NgBaoAnn/hw03-gui-usability/issues/30.

Nguồn: [WCAG 3.1.1](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html), [WCAG 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).


### Phản biện AI (bản AI soạn)

Trạng thái: bản AI soạn theo yêu cầu sinh viên, có bằng chứng đối chiếu; chưa xác nhận là sinh viên tự phản biện.

AI hỗ trợ tổ chức checklist và chạy kiểm thử, nhưng kế hoạch đầu đã dựa quá nhiều vào khuôn mẫu thương mại điện tử. Bộ lọc, sắp xếp và tai nghe dưới 500.000 đồng được đề xuất trước khi đối chiếu SUT. Các giả định ấy không phù hợp giao diện và dữ liệu mẫu. Việc sửa phạm vi cần bắt đầu từ nguồn yêu cầu và quan sát ứng dụng.

Bộ checklist ban đầu có nhãn truy cập và thao tác bàn phím nhưng thiếu ngôn ngữ tài liệu, phép đo tương phản. Đây là giới hạn của cách chia nhỏ tiêu chí: kiểm tra màu nút theo quy chuẩn không đồng nghĩa chữ trên nút dễ đọc. Ba mục G49–G51 được AI bổ sung theo yêu cầu sinh viên và chạy trên Chrome, Firefox, Safari thật. Trang khai báo tiếng Anh dù nội dung tiếng Việt; chữ giá đạt 3,76:1, chữ nút đạt 3,30:1, thấp hơn ngưỡng 4,5:1 áp dụng cho cỡ chữ đã đo. Kết quả cho thấy quan sát bằng mắt cần được bổ sung bằng phép đo có nguồn.

Công cụ cũng có thể gây kết luận sai. Trước đây, đọc kết quả trước khi React chuyển trang làm một số kiểm tra số lượng bị đánh dấu sai. Điều kiện chờ và kiểm chứng trạng thái giỏ đã được bổ sung. Nguyên tắc hợp tác là giữ dấu vết nguồn, phân biệt heuristic với yêu cầu sản phẩm, và giới hạn kết luận theo bằng chứng. AI không được biến ảnh tái hiện thành phiên người dùng, hoặc gán phần mình viết thành đóng góp tự phát hiện của sinh viên.


## 10. Đóng góp cá nhân

### Nguyễn Bảo An – 23120207

MSSV: **23120207**. Email: **23120207@student.hcmus.edu.vn**. Bài làm cá nhân. Cập nhật ngày 16/11/2026.

## Vai trò của sinh viên

Nguyễn Bảo An lựa chọn và xác nhận phạm vi bài, cung cấp thông tin và dữ liệu nghiên cứu, điều phối việc sử dụng AI, quyết định cách công bố hồ sơ và tự đánh giá bài làm. Phần điều phối các phiên usability được ghi nhận theo xác nhận trực tiếp của sinh viên trong cuộc trò chuyện. Các đóng góp dưới đây được đối chiếu với lời nhắn đã lưu; không suy ra từ tên người nộp hoặc số lượng file.

| Công việc | Đóng góp của Nguyễn Bảo An | Bằng chứng và phần AI hỗ trợ |
|---|---|---|
| Chọn phạm vi | Chọn G2 trong quá trình lập kế hoạch; xác nhận làm cá nhân và phạm vi G2 còn đúng. | Hội thoại lập kế hoạch trong AI_AUDIT_RECOVERED.md và xác nhận trong AI_TRANSCRIPT.md. AI thiết kế chi tiết checklist và điều chỉnh giả định theo SUT. |
| Xác nhận thông tin bài nộp | Xác nhận tên, MSSV và email sinh viên; yêu cầu đồng bộ hồ sơ Task 2 về Nguyễn Bảo An – 23120207. | Lời nhắn xác nhận email và yêu cầu sửa thông tin. AI cập nhật biểu mẫu, overlay, báo cáo và file nộp. |
| Điều phối công việc với AI | Yêu cầu thực hiện các phần của homework, rà phần còn thiếu, tích hợp Task 2 và tiếp tục phản biện/bổ sung checklist. | Chuỗi yêu cầu và đầu ra được lưu trong AI_TRANSCRIPT.md. AI đề xuất tiêu chí, viết bộ chạy và thực thi kiểm tra; không gán việc đó thành thao tác thủ công của sinh viên. |
| Hỗ trợ môi trường Safari | Đồng ý dùng Safari WebDriver và xác nhận đã trực tiếp xác thực/bật quyền trên máy khi hệ thống yêu cầu. | Hai lời nhắn đồng ý và xác nhận đã bật quyền. AI chạy bộ kiểm tra, xử lý lỗi harness và khôi phục thiết lập sau lượt chạy. |
| Điều phối nghiên cứu usability | Sinh viên xác nhận đã tự điều phối một pilot và bảy phiên thật; cung cấp folder task2_usability chứa biên bản, câu trả lời SUS và dữ liệu tổng hợp. | Câu trả lời: “Có, đây là các phiên thật tôi đã điều phối”. Nguồn và SHA-256 được lưu tại usability/provenance.json. AI đối chiếu CSV/JSON, tính lại điểm và tổng hợp; không xác minh độc lập danh tính hoặc việc diễn ra phiên. |
| Quyết định phạm vi Task 2 | Yêu cầu giữ nội dung và số liệu hồ sơ đã cung cấp khi sửa thông tin sinh viên; do đó Task 2 giữ luồng quản lý đơn hàng, Task 1 giữ G2. | Lời nhắn yêu cầu “còn lại giống với bài làm tôi gửi vào”. AI làm rõ hai phạm vi trong báo cáo, giữ dữ liệu gốc và liên kết bằng chứng tái hiện riêng. |
| Yêu cầu cải thiện phản biện | Chủ động yêu cầu AI viết phần rà soát, phản biện và bổ sung checklist trước khi quay demo. | Lời nhắn yêu cầu và các file AI_REVIEW.md, ADDITIONS.md, AI_CRITIQUE.md. G49–G51 do AI đề xuất/thực thi; đây là đóng góp điều phối của sinh viên, chưa phải xác nhận sinh viên tự phát hiện ba tiêu chí đó. |
| Quyết định công bố | Cho phép công khai repo bài làm để người chấm xem Issues và ảnh. | Lời nhắn “Cho phép công khai repo bài làm”. AI thực hiện công bố và giữ danh sách tên/liên hệ người tham gia ngoài repo public; không gán thao tác che dữ liệu cho sinh viên. |
| Tự đánh giá | Chọn tự chấm toàn bộ điểm: Task 1 = 30, Task 2 = 40, Task 3 = 20, skill/demo = 10; tổng 100/100. | Lời nhắn “cho full điểm”. AI điền bảng theo lựa chọn này. Đây là điểm tự đánh giá, không phải điểm giảng viên hoặc chứng nhận bài đã hoàn tất. |
| Video demo | Quyết định tự quay video demo và nhắc lại lựa chọn này khi giao AI hoàn thiện phần còn lại. | Lời nhắn “video tôi tự quay” và “tôi tự làm video demo”. Sinh viên đã cung cấp https://youtu.be/VGVm_V7L_ks ngày 16/11/2026; đã thử phát không đăng nhập. Prompt và kết quả đúng chat demo trong AI_DEMO_TRANSCRIPT.md, skill và bằng chứng thực tế đã kèm hồ sơ. |

## Sản phẩm do AI hỗ trợ thực hiện

AI thiết kế 48 tiêu chí đầu và bổ sung G49–G51, thực thi kiểm tra trên Chrome/Firefox/Safari, chụp bằng chứng, soạn bug và tạo Issues, đối chiếu SUS, chuẩn hóa hồ sơ, xây skill, soạn phản biện, cập nhật báo cáo/PDF/Excel, commit và đóng ZIP. Kết quả hiện có: 51 tiêu chí, 153 kết quả kiểm tra, 25 nhóm bug GUI và năm finding usability. Video do sinh viên cung cấp có luồng demo thực tế được đối chiếu với chat và ảnh; các thao tác browser trong video do agent thực hiện theo prompt sinh viên.

Người nộp là sinh viên; tác giả đề xuất/thực thi từng phần vẫn được khai báo đúng trong audit. Không quy đổi việc giao AI thực hiện thành bằng chứng sinh viên đã tự thao tác các bước kỹ thuật.

## Trạng thái cần hoàn tất

- Chưa có xác nhận thực tế rằng sinh viên đã tự rà soát kết quả hoặc tự phát hiện/bổ sung một tiêu chí mà AI bỏ sót. Phiếu HUMAN_REVIEW.md giữ nguyên trạng thái chờ; bản ghi đóng góp này không ký thay sinh viên.
- Video đã cung cấp và phát được: https://youtu.be/VGVm_V7L_ks .
- Trạng thái Moodle sẽ được kiểm tra riêng sau khi người dùng duyệt preview nộp. Không có video phiên usability trong dữ liệu được cung cấp; giới hạn này đã được nêu trong báo cáo.

Các nguồn tham chiếu cùng hồ sơ: [hội thoại hiện tại](AI_TRANSCRIPT.md), [hội thoại lập kế hoạch](AI_AUDIT_RECOVERED.md), [nguồn Task 2](../usability/provenance.json), [AI rà soát](../checklists/AI_REVIEW.md), [checklist bổ sung](../checklists/ADDITIONS.md), [phiếu sinh viên](../checklists/HUMAN_REVIEW.md).


## 11. Kiểm thử minh họa và phát hiện ngoài G2


Demo https://youtu.be/VGVm_V7L_ks thực hiện một luồng từ tìm kiếm đến tạo đơn #9. Kết quả/bằng chứng gốc tại `evidence/demo/run-2026-11-16-eshop-flow/README.md`, prompt/output tại AI_DEMO_TRANSCRIPT.md. Không cộng lượt này vào 153 kết quả cross-browser; bộ G2 vẫn 51 tiêu chí, 25 nhóm bug.

| Phát hiện mới | Nguồn | Mức độ | Báo cáo |
|---|---|---|---|
| D01 Tổng checkout chỉnh sửa trực tiếp | FR-08 | Major | bug-reports/demo/D01.md |
| D02 Giỏ không xóa sau checkout thành công | FR-08 | Major | bug-reports/demo/D02.md |
| D03 Nhãn form đăng nhập trộn tiếng Anh | FR-21 | Minor | bug-reports/demo/D03.md |

Các quan sát khác liên kết lại nhóm đã có: giỏ thiếu h1 → B02; breadcrumb → B12; thiếu badge/toast → B17; click đầu ở Detail chưa thêm → B18; nhãn Tổng tạm tính → B21; màu nút tích cực → B05 (demo quan sát thêm checkout); tiêu đề login Đăng Ký → U02. Không tạo Issue trùng cho các kết luận này. Báo cáo demo gốc dẫn G41 trong hàng badge/toast chưa chính xác; ánh xạ kết quả chính thức dùng B17 (G39/G42), G41 của bộ chính giữ kết quả ban đầu.

Demo chỉ chứng minh tổng checkout có thể chỉnh trên UI, chưa chứng minh backend chấp nhận giá bị sửa. Đơn thực tế dùng tổng gốc 6.000.000 ₫. D02 hậu kiểm giỏ trong cùng phiên, không suy rộng nghiên cứu người dùng. IAB không có thông tin version engine nên không thay thế một trong ba môi trường Task 3. Ba phát hiện mới có bug Markdown, ảnh và Issues riêng; tổng hồ sơ gồm 25 nhóm G2, 5 finding usability và 3 phát hiện demo.

GitHub Issues: D01: https://github.com/NgBaoAnn/hw03-gui-usability/issues/31, D02: https://github.com/NgBaoAnn/hw03-gui-usability/issues/32, D03: https://github.com/NgBaoAnn/hw03-gui-usability/issues/33.
