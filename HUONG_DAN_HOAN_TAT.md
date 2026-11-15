# Chốt bài HW03 của Nguyễn Bảo An – 23120207

Bộ hồ sơ đã tích hợp Task 2 bạn cung cấp và xác nhận là các phiên thật do bạn điều phối. Task 1/3 giữ G2; Task 2 giữ luồng quản lý đơn hàng. Không cần nhập lại điểm SUS hoặc viết lại báo cáo.

## Phần đã hoàn thành

- 51 mục GUI × Chrome/Firefox/Safari: 153 kết quả, 56 Passed, 97 Failed; 25 nhóm bug GUI có ảnh và Issues (48 mục gốc + 3 bổ sung).
- Task 2: một pilot và bảy biên bản, SUS từng người/trung bình, thời gian, tỷ lệ hoàn thành, bốn chủ đề probe và năm phát hiện. SUS 58,93/100; hoàn thành 6/7.
- Năm ảnh agent tái hiện U01–U05 trên SUT, báo cáo và Issues riêng. Đây là ảnh tái hiện, không phải ảnh/video phiên người tham gia.
- Tên/MSSV/email đã đồng bộ; PDF, Excel, audit AI, skill, nhật ký Git và ZIP được cập nhật.
- Repo public dùng mã người tham gia. Danh sách tên/liên hệ đã che và bộ Task 2 đầy đủ chỉ đưa vào ZIP nộp.

## 1. Quay demo skill của bạn

Dùng `skills/gui-usability-evaluator/DEMO.md`. Bản MP4 có sẵn do Codex ghi chỉ dùng tham khảo.

1. Mở SUT http://localhost:5173 và thư mục bài làm. Trên Mac dùng Shift–Command–5 để quay vùng cần thiết. Hiện họ tên, MSSV và email; tránh quay thông báo hoặc dữ liệu riêng.
2. Giới thiệu Nguyễn Bảo An, 23120207 và phạm vi G2. Mở `skills/gui-usability-evaluator/SKILL.md`.
3. Yêu cầu agent dùng skill đọc đặc tả rồi kiểm tra luồng thật: tìm tai nghe → xem chi tiết → thêm giỏ → kiểm tra giỏ. Đừng chỉ chiếu ảnh kết quả đã chuẩn bị.
4. Cho thấy quan sát của lần thêm đầu tiên, bước tái hiện và kết quả. Mở checklist G40, ảnh, B18 và GitHub Issue tương ứng để giải thích truy vết.
5. Nêu một giới hạn và cách dùng lại skill trên màn hình khác. Có thể quay khoảng 3–5 phút; đây là gợi ý, đề không ấn định thời lượng.
6. Xem lại video, tải lên YouTube Unlisted, thử mở link ẩn danh rồi gửi URL. Không cần gửi mật khẩu tài khoản.

## 2. Giới hạn bằng chứng Task 2 đã ghi nhận

Hồ sơ nguồn ghi tất cả người tham gia từ chối ghi hình. §6 hướng dẫn quay màn hình; §14 của đề tiếng Anh quy định kèm “screen recordings where available” (bản quay khi có). Bản nộp đã kèm ghi chú có cấu trúc, SUS, probe và ghi rõ không có video phiên. Không cần tạo video thay cho phiên cũ. Nếu bạn có bản quay thật được đồng ý chia sẻ, báo đường dẫn để bổ sung; không quay dựng rồi gán thành bản ghi phiên trước.

Video demo skill ở bước 1 là phần riêng và vẫn cần link YouTube. Các phiên được nhập cùng lúc nên thiếu commit tại thời điểm từng phiên; báo cáo đã nêu giới hạn này, không tạo lịch sử lùi ngày.

## 3. Rà soát và tự bổ sung checklist

Codex đã viết phản biện 278 từ, lượt AI rà soát và bổ sung G49–G51, có chín phép kiểm thật/ảnh trên ba browser. Đọc `checklists/ADDITIONS.md`, `checklists/AI_REVIEW.md` và `reports/AI_CRITIQUE.md` theo yêu cầu của bạn. Đọc bản này cùng `reports/MAIN_REPORT.pdf`, `checklists/gui_checklist_g2.xlsx`, ảnh và các bug. Dùng `checklists/HUMAN_REVIEW.md` ghi mục chấp nhận/sửa/loại và lý do. Đề yêu cầu bạn tự phát hiện và bổ sung mục AI bỏ sót; Codex không thể tự viết rồi gán là đóng góp của bạn.

Phần soạn phản biện và tiêu chí bổ sung đã được AI chuẩn bị, không cần viết lại từ đầu. Nếu bạn tự phát hiện thêm mục mới, gửi nội dung, lý do AI bỏ sót và quan sát của bạn. Codex sẽ kiểm tra trùng lặp, bổ sung ID, chạy trên ba môi trường và đồng bộ bằng chứng/báo cáo. Chỉ xác nhận đã đọc khi bạn thực sự đọc. Đọc và sửa `reports/AI_CRITIQUE.md` theo trải nghiệm thật; bản hiện tại là AI soạn.

## 4. Điểm tự đánh giá đã chọn và chốt nộp

Bạn đã yêu cầu cho full điểm: Task 1 = 30/30; Task 2 = 40/40; Task 3 = 20/20; skill/demo = 10/10; tổng 100/100. Bảng điểm đã đồng bộ theo lựa chọn này. Điểm tự chấm không xác nhận đã đủ human review hoặc video demo. Khi các mục còn thiếu hoàn tất, tên ZIP cuối dự kiến là `23120207_HW03_AI_GUIUsability_100.zip`.

Bạn có thể trả lời một lần:

```text
Human review: [đường dẫn phiếu đã điền].
Mục tôi tự bổ sung: [nội dung + lý do AI bỏ sót + quan sát].
AI Critique: [đã rà/sửa tại file].
YouTube demo: [URL].
AI audit: [đã đọc; còn/không còn nguồn chat khác].
```

Chạy `python3 scripts/validate_submission.py` để xem những mục còn thiếu. ZIP hiện tên DRAFT vì còn đầu vào bắt buộc từ sinh viên; không đổi tên thành điểm tùy ý để coi là hoàn tất. Bản cuối có dạng `23120207_HW03_AI_GUIUsability_<điểm ba chữ số>.zip`.

Hạn đã kiểm tra trên Moodle: **13:00 ngày 16/11/2026 (giờ Việt Nam)**, cutoff cùng giờ. Link nộp: https://courses.fit.hcmus.edu.vn/mod/assign/view.php?id=129903. Chưa nộp Moodle. Khi nộp, chọn “Em làm một mình”, kiểm tra trạng thái cuối Submitted; có file trên trang chưa chứng minh đã nộp hoàn tất.
