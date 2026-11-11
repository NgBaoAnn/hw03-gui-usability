# Kịch bản video demo skill

Trạng thái: sinh viên đã chọn **tự quay video dùng cho bài nộp**. Chưa nhận video hoặc YouTube URL của sinh viên. File `video/gui-g2-demo.mp4` dài 112,4 giây được giữ làm tham khảo do Codex ghi, có phụ đề, không âm thanh và có log tại `video/recording-log.json`; không gán nó thành bản quay của sinh viên.

Video ghi quá trình đọc nội dung skill, kiểm tra Home, tìm tai nghe, mở chi tiết, xác nhận lỗi lần thêm đầu, thử lại với hai click và kiểm chứng giỏ, rồi trình bày báo cáo B18. Đây là demo workflow kiểm thử do Codex thực hiện; không phải phiên người dùng hoặc bản quay sinh viên tự điều hành. Kịch bản dưới đây vẫn dùng được nếu sinh viên muốn bổ sung lời giải thích hoặc quay lại cách mình gọi agent.

1. Hiển thị SUT localhost, commit đang dùng và file SKILL.md. Giới thiệu phạm vi G2 và thông tin sinh viên.
2. Gọi skill bằng prompt thực tế: “Dùng skill gui-usability-evaluator trong thư mục skills của bài HW03. Đọc đặc tả EShop và chạy checklist cho luồng tìm sản phẩm, xem chi tiết, thêm giỏ. Ghi bằng chứng thật, tách lỗi công cụ khỏi lỗi SUT.”
3. Cho thấy agent đọc đặc tả, rà soát màn hình và dùng 48 mục có truy vết IA/FR. Giải thích chỗ kế hoạch cũ giả định sai về bộ lọc và giá.
4. Chạy đầy đủ một màn hình/luồng. Hiển thị lượt chạy, kiểm tra một lỗi thực tế (nút thêm giỏ lần đầu), mở ảnh gốc có email/MSSV/họ tên.
5. Mở bug Markdown và GitHub Issue kèm ảnh; mở Excel và test summary để thấy kết quả nối nhau.
6. Mở biểu mẫu usability và trình tính SUS. Nêu đúng trạng thái dữ liệu, không dùng dữ liệu tự tạo làm kết quả thật.
7. Quay liền mạch các bước chính; đăng YouTube Unlisted và đưa URL vào báo cáo sau khi video thật đã tồn tại. Kiểm tra link mở được bằng cửa sổ không đăng nhập.
