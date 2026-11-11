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
| Kiểm thử GUI | scripts/run_gui.cjs; scripts/run_safari.py; evidence/runs/*.json | 48 mục trên mỗi browser: Chrome/Firefox bằng Playwright, Safari thật bằng Apple WebDriver; raw results, version, timestamp và SUT commit |
| Chụp ảnh | evidence/gui/ | Browser screenshot thật, có chú thích định danh sau phép đo; không dùng ImageGen |
| Định danh trong form thật | evidence/identity/; cross-platform/IDENTITY.md | Điền tên/MSSV/email vào form đăng ký SUT trên ba browser, để trống mật khẩu, không gửi form và không tạo tài khoản |
| Kiểm tra Safari | evidence/runs/safari.json; evidence/gui/safari/ | Safari 26.2 thật: 19 Passed, 29 Failed, 0 Blocked; giữ thêm 9 quan sát CUA cũ để đối chiếu, không cộng lặp |
| Báo cáo bug | bug-reports/BUG_REPORTS.md và B01–B23.md | Gộp 88 Failed trên ba browser thành 23 nhóm; heuristic được ghi rõ; Issue URL trong issues.json |
| Chuẩn bị usability | usability/PROTOCOL.md, SUS_QUESTIONNAIRE.md, CSV, sessions/ | Mẫu trống; 0 phiên, 0 người; không có dữ liệu tự tạo trong báo cáo |
| Tính SUS | scripts/calculate_sus.py; sheet SUS | Self-check 0/50/100, từ chối thiếu/sai thang; dữ liệu thử đã xóa trước export |
| Xây skill | skills/gui-usability-evaluator/SKILL.md | Kiểm tra cấu trúc skill thành công; đã có demo MP4, chờ URL YouTube |
| Ghi demo theo skill | skills/gui-usability-evaluator/video/gui-g2-demo.mp4; video/recording-log.json | 112,4 giây browser thật, có phụ đề; các quan sát được assert trong quá trình ghi; chờ xem lại và YouTube URL |
| Khôi phục audit lập kế hoạch | reports/AI_AUDIT_RECOVERED.md; reports/legacy/ | 14 lời nhắn thật ngày 03/11 của OpenCode gắn đúng thư mục; ba đầu ra kế hoạch nguyên gốc kèm hash |
| Đóng gói | scripts/validate_submission.py và package_draft.py | Bản nháp có ghi rõ thiếu sót; chưa nộp Moodle |

## Rà soát và các sửa đổi đã xảy ra

Kế hoạch cũ giả định bộ lọc, sắp xếp, đánh giá sản phẩm và một tai nghe dưới 500.000 ₫; nguồn và dữ liệu chạy không hỗ trợ những giả định này. Codex đã thu hẹp kịch bản theo chức năng thực, ngân sách 7 triệu. Đây là sửa đổi của AI, chưa được ghi là đóng góp phản biện của sinh viên.

Bộ chạy thử ban đầu chưa chờ React chuyển trang xong, dẫn đến một số kết quả sai. Codex thêm điều kiện chờ route và heading giỏ, chạy lại cả Chrome/Firefox. Thống kê cuối lấy từ JSON cuối, không cộng dồn lượt thử. Không sửa logic SUT để che lỗi.

Sau khi sinh viên cho phép Safari WebDriver, sinh viên tự xác thực Touch ID/mật khẩu máy để bật quyền. Không cung cấp mật khẩu cho AI. Safari được chạy với Apple safaridriver. Iframe cùng origin đặt viewport CSS chính xác; riêng Browser Back dùng SUT ở top-level và lệnh Back chuẩn vì lịch sử của iframe không tương đương cửa sổ chính. Mạng chậm/HTTP 503 dùng XHR redirect tới fixture localhost có ghi rõ, không sửa logic SUT.

Sau khi hoàn tất, đã tắt lại Allow remote automation và Show features for web developers về trạng thái ban đầu. Không thay đổi thiết lập bàn phím hoặc các quyền JavaScript/cross-origin khác.

SafariDriver đôi khi blur input sau khi nhập mà chưa phát click. Codex ghi số DOM click, chỉ lặp lệnh WebDriver nếu chưa có click được giao, rồi chạy lại các mục bị ảnh hưởng. Lỗi nút bỏ qua click đầu vẫn được giữ vì click thực đã tới ứng dụng. Những mục từng Blocked không được coi là bug; JSON cuối có đủ 48 kết quả Passed/Failed. Kết quả tổng: 144 lượt, 56 Passed, 88 Failed, 23 nhóm bug. Sinh viên vẫn chưa rà soát hoặc thu dữ liệu usability thật.

Không dùng danh sách lớp Moodle làm người tham gia. Không tạo điểm SUS, phát ngôn, thời gian, tên/liên hệ hay kết quả phiên để lấp dữ liệu thiếu. Danh sách P1–P7 chỉ là mã trên biểu mẫu trống.

## Lịch sử lập kế hoạch đã khôi phục

Đã khôi phục session OpenCode “Homework requirements overview” gắn chính xác thư mục HW03, từ 15:28 đến 16:08 ngày 03/11/2026. File `AI_AUDIT_RECOVERED.md` chứa 14 lời nhắn user/assistant hiển thị, timestamp thật và cấu hình model từ metadata. Ba bản kế hoạch gốc được giữ trong `reports/legacy/` cùng SHA-256, bao gồm các giả định AI đã đề xuất sai. Không truy xuất các phiên đăng nhập hoặc mạng không liên quan.

Đầu ra tool viết file trong session cũ được đối chiếu với ba file và Git commits thực. Chỉ xuất phần văn bản hiển thị; không đưa suy luận nội bộ hoặc thông tin xác thực vào bài. Bản PDF audit có phụ lục hội thoại cũ và mới. Sinh viên cần kiểm tra và bổ sung nếu đã dùng AI ở những nơi khác không nằm trong hai nguồn đã khôi phục. Các tin nhắn sau thời điểm xuất transcript sẽ được xuất lại trước lần nộp cuối.

## Sinh viên xác nhận

Chưa xác nhận. Sinh viên cần đọc kết quả, chỉnh sửa AI Critique bằng trải nghiệm thật, bổ sung checklist tự phát hiện, kiểm tra ảnh/lỗi và tự chấm điểm. Không tự ký thay sinh viên.
