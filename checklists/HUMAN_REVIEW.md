# Phiếu rà soát checklist của sinh viên

Trạng thái: CHƯA ĐƯỢC SINH VIÊN RÀ SOÁT. 48 mục ban đầu và G49–G51 bổ sung đều do Codex thiết kế/thực thi theo yêu cầu sinh viên. Không có mục nào được gán là “sinh viên tự bổ sung”.

Theo yêu cầu sinh viên, Codex đã viết [bản AI rà soát bổ sung](AI_REVIEW.md). Bản đó hỗ trợ đọc và phản biện hồ sơ; không điền thay quyết định/quan sát cá nhân trong phiếu này.

Đọc kết quả, so sánh bài giảng và SUT. Chấp nhận/sửa/loại từng mục, ghi lý do. Tự bổ sung những mục thực tế mà AI bỏ sót, ghi vì sao (prompt thiếu ngữ cảnh, giới hạn mô hình, đặc thù giao diện). Bổ sung rồi thực thi trên đủ môi trường, không chỉ thêm cho đủ số lượng.

| Mục | Quyết định của sinh viên | Sửa đổi/lý do | Ngày giờ |
|---|---|---|---|

| Mục sinh viên tự bổ sung | IA | Bước thực thi và kỳ vọng | Vì sao AI bỏ sót | Kết quả/bằng chứng |
|---|---|---|---|---|

Gợi ý để sinh viên tự đánh giá, chưa tính là bổ sung của sinh viên: focus có nhìn thấy khi dùng bàn phím, đọc bằng screen reader thật, tương phản chữ giá, phóng to 200%, hướng RTL nếu nằm trong yêu cầu, dark mode nếu được hỗ trợ. Không báo thiếu dark mode/RTL là bug nếu sản phẩm không có yêu cầu hỗ trợ.

Điểm AI đã bỏ sót trong kế hoạch trước: giả định có bộ lọc/sắp xếp, chọn tai nghe dưới 500.000 ₫ dù seed rẻ nhất là 4 triệu, và coi đổi viewport như nền tảng khác. Bản hiện tại đã sửa theo quan sát/source; đây vẫn là chỉnh sửa của AI, chờ sinh viên phản biện.


## Phần phản biện đã được chuẩn bị

Đã có [bản phản biện AI](../reports/AI_CRITIQUE.md), [bản AI rà soát](AI_REVIEW.md) và [ba tiêu chí bổ sung đã kiểm thử](ADDITIONS.md). Sinh viên có thể đọc đối chiếu trực tiếp từng kết luận và bằng chứng; không cần viết lại báo cáo từ đầu. Tác giả đề xuất/thực thi G49–G51 vẫn ghi Codex. Ô quyết định sinh viên phía trên chỉ điền khi có việc xem xét thực tế; không có chữ ký hoặc lời xác nhận tự tạo.

## Chốt theo phản hồi ngày 16/11/2026

Sau khi được hỏi về phần tự rà soát/tự bổ sung, sinh viên trả lời “nếu thiếu thì tự bổ sung”, tiếp tục giao AI thực hiện. Đã có AI_REVIEW.md, ADDITIONS.md và phản biện đầy đủ; G49–G51 vẫn được ghi đúng tác giả AI. Chưa nhận được quyết định/chỉnh sửa hoặc quan sát tự phát hiện cụ thể từ sinh viên, vì vậy các ô trên không được tự điền và human_review_complete vẫn false. Đây là giới hạn tuân thủ §2 và Task 1, không phải lỗi thiếu file.
