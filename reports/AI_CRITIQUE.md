# AI Critique

Trạng thái: bản AI soạn theo yêu cầu sinh viên, có bằng chứng đối chiếu; chưa xác nhận là sinh viên tự phản biện.

AI hỗ trợ tổ chức checklist và chạy kiểm thử, nhưng kế hoạch đầu đã dựa quá nhiều vào khuôn mẫu thương mại điện tử. Bộ lọc, sắp xếp và tai nghe dưới 500.000 đồng được đề xuất trước khi đối chiếu SUT. Các giả định ấy không phù hợp giao diện và dữ liệu mẫu. Việc sửa phạm vi cần bắt đầu từ nguồn yêu cầu và quan sát ứng dụng.

Bộ checklist ban đầu có nhãn truy cập và thao tác bàn phím nhưng thiếu ngôn ngữ tài liệu, phép đo tương phản. Đây là giới hạn của cách chia nhỏ tiêu chí: kiểm tra màu nút theo quy chuẩn không đồng nghĩa chữ trên nút dễ đọc. Ba mục G49–G51 được AI bổ sung theo yêu cầu sinh viên và chạy trên Chrome, Firefox, Safari thật. Trang khai báo tiếng Anh dù nội dung tiếng Việt; chữ giá đạt 3,76:1, chữ nút đạt 3,30:1, thấp hơn ngưỡng 4,5:1 áp dụng cho cỡ chữ đã đo. Kết quả cho thấy quan sát bằng mắt cần được bổ sung bằng phép đo có nguồn.

Công cụ cũng có thể gây kết luận sai. Trước đây, đọc kết quả trước khi React chuyển trang làm một số kiểm tra số lượng bị đánh dấu sai. Điều kiện chờ và kiểm chứng trạng thái giỏ đã được bổ sung. Nguyên tắc hợp tác là giữ dấu vết nguồn, phân biệt heuristic với yêu cầu sản phẩm, và giới hạn kết luận theo bằng chứng. AI không được biến ảnh tái hiện thành phiên người dùng, hoặc gán phần mình viết thành đóng góp tự phát hiện của sinh viên.
