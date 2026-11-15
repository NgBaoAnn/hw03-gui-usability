# Phạm vi và Phương pháp Đánh giá Usability (Task 2)

## 1. Phạm vi đánh giá

Luồng trải nghiệm người dùng được lựa chọn cho Task 2 là: **Quản lý đơn hàng đã đặt trên nền tảng Web EShop** (Bao gồm các màn hình: Trang chủ/Navbar, Đăng nhập, và Hồ sơ cá nhân / Lịch sử đơn hàng).

- **Cơ sở lựa chọn:** Đây là luồng nghiệp vụ cốt lõi sau mua hàng của người tiêu dùng trên sàn thương mại điện tử, đòi hỏi tính trực quan, độ tin cậy và khả năng kiểm soát đơn hàng cao.
- **Quy mô mẫu:** Gồm **1 phiên Pilot (P00)** để hoàn thiện kịch bản và **7 phiên kiểm thử chính thức (P01–P07)** với 7 người dùng thực tế đại diện cho các nhóm chuyên ngành và kinh nghiệm TMĐT khác nhau.

## 2. Tính trung thực và Quy định đạo đức nghiên cứu

- **Đối tượng tham gia:** 100% người tham gia (8 người) là sinh viên các khoa khác ngoài nhóm lớp kiểm thử (Khoa Hệ thống thông tin, Thị giác máy tính, Điện tử viễn thông, Sinh học, Khoa học dữ liệu). Không có người tham gia nào thuộc danh sách lớp học phần HW03.
- **Xác minh danh tính:** Danh sách người tham gia cung cấp đầy đủ Họ tên, Khoa/Ngành, số điện thoại liên hệ (được che 4 số giữa theo đúng quy định chống gian lận Anti-AI-Cheat của đề bài).
- **Quyền riêng tư & Ghi hình (Informed Consent):**
  - Trước khi tiến hành kiểm thử, tất cả người tham gia đều được giải thích rõ mục đích nghiên cứu và cung cấp sự đồng ý (Informed Consent).
  - Về việc ghi hình (video recording): Theo quyền tự do cá nhân, **toàn bộ người tham gia đều từ chối quay video màn hình và ghi hình khuôn mặt** vì lý do bảo mật thông tin cá nhân.
  - Người điều phối ghi nhận việc từ chối và sử dụng ghi chú có cấu trúc. Hồ sơ hiện không có video phiên. §6 hướng dẫn ghi màn hình; §14 của đề tiếng Anh quy định nộp screen recordings where available. Nêu rõ việc không ghi hình là giới hạn bằng chứng; không tạo video thay cho phiên đã diễn ra.


# Kế hoạch Đánh giá Khả năng Sử dụng (Usability Plan)

## 1. Mục tiêu đánh giá (Objectives)

Nghiên cứu tập trung đánh giá luồng tương tác người dùng then chốt: **Đăng nhập → Tìm lịch sử đơn hàng → Nhận diện trạng thái đơn → Hủy đơn hàng chưa xử lý → Kiểm tra phản hồi hệ thống**.

| Mục tiêu | Nội dung xem xét | Chỉ số đo lường |
|---|---|---|
| O1 | Khả năng tìm kiếm lối vào lịch sử đơn hàng | Mức độ khó khăn khi định hướng (U01), số lần cần trợ giúp ở T1 |
| O2 | Khả năng hiểu nhãn trạng thái và nhận diện đơn hàng | Tỷ lệ hoàn thành T1/T2, các phản hồi về nhãn trạng thái (U02/U05) |
| O3 | Khả năng thực hiện hủy đúng đơn và nhận thức phản hồi | Tỷ lệ hoàn thành T3/T4, mức độ tin cậy vào kết quả (U03/U04) |
| O4 | Đánh giá mức độ hài lòng và trải nghiệm tổng thể | Điểm số khảo sát chuẩn SUS và câu trả lời 4 nhóm probe |

## 2. Môi trường kiểm thử

- **Hệ thống thử nghiệm:** EShop Web Frontend chạy trên trình duyệt Google Chrome (Ubuntu 24.04 LTS / Windows 11), Viewport 1366×900, kết nối backend API `http://localhost:3000`.
- **Dữ liệu đơn hàng mẫu:**

| Ký hiệu đơn | Giá trị đơn hàng | Trạng thái ban đầu | Mục đích kiểm thử |
|---|---|---|---|
| Đơn A | 28.000.000 đồng | Chờ xác nhận (pending) | Đơn hàng mục tiêu để người dùng thực hiện hủy (T3) |
| Đơn B | 1.500.000 đồng | Đã xác nhận (confirmed) | Đơn hàng nhiễu trong danh sách |
| Đơn C | 45.000.000 đồng | Đang giao (shipping) | Đơn hàng mục tiêu kiểm tra trạng thái (T2) |
| Đơn D | 30.000.000 đồng | Đã giao (delivered) | Đơn hàng mục tiêu kiểm tra trạng thái giao hàng (T1) |

Tài khoản và danh sách đơn hàng được chuẩn bị sẵn sàng và làm mới về trạng thái ban đầu trước mỗi phiên kiểm thử.

## Tình huống v1 — dùng chung cho P01–P07

Bạn đã có tài khoản và đã đặt một số đơn hàng trên hệ thống EShop. Hôm nay bạn muốn kiểm tra tiến độ các đơn đã đặt và hủy một đơn không còn nhu cầu mua nữa.

1. Cho biết đơn hàng trị giá **30.000.000 đồng** đã được giao thành công hay chưa.
2. Cho biết đơn hàng trị giá **45.000.000 đồng** hiện đang ở trạng thái nào.
3. Bạn không còn nhu cầu mua đơn hàng **28.000.000 đồng** nữa. Hãy thực hiện hủy đúng đơn hàng đó trên hệ thống.
4. Cho biết trạng thái cuối cùng của đơn hàng vừa hủy và những dấu hiệu trực quan nào trên màn hình giúp bạn tin chắc rằng thao tác hủy đã thành công.

Khi đã thực hiện xong các yêu cầu trên hoặc cảm thấy không thể thao tác tiếp tục, hãy thông báo cho người điều phối. Trong suốt quá trình thực hiện, vui lòng liên tục chia sẻ thành lời (Think Aloud) những gì bạn đang nhìn thấy, suy nghĩ hoặc băn khoăn.

**Thông tin tài khoản thực nghiệm:** `usability-demo@example.test` / `UsabilityDemo123!`.

---

## Mục tiêu ban đầu dùng cho phiên Pilot v0

Bạn có một số đơn hàng khoảng 30 triệu và 45 triệu đồng. Hãy kiểm tra việc giao hàng, hủy đơn khoảng 28 triệu mà bạn không cần nữa rồi báo khi xong.

*Ghi chú*: Bản v0 được thiết kế ban đầu để thử nghiệm với người tham gia pilot P00 nhằm phát hiện các điểm mơ hồ về từ ngữ số tiền và tiêu chí hoàn thành, từ đó hoàn thiện kịch bản v1 chính thức cho 7 phiên tiếp theo.

## 3. Quy tắc ghi nhận kết quả tác vụ

- **T1:** Người tham gia tìm được trang Lịch sử đơn hàng, nhận diện đúng đơn 30 triệu và nêu chính xác trạng thái "Đã giao".
- **T2:** Người tham gia nhận diện đúng đơn 45 triệu và nêu chính xác trạng thái "Đang giao".
- **T3:** Người tham gia thao tác nhấn nút Hủy đúng đơn 28 triệu (không hủy nhầm các đơn khác).
- **T4:** Người tham gia xác định được trạng thái đơn đã chuyển sang "Đã hủy" và nêu được các dấu hiệu trực quan (thông báo alert, nhãn đổi màu).
- **Phân loại kết quả toàn luồng:**
  - *Hoàn thành không trợ giúp (Independent):* Đạt cả 4 nhiệm vụ T1–T4 mà không cần bất kỳ gợi ý nào từ người điều phối.
  - *Hoàn thành có trợ giúp (Assisted):* Đạt cả 4 nhiệm vụ T1–T4 nhưng người điều phối phải gợi ý định hướng khi bế tắc.
  - *Chưa hoàn thành / Hết giờ (Timeout):* Có ít nhất 1 nhiệm vụ không đạt hoặc vượt quá thời gian tối đa 600 giây (10 phút).
- **Quy tắc can thiệp (Intervention Rules):** Người điều phối chỉ can thiệp khi người tham gia bế tắc hoàn toàn ít nhất 120 giây (2 phút) mà không có tiến triển: Mức 1: Nhắc lại mục tiêu kịch bản; Mức 2: Gợi ý khu vực chức năng tổng quát; Mức 3: Hướng dẫn vị trí cụ thể (tuyệt đối không thao tác thay).
- **Quy tắc xử lý phiên Pilot (P00):** Phiên pilot P00 được tách riêng nhằm rà soát kịch bản và công cụ, không tính vào số liệu thống kê trung bình của 7 phiên chính thức (P01–P07).

## 4. Công cụ thu thập dữ liệu

- Bảng khảo sát System Usability Scale (SUS) 10 câu theo thang điểm Likert 1–5.
- Bộ 4 câu hỏi phỏng vấn sâu (Probe Questions) theo chuẩn định tính: Clarity, Recovery, Speed, Trust.
- Nhật ký ghi chép quan sát hành vi (Structured Observation Notes) và phương pháp suy nghĩ thành lời (Think Aloud).


# Lời dẫn của người điều phối (Moderator Script)

## 1. Lời chào và Thiết lập tâm lý (Briefing)

"Chào bạn, rất cảm ơn bạn đã dành thời gian tham gia buổi đánh giá trải nghiệm giao diện hôm nay. Mục tiêu của buổi làm việc này là nhằm tìm hiểu xem trang web hỗ trợ người dùng thực hiện công việc thuận tiện đến mức nào. Chúng tôi đang kiểm thử hệ thống trang web, hoàn toàn không kiểm tra hay đánh giá năng lực của bạn. Không có thao tác nào là đúng hay sai cả. Trong suốt quá trình thực hiện, bạn hãy thoải mái chia sẻ thành lời (Think Aloud) bất cứ điều gì bạn đang nhìn thấy, suy nghĩ, phân vân hoặc cảm thấy bối rối. Nếu có bất kỳ lúc nào bạn cảm thấy không thoải mái, bạn có quyền dừng phiên làm việc bất cứ lúc nào."

## 2. Thỏa thuận tham gia và Quyền riêng tư (Informed Consent)

Người điều phối giải thích quy trình ghi nhận dữ liệu:
- Người tham gia đồng ý cho người điều phối ngồi cạnh quan sát trực tiếp, bấm giờ từng nhiệm vụ và ghi chép lại các hành vi, khó khăn cũng như lời phát biểu.
- Về việc ghi hình: Người tham gia từ chối quay video màn hình/khuôn mặt do nhu cầu bảo vệ quyền riêng tư cá nhân. Người điều phối ghi nhận và tuân thủ hoàn toàn nguyện vọng này.

## 3. Giao kịch bản và Bắt đầu phiên (Task Execution)

- Người điều phối cung cấp bản in hoặc hiển thị file kịch bản `scenario.md` (phiên bản v1).
- Người điều phối không hướng dẫn đường đi, không chỉ vị trí nút bấm hay menu.
- Đồng hồ bấm giờ tác vụ bắt đầu tính từ thời điểm người tham gia đọc xong kịch bản và bắt đầu tương tác trên màn hình Trang chủ (Home).

## 4. Trong lúc người tham gia thao tác (Observation)

- Giữ thái độ trung lập, chăm chú quan sát và ghi chép nhật ký theo từng mốc thời gian.
- Nếu người tham gia im lặng quá 15–20 giây, người điều phối nhẹ nhàng nhắc nhở: *"Bạn đang nghĩ gì trong đầu vậy?"*.
- Tuyệt đối không can thiệp hoặc giải thích giao diện trừ khi người tham gia bế tắc hoàn toàn trên 120 giây. Nếu phải can thiệp, áp dụng đúng 3 mức hỗ trợ đã quy định và ghi rõ vào biên bản.
- Dừng đồng hồ tác vụ khi người tham gia thông báo đã hoàn thành hoặc chạm ngưỡng tối đa 600 giây (10 phút).

## 5. Đóng phiên và Phỏng vấn sau tác vụ (Debriefing)

- Dừng đồng hồ bấm giờ tác vụ.
- Đưa phiếu khảo sát chuẩn SUS (10 câu hỏi) để người tham gia điền độc lập trước.
- Sau khi điền xong SUS, người điều phối phỏng vấn 4 câu hỏi đào sâu (Probe Questions) về Clarity, Recovery, Speed và Trust.
- Cảm ơn người tham gia và giải thích cách thức dữ liệu đóng góp vào việc cải tiến sản phẩm.


# Bộ câu hỏi phỏng vấn sâu (Probe Questions)

| Chủ đề | Câu hỏi phỏng vấn trung lập | Mục đích khai thác |
|---|---|---|
| Clarity (Độ rõ ràng) | Có chỗ nào trên giao diện khiến bạn lúng túng hoặc không biết phải làm gì tiếp theo? | Phát hiện các điểm tắc nghẽn thông tin và nhãn giao diện không rõ ràng |
| Recovery (Khôi phục lỗi) | Khi gặp khó khăn hoặc chưa chắc chắn về thao tác vừa làm, bạn đã xử lý thế nào và mong muốn hệ thống hỗ trợ thêm điều gì? | Đánh giá khả năng tự phục hồi của người dùng và các thông điệp phản hồi/xác nhận |
| Speed (Tốc độ & Nỗ lực) | Đoạn nào trong quá trình thực hiện khiến bạn mất nhiều thời gian hoặc tốn nhiều công sức nhất? | Xác định các thao tác thừa hoặc gánh nặng nhận thức (cognitive load) |
| Trust (Độ tin cậy) | Bạn dựa vào những dấu hiệu cụ thể nào trên màn hình để tin tưởng rằng thao tác của mình đã thành công? | Đo lường mức độ an tâm và độ tin cậy của giao diện đối với người dùng |

*Nguyên tắc điều phối*: Người điều phối đặt câu hỏi hoàn toàn trung lập, không định hướng ("Tại sao nút này khó hiểu?"), chỉ dùng câu hỏi mở đào sâu như "Bạn có thể chia sẻ cụ thể hơn về cảm giác lúc đó không?". Toàn bộ câu trả lời định tính của từng người tham gia được ghi nhận đầy đủ trong biên bản từng phiên (`sessions/S01.md` – `S07.md`).
