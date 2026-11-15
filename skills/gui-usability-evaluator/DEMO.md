# Video demo skill đã cung cấp

Sinh viên Nguyễn Bảo An – 23120207 cung cấp video: https://youtu.be/VGVm_V7L_ks . Tiêu đề: HW03 – 23120207 – Demo GUI Testing Skill - Nguyễn Bảo An -. Thời lượng giao diện YouTube 10:38 (metadata làm tròn 639 giây). Ngày 16/11/2026 đã mở và phát được khi không đăng nhập; dữ liệu kiểm tra đã lọc tại `evidence/demo/video-verification.json`.

## Skill và prompt thực tế

Bản skill dùng trong video được sao chép nguyên trạng từ SUT vào [demo-version/SKILL.md](demo-version/SKILL.md), có đủ checklist 51 mục và SUS scorer. SHA-256 được lưu trong file kiểm tra video. Để dùng lại, chép cả thư mục demo-version thành `.agents/skills/gui-usability-evaluator/` ở SUT khác, cung cấp đặc tả và URL thực tế. Bản skill homework gốc ở thư mục cha hỗ trợ các bộ chạy đầy đủ đã dùng cho Task 1/3.

Prompt sinh viên dùng lúc 01:03:18 ngày 16/11/2026:

> Dùng skill gui-usability-evaluator để kiểm thử một luồng hoàn chỉnh trên EShop tại http://localhost:5173. Thao tác trực tiếp trên trình duyệt hiển thị, giải thích ngắn quá trình kiểm thử và trình bày kết quả cùng bằng chứng

## Nội dung và bằng chứng

Lượt chạy bắt đầu khoảng 01:04, kết thúc khoảng 01:10: đọc skill/đặc tả → tìm AirPods Pro 2 → xem chi tiết → thử thêm vào giỏ → đăng nhập tài khoản demo → thêm từ thẻ → checkout → kiểm tra đơn #9 và giỏ còn hàng. Bản ghi gốc và sáu ảnh nằm tại `evidence/demo/run-2026-11-16-eshop-flow/`; đây là một lượt agent trên browser IAB hiển thị. Transcript prompt/output có timestamp: `reports/AI_DEMO_TRANSCRIPT.md`.

Bằng chứng bổ sung xác nhận ba phát hiện ngoài bộ G2: D01 tổng checkout chỉnh trực tiếp, D02 giỏ không xóa sau thành công, D03 nhãn đăng nhập dùng tiếng Anh. Xem `reports/DEMO_FINDINGS.md`, bug Markdown và GitHub Issues. Các lỗi thuộc G2 đã có báo cáo/Issue được liên kết lại, tránh đếm trùng.

## Giới hạn

Video là demo dùng skill trên luồng đầy đủ, không phải lượt thực thi lại toàn bộ 51 mục/ba browser hay phiên nghiên cứu người dùng. Không cộng vào 156 kết quả của Task 1/3 và không dùng thay pilot/SUS. Engine/version của IAB không được công cụ demo hiển thị nên không gán thành Chrome, Firefox hoặc Safari. Sáu ảnh demo gốc giữ nguyên; định danh ghi ở báo cáo gốc, không phải overlay có sẵn trên các ảnh này. Bộ ảnh Failed dùng cho Task 3 có overlay và bộ định danh riêng.

Đã đối chiếu các khung hình mẫu của bản quay cục bộ có thời lượng 638,538 giây và hồ sơ của đúng chat demo. Không đánh giá độc lập toàn bộ lời thuyết minh âm thanh. MP4 tham khảo cũ do AI ghi đã được người dùng loại khỏi hồ sơ; link trên là video sinh viên chọn để nộp.
