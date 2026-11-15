# Rà soát checklist và khai báo nguồn đóng góp

Sinh viên: Nguyễn Bảo An — 23120207 — 23120207@student.hcmus.edu.vn.

## 1. Nguồn và giới hạn lời khai

Người dùng bổ sung vào workspace một bản khai nói đã đọc/đối chiếu G49–G51 và AI Critique. Hồ sơ ghi nhận việc tự rà soát **theo bản khai được cung cấp**, không xác minh độc lập thao tác đọc/tính toán. Không tạo chữ ký, giờ xác nhận hoặc lời xác nhận qua chat thay sinh viên.

Bản khai trước gán G52 là sinh viên tự phát hiện, nhưng AI_TRANSCRIPT.md mục 86 ghi “Mình đề xuất thêm G52”. Theo yêu cầu xử lý mâu thuẫn ngày 16/11/2026, bản hiện tại sửa nguồn G52 thành **AI đề xuất và thực thi theo yêu cầu sinh viên**. Đề xuất của AI không trở thành phát hiện riêng của sinh viên khi sinh viên giao AI làm hoặc duyệt kết quả.

SHA-256 của bản khai được cung cấp trước đính chính: 183e4eff1511adeb16e50a5be1000cd51d45a0044c07716609ee908f33033bcc. Bản nguồn được giữ riêng, không đưa lên GitHub hoặc ZIP để tránh tiếp tục dùng lời xác nhận đã đính chính làm bằng chứng hoàn tất.

## 2. Nội dung sinh viên đã khai báo rà soát

| ID | Quyết định trong bản khai được cung cấp | Căn cứ được khai báo | Đối chiếu của AI |
|---|---|---|---|
| G49 | Giữ nguyên | lang=en trên nội dung tiếng Việt; chỉ kết luận thuộc tính, chưa kết luận screen reader | Khớp JSON ba browser, B24 và Issue #29 |
| G50 | Giữ Failed và ngưỡng 4.5:1 | Tỷ lệ 3.763128 với chữ 16px/700 | Khớp bằng chứng B25; không thuộc chữ lớn |
| G51 | Giữ Failed, ghi heuristic tiếp cận | Tỷ lệ 3.295734 với chữ 16px/400 | Khớp bằng chứng B25 và Issue #30 |

Đây là quyết định theo hồ sơ người dùng cung cấp; việc AI tính lại không chứng minh sinh viên đã tự tính. Không dùng lời khai trên để gán quyền tác giả G49–G52 cho sinh viên.

## 3. G52: bổ sung của AI theo yêu cầu sinh viên

- IA-02 / Product Detail, URL http://localhost:5173/product/1.
- Ở viewport 390×844 CSS px, đo getBoundingClientRect của ô Số lượng và nút Thêm vào giỏ hàng; cả hai mục tiêu tối thiểu 24×24 CSS px.
- Nguồn: WCAG 2.2 SC 2.5.8, heuristic ngoài FR. Chỉ kết luận hai mục tiêu được đo; không chứng nhận toàn trang đạt WCAG. Các trường hợp mục tiêu nhỏ còn cần xét ngoại lệ của chuẩn.
- Vì sao bộ AI trước bỏ sót: G08/G09 đo tràn ngang, G10 đo vị trí nút; chưa có phép đo diện tích bấm. Đây là phân tích của AI, không gán là nhận định tự phát hiện của sinh viên.

| Browser | Viewport | Ô số lượng | Nút thêm giỏ | Kết quả | Bằng chứng |
|---|---|---|---|---|---|
| Chrome 157 | 390×844 | 80×42 | 185.9×48 | Passed | evidence/runs/chrome.json; evidence/gui/chrome/G52.png |
| Firefox 153 | 390×844 | 80×42 | 186.8×48 | Passed | evidence/runs/firefox.json; evidence/gui/firefox/G52.png |
| Safari 26.2 | 390×844, đã đo lại | 80×42 | 185.9×48 | Passed | evidence/accessibility/safari/G52.json và G52.png; evidence/runs/safari.json |

Safari được đo lại bằng native CUA trên trình duyệt thật, iframe cùng origin chỉ đọc DOM/CSS. Trang đo đặt cả chiều rộng và chiều cao cố định, chờ innerWidth=390 và innerHeight=844 trước khi đo. Không bật Remote Automation hoặc sửa logic SUT. Bản 390×839 cũ được lưu G52-390x839-original.json để truy vết, không cộng thêm lượt vào thống kê.

## 4. Trạng thái tuân thủ

- Hồ sơ có 52 tiêu chí, 156 kết quả: 59 Passed, 97 Failed; 25 nhóm bug GUI. G52 Passed nên không tạo bug hoặc Issue mới.
- human_review_complete=true ghi nhận bản khai người dùng cung cấp; nguồn khai báo và giới hạn ở mục 1.
- human_added_check_ids=[]: chưa có tiêu chí tự phát hiện riêng được chứng minh. ai_added_check_ids gồm G49–G52.
- Phần yêu cầu sinh viên tự bổ sung checklist chưa được coi là hoàn tất. Mọi điểm tự chấm 100/100 vẫn là lựa chọn sinh viên, không phải điểm chính thức.

Nguồn: [nhật ký AI](../reports/AI_TRANSCRIPT.md), [AI rà soát](AI_REVIEW.md), [bổ sung G49–G51](ADDITIONS.md), [AI Critique](../reports/AI_CRITIQUE.md).
