# Đóng góp cá nhân của Nguyễn Bảo An

MSSV: **23120207**. Email: **23120207@student.hcmus.edu.vn**. Bài làm cá nhân. Cập nhật ngày 16/11/2026.

## Vai trò của sinh viên

Nguyễn Bảo An lựa chọn và xác nhận phạm vi bài, cung cấp thông tin và dữ liệu nghiên cứu, điều phối việc sử dụng AI, quyết định cách công bố hồ sơ và tự đánh giá bài làm. Phần điều phối các phiên usability được ghi nhận theo xác nhận trực tiếp của sinh viên trong cuộc trò chuyện. Các đóng góp dưới đây được đối chiếu với lời nhắn đã lưu; không suy ra từ tên người nộp hoặc số lượng file.

| Công việc | Đóng góp của Nguyễn Bảo An | Bằng chứng và phần AI hỗ trợ |
|---|---|---|
| Chọn phạm vi | Chọn G2 trong quá trình lập kế hoạch; xác nhận làm cá nhân và phạm vi G2 còn đúng. | Hội thoại lập kế hoạch trong AI_AUDIT_RECOVERED.md và xác nhận trong AI_TRANSCRIPT.md. AI thiết kế chi tiết checklist và điều chỉnh giả định theo SUT. |
| Xác nhận thông tin bài nộp | Xác nhận tên, MSSV và email sinh viên; yêu cầu đồng bộ hồ sơ Task 2 về Nguyễn Bảo An – 23120207. | Lời nhắn xác nhận email và yêu cầu sửa thông tin. AI cập nhật biểu mẫu, overlay, báo cáo và file nộp. |
| Điều phối công việc với AI | Yêu cầu thực hiện các phần của homework, rà phần còn thiếu, tích hợp Task 2 và tiếp tục phản biện/bổ sung checklist. | Chuỗi yêu cầu và đầu ra được lưu trong AI_TRANSCRIPT.md. AI đề xuất tiêu chí, viết bộ chạy và thực thi kiểm tra; không gán việc đó thành thao tác thủ công của sinh viên. |
| Hỗ trợ môi trường Safari | Đồng ý dùng Safari WebDriver và xác nhận đã trực tiếp xác thực/bật quyền trên máy khi hệ thống yêu cầu. | Hai lời nhắn đồng ý và xác nhận đã bật quyền. AI chạy bộ kiểm tra, xử lý lỗi harness và khôi phục thiết lập sau lượt chạy. |
| Điều phối nghiên cứu usability | Sinh viên xác nhận đã tự điều phối một pilot và bảy phiên thật; cung cấp folder task2_usability chứa biên bản, câu trả lời SUS và dữ liệu tổng hợp. | Câu trả lời: “Có, đây là các phiên thật tôi đã điều phối”. Nguồn và SHA-256 được lưu tại usability/provenance.json. AI đối chiếu CSV/JSON, tính lại điểm và tổng hợp; không xác minh độc lập danh tính hoặc việc diễn ra phiên. |
| Quyết định phạm vi Task 2 | Yêu cầu giữ nội dung và số liệu hồ sơ đã cung cấp khi sửa thông tin sinh viên; do đó Task 2 giữ luồng quản lý đơn hàng, Task 1 giữ G2. | Lời nhắn yêu cầu “còn lại giống với bài làm tôi gửi vào”. AI làm rõ hai phạm vi trong báo cáo, giữ dữ liệu gốc và liên kết bằng chứng tái hiện riêng. |
| Yêu cầu cải thiện phản biện | Chủ động yêu cầu AI viết phần rà soát, phản biện và bổ sung checklist trước khi quay demo. | Lời nhắn yêu cầu và các file AI_REVIEW.md, ADDITIONS.md, AI_CRITIQUE.md. G49–G51 do AI đề xuất/thực thi; đây là đóng góp điều phối của sinh viên, chưa phải xác nhận sinh viên tự phát hiện ba tiêu chí đó. |
| Quyết định công bố | Cho phép công khai repo bài làm để người chấm xem Issues và ảnh. | Lời nhắn “Cho phép công khai repo bài làm”. AI thực hiện công bố và giữ danh sách tên/liên hệ người tham gia ngoài repo public; không gán thao tác che dữ liệu cho sinh viên. |
| Tự đánh giá | Chọn tự chấm toàn bộ điểm: Task 1 = 30, Task 2 = 40, Task 3 = 20, skill/demo = 10; tổng 100/100. | Lời nhắn “cho full điểm”. AI điền bảng theo lựa chọn này. Đây là điểm tự đánh giá, không phải điểm giảng viên hoặc chứng nhận bài đã hoàn tất. |
| Video demo | Quyết định tự quay video demo và nhắc lại lựa chọn này khi giao AI hoàn thiện phần còn lại. | Lời nhắn “video tôi tự quay” và “tôi tự làm video demo”. Đây là phần sinh viên nhận thực hiện; hiện chưa có video/URL được cung cấp để ghi là đã hoàn thành. |

## Sản phẩm do AI hỗ trợ thực hiện

AI thiết kế 48 tiêu chí đầu và bổ sung G49–G51, thực thi kiểm tra trên Chrome/Firefox/Safari, chụp bằng chứng, soạn bug và tạo Issues, đối chiếu SUS, chuẩn hóa hồ sơ, xây skill, soạn phản biện, cập nhật báo cáo/PDF/Excel, commit và đóng ZIP. Kết quả hiện có: 51 tiêu chí, 153 kết quả kiểm tra, 25 nhóm bug GUI và năm finding usability. Bản MP4 tham khảo có sẵn do AI ghi; không tính là video sinh viên tự quay.

Người nộp là sinh viên; tác giả đề xuất/thực thi từng phần vẫn được khai báo đúng trong audit. Không quy đổi việc giao AI thực hiện thành bằng chứng sinh viên đã tự thao tác các bước kỹ thuật.

## Trạng thái cần hoàn tất

- Chưa có xác nhận thực tế rằng sinh viên đã tự rà soát kết quả hoặc tự phát hiện/bổ sung một tiêu chí mà AI bỏ sót. Phiếu HUMAN_REVIEW.md giữ nguyên trạng thái chờ; bản ghi đóng góp này không ký thay sinh viên.
- Chưa có video demo sinh viên tự quay và URL YouTube. Việc đã nhận quay video chưa được ghi là sản phẩm hoàn thành.
- Chưa nộp Moodle. Không có video phiên usability trong dữ liệu được cung cấp; giới hạn này đã được nêu trong báo cáo.

Các nguồn tham chiếu cùng hồ sơ: [hội thoại hiện tại](AI_TRANSCRIPT.md), [hội thoại lập kế hoạch](AI_AUDIT_RECOVERED.md), [nguồn Task 2](../usability/provenance.json), [AI rà soát](../checklists/AI_REVIEW.md), [checklist bổ sung](../checklists/ADDITIONS.md), [phiếu sinh viên](../checklists/HUMAN_REVIEW.md).
