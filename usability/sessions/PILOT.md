# Phiên Pilot PILOT — PILOT (Kịch bản v0)

| Thông tin phiên kiểm thử | Giá trị ghi nhận |
|---|---|
| Người tham gia | PILOT (PILOT) — Khoa Hệ thống thông tin |
| Thông tin liên hệ (Masked) | Liên hệ đã che trong danh sách nộp riêng |
| Thời điểm thực hiện | 2026-11-10 08:30 |
| Kinh nghiệm sử dụng TMĐT | Quen dùng các sàn TMĐT (Shopee, Tiki), mua sắm 2–3 lần/tháng |
| Môi trường kiểm thử | EShop Web Frontend trên Chrome Desktop (Ubuntu 24.04 LTS / Windows 11), Viewport 1366×900, kết nối backend API localhost:3000. |
| Thời gian tác vụ | 390 giây (06:30) |
| Kết quả toàn luồng | Hoàn thành có trợ giúp |
| Quyền riêng tư & Ghi hình | Informed Consent: Đồng ý quan sát trực tiếp & ghi chép; Từ chối ghi hình video vì quyền riêng tư |

## 1. Kết quả thực hiện từng nhiệm vụ

| Nhiệm vụ | Mục tiêu kiểm thử | Kết quả thực tế |
|---|---|---|
| T1 | Xác định trạng thái đơn 30 triệu | Không trợ giúp |
| T2 | Xác định trạng thái đơn 45 triệu | Không trợ giúp |
| T3 | Hủy đúng đơn 28 triệu | Không trợ giúp |
| T4 | Nêu trạng thái cuối và dấu hiệu xác nhận | Có trợ giúp |

## 2. Nhật ký quan sát chi tiết (Observation Timeline)

| Mốc thời gian | Màn hình | Hành động của người tham gia | Ghi nhận quan sát của điều phối viên | Phát biểu của người tham gia (Think Aloud) | Vấn đề phát hiện |
|---|---|---|---|---|---|
| 00:00 | Home | Đọc kịch bản v0 dùng số tiền gần đúng | Bắt đầu đồng hồ pilot | — | — |
| 00:55 | Home | Hỏi đơn khoảng 30 triệu có tính đơn 28 triệu không | Vấn đề ở cách viết tình huống, không phải bằng chứng lỗi ứng dụng | — | — |
| 01:40 | Login | Đăng nhập bằng thông tin demo | Moderator làm rõ mục tiêu nhận diện đơn bằng số tiền chính xác | — | — |
| 03:00 | Profile | Đọc trạng thái hai đơn | T1/T2 hoàn thành | — | — |
| 04:00 | Profile | Hủy đơn 28 triệu | T3 hoàn thành | — | — |
| 04:30 | Profile | Hỏi khi nào được coi là xong | Chưa có điều kiện kết thúc rõ | — | — |
| 06:30 | Profile | Được nhắc xác nhận trạng thái cuối rồi dừng | T4 có trợ giúp; sửa kịch bản trước bảy hồ sơ v1 | — | — |

## 3. Can thiệp của người điều phối (Moderator Assistance)

| Mốc thời gian | Mức hỗ trợ | Nội dung can thiệp |
|---|---|---|
| 00:55 | Mức 1 | Dùng đúng số tiền từng đơn trong tình huống. |
| 06:30 | Mức 2 | Hãy xem và báo lại trạng thái cuối của đơn vừa hủy. |

## 4. Kết quả đánh giá thang điểm SUS

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Điểm SUS tổng hợp |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 52.5 / 100 |

## 5. Phỏng vấn sâu sau tác vụ (Probe Answers)

| Chủ đề phỏng vấn | Phản hồi chi tiết của người tham gia |
|---|---|
| Độ rõ ràng | Cụm khoảng 30 triệu dễ nhầm với 28 triệu. |
| Khôi phục / xử lý khó khăn | Tôi muốn biết cần báo lại trạng thái nào sau thao tác. |
| Tốc độ / nỗ lực | Tôi mất thời gian hỏi lại mục tiêu. |
| Sự tin tưởng | Có tiêu chí kết thúc rõ thì tôi dễ xác nhận hơn. |

## 6. Điều chỉnh kịch bản sau phiên Pilot

| Vấn đề phát hiện trong Pilot v0 | Cải tiến áp dụng cho Kịch bản v1 chính thức |
|---|---|
| Số tiền gần đúng gây nhầm nhận diện đơn. | v1 dùng chính xác 30.000.000, 45.000.000 và 28.000.000 đồng. |
| Chưa định nghĩa lúc kết thúc. | v1 yêu cầu báo trạng thái cuối và dấu hiệu xác nhận đã hủy. |
| Mẫu ghi chú trộn thời gian tác vụ với thời gian trả lời SUS. | Tách đồng hồ tác vụ tối đa 600 giây; SUS/probe sau khi dừng đồng hồ. |

*Lưu ý*: Phiên pilot dùng để tinh chỉnh kịch bản, số liệu của PILOT được phân tích riêng và không tính gộp vào thống kê 7 phiên chính thức.


Nguồn: hồ sơ sinh viên cung cấp ngày 15/11/2026; sinh viên xác nhận đã điều phối phiên thật trong chat. Không có video phiên trong hồ sơ. Bản công khai dùng mã thay họ tên/liên hệ.
