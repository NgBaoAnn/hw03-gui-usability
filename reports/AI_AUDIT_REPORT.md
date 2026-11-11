# AI Audit Report - HW03 G2

Sinh viên: Nguyễn Bảo An - 23120207. Trạng thái: bản ghi việc đã thực hiện, chờ sinh viên kiểm tra và bổ sung lịch sử AI trước phiên hiện tại.

## Khai báo

“I use AI tools for the following tasks,” gồm: đọc đề và chính sách; kiểm tra thông tin Moodle; đối chiếu phạm vi với mã nguồn/dữ liệu SUT; thiết kế 48 mục checklist; viết và chạy bộ kiểm thử trình duyệt; chụp bằng chứng thật; nhóm và viết báo cáo lỗi; chuẩn bị protocol, SUS và biểu mẫu; viết trình tính SUS; xây dựng agent skill; soạn báo cáo và xuất Excel/PDF/bản zip nháp.

Công cụ AI: OpenAI Codex desktop, agent dựa trên GPT-6 theo thông tin phiên. Phiên hiện tại bắt đầu ngày 11/11/2026, múi giờ Asia/Ho_Chi_Minh. Thời điểm từng prompt/output lấy từ timestamp transcript, không tự ước lượng.

## Prompt, thời điểm và đầu ra

`AI_TRANSCRIPT.md` chứa nguyên văn prompt và câu trả lời hiển thị của chat hiện tại, có ngày giờ từng tin nhắn. Các câu hỏi và câu trả lời về phạm vi G2, email sinh viên, dữ liệu người tham gia cũng được giữ để truy vết quyết định. File này không xuất suy luận nội bộ hay thông tin xác thực.

Đầu ra có thể tái kiểm tra:

| Hoạt động AI | Đầu ra thực tế | Kiểm chứng / trạng thái |
|---|---|---|
| Khám phá yêu cầu | MAIN_REPORT.md §1 | Đối chiếu PDF gốc, policies, assignment/status/section và thread GUI/Usability Moodle |
| Thiết kế checklist | checklists/items.json; gui_checklist_g2.md/.csv/.xlsx | 48 ID duy nhất, 12 mục/IA; chưa có mục sinh viên tự bổ sung |
| Kiểm thử GUI | scripts/run_gui.cjs; evidence/runs/*.json | Chạy Chrome và Firefox thật bằng Playwright; kết quả raw, version, timestamp và SUT commit |
| Chụp ảnh | evidence/gui/ | Browser screenshot thật, có chú thích định danh sau phép đo; không dùng ImageGen |
| Kiểm tra Safari | evidence/gui/safari/ | Native Safari qua CUA, mới kiểm tra nhanh; không gán là lượt đủ 48 mục |
| Báo cáo bug | bug-reports/BUG_REPORTS.md và B01–B23.md | Gộp 59 Failed thành 23 nhóm; heuristic được ghi rõ; Issue URL trong issues.json |
| Chuẩn bị usability | usability/PROTOCOL.md, SUS_QUESTIONNAIRE.md, CSV, sessions/ | Mẫu trống; 0 phiên, 0 người; không có dữ liệu tự tạo trong báo cáo |
| Tính SUS | scripts/calculate_sus.py; sheet SUS | Self-check 0/50/100, từ chối thiếu/sai thang; dữ liệu thử đã xóa trước export |
| Xây skill | skills/gui-usability-evaluator/SKILL.md | Kiểm tra cấu trúc skill thành công; demo chưa quay |
| Đóng gói | scripts/validate_submission.py và package_draft.py | Bản nháp có ghi rõ thiếu sót; chưa nộp Moodle |

## Rà soát và các sửa đổi đã xảy ra

Kế hoạch cũ giả định bộ lọc, sắp xếp, đánh giá sản phẩm và một tai nghe dưới 500.000 ₫; nguồn và dữ liệu chạy không hỗ trợ những giả định này. Codex đã thu hẹp kịch bản theo chức năng thực, ngân sách 7 triệu. Đây là sửa đổi của AI, chưa được ghi là đóng góp phản biện của sinh viên.

Bộ chạy thử ban đầu chưa chờ React chuyển trang xong, dẫn đến một số kết quả sai. Codex thêm điều kiện chờ route và heading giỏ, chạy lại cả Chrome/Firefox. Thống kê cuối lấy từ JSON cuối, không cộng dồn lượt thử. Không sửa logic SUT để che lỗi.

Không dùng danh sách lớp Moodle làm người tham gia. Không tạo điểm SUS, phát ngôn, thời gian, tên/liên hệ hay kết quả phiên để lấp dữ liệu thiếu. Danh sách P1–P7 chỉ là mã trên biểu mẫu trống.

## Phần lịch sử chưa đầy đủ

Các file kế hoạch ngày 03/11 đã có từ trước phiên này. Git có commit thực của chúng nhưng chưa có prompt/output nguyên gốc tương ứng trong dữ liệu được xuất hiện tại. Sinh viên cần bổ sung bản xuất chat cũ; không tuyên bố audit bao phủ hoàn toàn mọi lần dùng AI trước đây. Các phản hồi sau thời điểm xuất transcript cần xuất lại trước khi nộp cuối.

## Sinh viên xác nhận

Chưa xác nhận. Sinh viên cần đọc kết quả, chỉnh sửa AI Critique bằng trải nghiệm thật, bổ sung checklist tự phát hiện, kiểm tra ảnh/lỗi và tự chấm điểm. Không tự ký thay sinh viên.
