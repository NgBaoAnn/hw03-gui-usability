# AI Critique

Trạng thái: bản AI soạn để sinh viên rà soát và sửa theo trải nghiệm thật; chưa được sinh viên xác nhận.

Trong bài HW03, AI hỗ trợ thiết kế checklist, thực thi kiểm thử và tổ chức bằng chứng. Hạn chế rõ nhất xuất hiện ở kế hoạch ban đầu: AI giả định EShop có bộ lọc giá, sắp xếp và đánh giá sản phẩm dù giao diện thực tế không có. Kịch bản tai nghe dưới 500.000 đồng cũng không phù hợp dữ liệu mẫu. Nguyên nhân là mô hình dựa vào khuôn mẫu thương mại điện tử và chưa kiểm tra SUT trước khi đề xuất. Khi đối chiếu mã nguồn và dữ liệu chạy thật, phạm vi đã được điều chỉnh.

Kết quả tự động cũng cần kiểm chứng. Bộ chạy ban đầu đọc nội dung ngay sau khi bấm chuyển trang, khiến một số kiểm tra số lượng bị đánh dấu Passed khi giao diện vẫn ở trang chi tiết. Sau khi bổ sung điều kiện chờ URL và tiêu đề giỏ, hai trình duyệt được chạy lại. Trường hợp này cho thấy lỗi của công cụ có thể tạo cảm giác chắc chắn sai.

AI còn dễ nhầm giữa số mục Failed và số bug độc lập, hoặc coi viewport nhỏ là nền tảng mới. Báo cáo vì vậy gom lỗi theo nguyên nhân và tách kiểm tra responsive khỏi cross-browser. Nguyên tắc hợp tác rút ra là yêu cầu AI chỉ rõ nguồn kỳ vọng, phép đo, bằng chứng và phần chưa xác minh. Sinh viên vẫn phải tự phản biện checklist, bổ sung mục còn thiếu và thu dữ liệu người dùng thật. Điểm SUS, phát ngôn và danh tính không thể suy ra từ kiểm thử tự động.
