# Kế hoạch đánh giá usability G2

Trạng thái: đã thiết kế; chưa thực hiện pilot và 7 phiên chính thức. Người điều hành: Nguyễn Bảo An, 23120207. Không có dữ liệu người tham gia hay điểm SUS tại thời điểm lập tài liệu.

## Mục tiêu và phạm vi

Đo khả năng người mua tìm sản phẩm theo nhu cầu/ngân sách, hiểu thông tin chi tiết và xác nhận sản phẩm đã vào giỏ. Quan sát thời gian, lần thao tác sai, lần do dự, khả năng khôi phục và mức tự tin. SUT là EShop, màn hình chính Home/Search, hỗ trợ Product Detail và Cart; FR-05, FR-06 và phần tích hợp FR-07.

SUT hiện có 5 sản phẩm seed. AirPods Pro 2 giá 6.000.000 ₫, Keychron Q1 giá 4.000.000 ₫. Giao diện không có bộ lọc giá/danh mục, sắp xếp, đánh giá hay chính sách đổi trả. Vì vậy không giao các bước không tồn tại trong kế hoạch cũ. Đây là điều chỉnh của trợ lý AI dựa trên SUT, đang chờ sinh viên duyệt.

## Kịch bản đưa cho người tham gia

“Bạn muốn mua một chiếc tai nghe để nghe nhạc và có ngân sách tối đa 7 triệu đồng. Hãy dùng cửa hàng này để chọn sản phẩm phù hợp, xem những thông tin bạn cần trước khi quyết định, rồi cho một chiếc vào giỏ. Bạn dừng khi tin rằng giỏ hàng đã đúng. Chưa cần đặt hàng hay thanh toán.”

Đọc nguyên văn mục tiêu. Không nêu tên AirPods, vị trí nút hay số lần phải bấm. Người tham gia tự chọn cách tìm. Nếu họ yêu cầu thông tin không có, ghi lại nhu cầu thay vì tự thêm dữ liệu.

## Người tham gia và chuẩn bị

- Tuyển 7 người thật ngoài lớp đang học môn này; ưu tiên người mua hàng trực tuyến không làm IT/testing. Pilot dùng mã PILOT, tách khỏi 7 phiên phân tích.
- Xin phép dùng tên, liên hệ để TA xác minh; xin phép quay màn hình, và hỏi riêng quyền ghi âm. Không ghi âm nếu chưa đồng ý. Không tạo tài khoản cá nhân hoặc giao dịch thật.
- Bản nộp chỉ ghi SĐT/Zalo đã che 4 số giữa, ví dụ 090****123. Bản liên hệ gốc, nếu cần xác minh, lưu riêng trong `usability/private/`, không commit, không đưa lên GitHub.
- Mỗi phiên dùng cùng bản SUT và dữ liệu seed, cửa sổ mới, giỏ trống, cùng kích thước màn hình. Ghi browser/OS và commit SUT. Không sửa lỗi giữa các phiên chính thức; nếu bắt buộc đổi, ghi phiên bản và ảnh hưởng.
- Dự kiến 15–20 phút/phiên: giới thiệu và đồng ý 2 phút, thao tác tối đa 10 phút, SUS và hỏi sâu 5–8 phút. Đây là kế hoạch thời lượng, không phải số liệu quan sát.

## Pilot trước phiên chính thức

Chạy với một người trước. Ghi vào `sessions/PILOT.md`: ngày giờ, kịch bản có hiểu được không, seed có sản phẩm phù hợp không, trục trặc môi trường, thời lượng thật, thay đổi sau pilot và phiên bản kịch bản đã chốt. Không dùng điểm pilot để đủ n=7.

## Kịch bản điều hành

1. “Mình đang kiểm tra sản phẩm, không đánh giá năng lực của bạn. Bạn cứ thao tác như khi mua hàng và nói ra điều bạn đang nghĩ. Bạn có thể dừng bất kỳ lúc nào.”
2. Xác nhận đồng ý tham gia, quay màn hình và ghi âm riêng biệt. Bắt đầu ghi màn hình nếu được đồng ý. Đọc kịch bản; xác nhận họ hiểu mục tiêu, không hướng dẫn giao diện.
3. Bắt đầu đồng hồ khi họ bắt đầu thao tác. Ghi mốc thời gian, thao tác, phát ngôn nguyên văn và biểu hiện quan sát được vào mẫu phiên. Phân biệt phát ngôn với diễn giải của người điều hành.
4. Khi im lặng, có thể hỏi trung lập: “Bạn đang nghĩ gì?”. Khi do dự, hỏi “Bạn mong điều gì sẽ xảy ra?”. Không chỉ vào nút, giải thích chức năng hay nói lỗi đã biết.
5. Chỉ can thiệp khi người tham gia không thể tiến tiếp. Ghi thời điểm, nguyên nhân và câu hỗ trợ chính xác; kết quả đó là hoàn thành có hỗ trợ. Nếu hết 10 phút, ghi dừng theo giới hạn, không tự gán hoàn thành.
6. Kết thúc khi giỏ có đúng 1 tai nghe phù hợp ngân sách và người dùng tuyên bố xong, hoặc họ dừng/bị chặn/hết giờ. Ghi kết quả, thời gian thực và giỏ thực tế.
7. Cho điền 10 câu SUS ngay sau thao tác, trước phần hỏi sâu. Không gợi ý điểm. Sau đó hỏi 4 câu mở bên dưới và những điểm đã quan sát.
8. Lưu ghi chú, phản hồi gốc, đường dẫn video/ảnh. Tạo một commit riêng cho phiên đã thực sự hoàn thành.

## Câu hỏi mở sau phiên

1. Clarity: Thông tin hay nhãn nào khiến bạn khó hiểu? Bạn nghĩ chúng có nghĩa gì?
2. Error recovery: Khi thao tác không ra kết quả mong đợi, bạn đã làm gì? Điều gì giúp hoặc cản bạn tiếp tục?
3. Speed: Đoạn nào khiến bạn mất nhiều thời gian nhất? Bạn đã chờ hay phải làm lại gì?
4. Trust: Bạn dựa vào dấu hiệu nào để tin giá/sản phẩm/số lượng trong giỏ là đúng? Điều gì làm bạn chưa yên tâm?

## Phân tích sau khi có dữ liệu thật

Tính SUS từng người rồi trung bình 7 người. SUS là thang 0–100, không phải phần trăm hoàn thành. Báo cáo số phiên thành công độc lập/có hỗ trợ/bị chặn, thời gian trung vị và khoảng min–max từ quan sát thật. Không suy rộng mẫu 7 người thành toàn bộ người dùng.

Nhóm friction theo hiện tượng và nguyên nhân. Ghi số người gặp theo mã P1–P7, thời điểm/video minh chứng, phát ngôn thật, lỗi tái hiện độc lập và đề xuất cải thiện. Tách bug cụ thể khỏi vấn đề thiết kế lặp lại. Blocker: chặn mục tiêu và không có cách phục hồi phù hợp; Major: cần hỗ trợ/làm lại đáng kể; Minor: vẫn hoàn thành, ảnh hưởng nhỏ. Không suy ra tần suất từ số lỗi tự động.

Nguồn thang đo: John Brooke, “SUS - A quick and dirty usability scale”, tài liệu được học phần liên kết: https://hell.meiert.org/core/pdf/sus.pdf.
