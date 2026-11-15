# Rà soát bổ sung do AI thực hiện

Người thực hiện: Codex. Theo yêu cầu sinh viên “bạn hãy tự ghi phần rà soát đi”. Nguồn: checklist 48 mục, ba JSON chạy cuối, danh mục bug, SUS và báo cáo hiện có. Lượt này rà hồ sơ/bằng chứng đã lưu; không phải lượt chạy browser mới hoặc đóng góp tự phát hiện của sinh viên.

## Kết quả đối chiếu

| Nội dung | Nhận xét và xử lý |
|---|---|
| Độ phủ IA | 48 ID duy nhất, mỗi IA 12 mục. Không bổ sung mục chỉ để tăng số lượng. |
| Kết quả ba browser | 144 kết quả Passed/Failed: 56 Passed, 88 Failed. Mọi Failed có Notes và ảnh. Không cộng lượt thử hoặc quan sát Safari cũ vào thống kê. |
| Gom bug | 30 mục fail ít nhất một browser được gom thành 23 nhóm GUI. Năm finding usability tách riêng; tổng 28 Issues không có nghĩa 28 lỗi chức năng độc lập. |
| G07 / B04: cắt ảnh | `object-cover` và tỷ lệ ảnh chứng minh có crop. Mức ảnh hưởng đến khả năng nhận diện sản phẩm còn cần đánh giá; giữ cách diễn đạt phát hiện heuristic, không suy ra mất nội dung quan trọng chỉ từ CSS. |
| G09 / B23: responsive | Tràn ngang 8 px được ghi trên Firefox desktop ở viewport 390 px. Không gán thành kiểm thử điện thoại hoặc hệ điều hành khác. |
| G13/G23: nhãn | DOM cho thấy thiếu liên kết nhãn. Chưa thực hiện screen reader thật; không diễn giải đây là kết quả thử với người dùng khiếm thị. |
| G16/G24: từ khóa | Phân biệt lỗi mã hóa dấu & với HTML injection. Thẻ b vô hại chứng minh HTML được render; chưa chứng minh thực thi JavaScript hoặc một chuỗi khai thác XSS. |
| G19–G22: số lượng | Bước bấm lần hai phải ghi rõ là workaround cho B18; không để việc thêm thất bại ở click đầu che mất kiểm tra dữ liệu biên. |
| G29: Back | Phép kiểm Safari dùng top-level native Back. Giữ kỳ vọng duy trì tìm kiếm là heuristic; không suy ra từ lịch sử iframe. |
| G37/G47/G48: mạng | Ghi rõ delay/503 được mô phỏng có kiểm soát; đây không phải bằng chứng production backend đã phát sinh 503. |
| G39/G41/G42: phản hồi | Ba mục đo vị trí/phạm vi phản hồi khác nhau. G39 và G42 có thể cùng nguyên nhân thiếu badge nên đã gom trong B17, không đếm thành hai bug độc lập. |
| Task 2 | Đối chiếu 70 câu trả lời CSV/JSON; pilot không cộng vào n=7. SUS 58,93 là điểm thang 0–100, không phải tỷ lệ thành công. Hoàn thành 6/7; thời gian 324 giây gồm timeout, 278 giây cho sáu ca hoàn thành. |
| Nguồn nghiên cứu | Phiên do sinh viên cung cấp và xác nhận. Không có kiểm chứng độc lập danh tính hoặc video phiên. Ảnh U01–U05 là agent tái hiện trên fixture, không phải ảnh của người tham gia. |
| Điểm tự chấm | Ghi 30/40/20/10 theo lựa chọn “cho full điểm”. Việc ghi điểm không thay bằng chứng human review hoặc video demo còn thiếu. |

## Phần chưa kiểm tra và gợi ý cho sinh viên

Focus nhìn thấy, screen reader, tương phản và zoom 200% chưa được kiểm tra đầy đủ trong bộ hiện tại. Đây là gợi ý của AI, chưa phải mục sinh viên tự bổ sung, chưa có kết quả Passed/Failed. Sinh viên cần quan sát thực tế, chọn tiêu chí có ý nghĩa và giải thích vì sao AI bỏ sót; sau đó mới đưa vào checklist và chạy trên các môi trường thích hợp.

Các giả định cũ về bộ lọc/sắp xếp, ngân sách 500.000 đồng và coi viewport là nền tảng đã được AI sửa theo SUT. Không ghi những sửa đổi này là việc sinh viên đã tự thực hiện.

Phiếu `HUMAN_REVIEW.md` giữ trạng thái chờ sinh viên. Việc sinh viên giao AI viết phần rà soát chưa chứng minh sinh viên đã tự đọc, phản biện hoặc phát hiện mục mới theo Task 1.
