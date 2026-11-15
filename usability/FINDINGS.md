# Báo cáo Kết quả Đánh giá Khả năng Sử dụng (Usability Evaluation Report)

## 1. Thiết kế và Thông số Thực nghiệm

Nghiên cứu đánh giá khả năng sử dụng (Usability Evaluation) được tiến hành trên luồng nghiệp vụ: **Quản lý đơn hàng đã đặt trên nền tảng Web EShop** với sự tham gia của **1 người thực hiện phiên Pilot (P00)** và **7 người tham gia chính thức (P1–P7)**. Toàn bộ người tham gia là sinh viên các khoa khác thuộc khối ngành kỹ thuật, tự nhiên và kinh tế (ngoài môn học kiểm thử), đem lại góc nhìn khách quan và chân thực.

| Chỉ số đánh giá (7 phiên chính thức P1–P7) | Kết quả thực tế |
|---|---|
| Hoàn thành độc lập không cần trợ giúp | 4/7 (57.1%) |
| Hoàn thành có sự trợ giúp của điều phối viên | 2/7 (28.6%) |
| Chưa hoàn thành / Quá thời gian quy định (Timeout) | 1/7 (14.3%) |
| Tỷ lệ hoàn thành nhiệm vụ chung (Completion Rate) | 6/7 (85.7%) |
| Thời gian hoàn thành trung bình (tính cả ca timeout) | 324.00 giây (05:24) |
| Trung vị thời gian; Khoảng biến thiên (Min – Max) | 268 giây; 160 – 600 giây |
| Thời gian trung bình của các ca hoàn thành thành công | 278.00 giây (n=6) |
| Điểm SUS trung bình; Điểm SUS trung vị | 58.93 / 100; 62.50 / 100 |
| Độ lệch chuẩn mẫu SUS; Khoảng điểm (Min – Max) | 20.91; 27.5 – 87.5 |
| Số người tham gia thực tế / Số phiên thực hiện | 8 người (1 pilot + 7 chính thức) / 8 phiên |
| Tình trạng ghi hình / Bảo mật quyền riêng tư | Đồng ý quan sát trực tiếp & khảo sát; Từ chối ghi hình video |

## 2. Kết quả thực hiện của từng người tham gia

| Mã | Họ và Tên | Khoa / Ngành | T1 | T2 | T3 | T4 | Thời gian | Điểm SUS | Đánh giá toàn luồng |
|---|---|---|---|---|---|---|---|---|---|
| P1 | P1 | Khoa Thị giác máy tính | Không trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 205s | 75.0 | Độc lập |
| P2 | P2 | Khoa Hệ thống thông tin | Không trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 268s | 62.5 | Độc lập |
| P3 | P3 | Khoa Điện tử viễn thông | Có trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 440s | 37.5 | Có trợ giúp |
| P4 | P4 | Khoa Sinh học | Không trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 160s | 87.5 | Độc lập |
| P5 | P5 | Khoa Hệ thống thông tin | Không trợ giúp | Không trợ giúp | Không trợ giúp | Có trợ giúp | 365s | 55.0 | Có trợ giúp |
| P6 | P6 | Khoa Khoa học dữ liệu | Có trợ giúp | Không trợ giúp | Thất bại / hết giờ | Chưa thực hiện | 600s | 27.5 | Hết giờ (Timeout) |
| P7 | P7 | Ngành Khoa học dữ liệu | Không trợ giúp | Không trợ giúp | Không trợ giúp | Không trợ giúp | 230s | 67.5 | Độc lập |

*Nhận xét*:
- 4/7 người tham gia (P1, P2, P4, P7) hoàn thành luồng công việc hoàn toàn độc lập với thời gian nhanh chóng (từ 205s đến 280s).
- 2/7 người tham gia (P3, P5) gặp lúng túng trong khâu tìm kiếm trang Lịch sử đơn hàng và cần gợi ý định hướng từ điều phối viên nhưng sau đó hoàn thành tốt các bước tiếp theo.
- 1/7 người tham gia (P6) do ít kinh nghiệm thao tác TMĐT và thao tác cẩn trọng quá mức nên bị hết thời gian (600 giây) ở bước T3.

## 3. Phân tích Thang điểm SUS (System Usability Scale)

Điểm SUS trung bình đạt **58.93 / 100** (thấp hơn ngưỡng tiêu chuẩn ngành 68 điểm). Điều này phản ánh rõ ràng rằng giao diện hiện tại của EShop còn tồn tại nhiều rào cản về tính dễ dùng và độ trực quan:
- Người dùng có nền tảng kỹ thuật cao và quen TMĐT (như P4 - SUS 85.0, P1 - SUS 75.0) cho điểm khá tích cực vì họ có khả năng tự suy luận logic giao diện.
- Ngược lại, người dùng ít thao tác hoặc quen dùng ứng dụng di động (như P6 - SUS 32.5, P3 - SUS 42.5) đánh giá thấp do giao diện thiếu các chỉ báo điều hướng rõ ràng và thiếu hộp thoại xác nhận an toàn.

## 4. Gom nhóm Vấn đề Usability và Xếp hạng Mức độ Nghiêm trọng

Thang phân loại mức độ nghiêm trọng (Severity Ranking):
- **Mức 4 (Blocker):** Chặn đứng hoàn toàn người dùng, không thể hoàn thành mục tiêu.
- **Mức 3 (Major):** Gây trở ngại lớn, khiến người dùng bối rối nghiêm trọng hoặc cần trợ giúp.
- **Mức 2 (Minor):** Gây chậm trễ, nhầm lẫn tạm thời nhưng người dùng vẫn tự khắc phục được.
- **Mức 1 (Minor):** Khó chịu nhỏ về mặt thị giác hoặc thẩm mỹ.

| Ưu tiên | Mã | Vấn đề Usability phát hiện | Mức độ | Tần suất (/7) | Các phiên ghi nhận | Phân loại |
|---|---|---|---|---|---|---|
| 1 | U01 | Lối vào lịch sử đơn qua lời chào khó nhận biết | Mức 3 | 5/7 | P1 (00:45); P2 (01:08); P3 (01:35); P5 (00:35); P6 (02:10) | Vấn đề Điều hướng (Navigation UX) |
| 2 | U03 | Nút Hủy xuất hiện ở đơn đang giao gây hoang mang kỳ vọng | Mức 3 | 3/7 | P1 (02:05); P4 (01:40); P7 (02:35) | Lỗi Trạng thái & Nghiệp vụ (State Bug) |
| 3 | U04 | Thiếu hộp thoại xác nhận (Confirmation Modal) trước khi hủy đơn | Mức 3 | 3/7 | P3 (05:45); P5 (04:00); P6 (07:00) | Vấn đề Phản hồi & Khôi phục lỗi (Feedback & Recovery) |
| 4 | U02 | Tiêu đề Đăng Ký trên form đăng nhập gây nhầm | Mức 2 | 3/7 | P2 (00:32); P3 (00:45); P6 (01:00) | Lỗi Nhãn Giao diện (GUI Bug) |
| 5 | U05 | Nhận diện đơn hàng chỉ dựa trên mã và số tiền gây tốn công nhận thức | Mức 2 | 4/7 | P1 (01:18); P2 (01:55); P5 (01:55); P7 (01:25) | Vấn đề Trải nghiệm nhận thức (Cognitive Load) |


### U01 — Lối vào lịch sử đơn qua lời chào khó nhận biết (Mức 3)

- **Thực tế quan sát:** Người tham gia gặp khó khăn khi tìm kiếm liên kết Lịch sử đơn hàng vì liên kết nằm ẩn trong menu chào hỏi người dùng trên Navbar (ghi nhận ở P3, P6).
- **Đề xuất giải pháp cải tiến:** Thêm liên kết 'Đơn hàng của tôi' rõ nghĩa và trực quan trên thanh điều hướng (Navbar).

### U02 — Tiêu đề Đăng Ký trên form đăng nhập gây nhầm (Mức 2)

- **Thực tế quan sát:** Tiêu đề trang đăng nhập hiển thị 'Đăng Ký' (BUG-001 / GUI-001) khiến người tham gia bối rối, phân vân liệu mình có bấm nhầm trang đăng ký hay không (ghi nhận ở P2, P3, P6).
- **Đề xuất giải pháp cải tiến:** Đổi tiêu đề đúng chức năng đăng nhập và thống nhất nhãn tiếng Việt.
- **Liên kết Bug Report:** [U02 liên quan đến GitHub Issue](../bug-reports/usability/U02.md) · [Ảnh minh chứng](../evidence/usability/U02.png).

### U03 — Nút Hủy xuất hiện ở đơn đang giao gây hoang mang kỳ vọng (Mức 3)

- **Thực tế quan sát:** Nút Hủy đơn hiển thị trên dòng đơn đang giao (BUG-010 / GUI-030) khiến người tham gia thắc mắc về tính đúng đắn của trạng thái đơn hàng (ghi nhận ở P1, P4).
- **Đề xuất giải pháp cải tiến:** Ẩn nút Hủy đơn đối với các đơn hàng đã ở trạng thái đang giao (shipping), đồng bộ giao diện với quy tắc nghiệp vụ.
- **Liên kết Bug Report:** [U03 liên quan đến GitHub Issue](../bug-reports/usability/U03.md) · [Ảnh minh chứng](../evidence/usability/U03.png).

### U04 — Thiếu hộp thoại xác nhận (Confirmation Modal) trước khi hủy đơn (Mức 3)

- **Thực tế quan sát:** Sau khi nhấn Hủy đơn, hệ thống kích hoạt native alert mà không có hộp thoại xác nhận trước thao tác, khiến người tham gia lo lắng vì sợ bấm nhầm không thể hoàn tác (ghi nhận ở P3, P5, P6).
- **Đề xuất giải pháp cải tiến:** Bổ sung popup/dialog xác nhận 'Bạn có chắc chắn muốn hủy đơn hàng này không?' trước khi thực thi hủy đơn.

### U05 — Nhận diện đơn hàng chỉ dựa trên mã và số tiền gây tốn công nhận thức (Mức 2)

- **Thực tế quan sát:** Bảng danh sách đơn hàng chỉ hiển thị mã đơn và số tiền mà không có tóm tắt sản phẩm, khiến người tham gia phải tốn thời gian dò tìm số tiền để đối chiếu đơn cần xử lý (ghi nhận ở P1, P2, P5, P7 theo timeline).
- **Đề xuất giải pháp cải tiến:** Hiển thị tên tóm tắt hoặc ảnh sản phẩm đại diện trong danh sách đơn hàng để người dùng dễ nhận diện.

## 5. Phân tích Chi tiết 4 Chủ đề Định tính (Probe Topics)

1. **Clarity (Độ rõ ràng):**
   - Điểm nghẽn lớn nhất nằm ở **menu điều hướng tài khoản**: Tên hiển thị người dùng `Chào, [Tên]` không có biểu tượng mũi tên xổ xuống (dropdown icon) hay chữ "Đơn hàng của tôi", khiến người dùng không nhận biết được đây là liên kết dẫn đến trang Hồ sơ & Lịch sử đơn (ghi nhận ở P3, P5, P6).
   - Form Đăng nhập hiển thị tiêu đề "Đăng Ký" (BUG-001) gây giật mình cho P2, P3, P6, khiến họ phải khựng lại kiểm tra thanh URL trước khi dám nhập mật khẩu.
2. **Recovery (Khả năng xử lý và phục hồi lỗi):**
   - Việc nhấn nút Hủy đơn lập tức gọi lệnh hủy qua hộp thoại browser alert mà không có bước xác nhận trung gian ("Bạn có chắc chắn muốn hủy không?") khiến người dùng (P3, P5, P6) rất lo ngại việc bấm nhầm sẽ không thể hoàn tác lại được.
   - Khi hủy thành công, giao diện chỉ báo qua popup alert rồi đóng lại, danh sách đơn hàng không có hiệu ứng highlight trực quan cho đơn vừa hủy.
3. **Speed (Tốc độ & Nỗ lực nhận thức):**
   - Người dùng tốn nhiều thời gian nhất ở công đoạn **so sánh số tiền** để tìm đơn hàng cần hủy (T3) do danh sách đơn không có hình ảnh thu nhỏ sản phẩm hoặc tên sản phẩm tóm tắt (P2, P4, P7).
4. **Trust (Mức độ tin cậy):**
   - Người dùng tin rằng đơn hàng đã hủy thành công chủ yếu nhờ vào việc nhìn thấy nhãn trạng thái đổi thành "Đã hủy" (màu đỏ) sau khi đóng alert.
   - Việc nút "Hủy đơn" vẫn hiển thị chình ình trên dòng đơn hàng đang ở trạng thái "Đang giao" (BUG-010) làm giảm sút nghiêm trọng niềm tin của người dùng vào tính chính xác của hệ thống quản lý trạng thái.

## 6. Đối chiếu Mục tiêu Ban đầu

| Mục tiêu | Kết luận đánh giá | Dữ liệu minh chứng |
|---|---|---|
| O1: Khả năng tìm kiếm lịch sử đơn | Lối vào qua Navbar chưa trực quan, cần cải tiến điều hướng rõ ràng. | Vấn đề U01; Cần hỗ trợ định hướng ở phiên P3, P5. |
| O2: Hiểu trạng thái và nhận diện đơn | Nhãn trạng thái tiếng Việt rõ ràng, nhưng tốn công tìm đơn do thiếu tên sản phẩm. | Đạt 100% ở T1/T2; Phát hiện vấn đề U02 và U05. |
| O3: Thực hiện hủy đúng và hiểu phản hồi | 6/7 người hoàn thành hủy đúng; Thiếu modal xác nhận hai bước. | Đạt 6/7 ở T3/T4; Phát hiện vấn đề U03 và U04. |
| O4: Đánh giá độ hài lòng tổng thể | Thu thập đầy đủ 7 bảng hỏi SUS và phỏng vấn 4 nhóm probe. | sus_responses.csv; 7 biên bản phỏng vấn chi tiết S01–S07. |

## 7. Đề xuất Lộ trình Cải tiến Sản phẩm

1. **Ưu tiên 1 (Cần xử lý ngay):**
   - Ẩn nút "Hủy đơn" đối với đơn hàng đang giao (shipping) để bảo đảm đúng logic nghiệp vụ và tránh gây hiểu lầm cho người dùng.
   - Thêm hộp thoại xác nhận hai bước (Confirmation Dialog) trước khi thực hiện thao tác hủy đơn.
2. **Ưu tiên 2 (Cải thiện điều hướng):**
   - Tách rõ ràng liên kết "Lịch sử đơn hàng" trên Navbar hoặc bổ sung icon menu tài khoản trực quan.
   - Sửa tiêu đề trang Đăng nhập từ "Đăng Ký" thành "Đăng Nhập".
3. **Ưu tiên 3 (Nâng cao trải nghiệm):**
   - Hiển thị tóm tắt tên/ảnh sản phẩm chính trong từng dòng đơn hàng để giảm tải nhận thức cho người dùng khi tra cứu.


## Nguồn và giới hạn bằng chứng

Dữ liệu do sinh viên cung cấp và xác nhận là các phiên thật do mình điều phối. Codex đối chiếu độc lập phép tính; không xác minh độc lập người tham gia. Pilot được loại khỏi thống kê. Task 2 dùng luồng quản lý đơn hàng, khác phạm vi GUI G2 của Task 1. Không có video phiên vì hồ sơ ghi người tham gia từ chối. §6 hướng dẫn ghi màn hình; §14 ghi bản quay khi có (screen recordings where available). Hồ sơ nộp ghi chú có cấu trúc và nêu rõ giới hạn không có video.


## Đối chiếu với bằng chứng tái hiện

| Mã | Severity đề xuất | Tần suất trong mẫu | GitHub Issue | Ảnh agent tái hiện |
|---|---|---|---|---|
| U01 | Major | 5/7 | https://github.com/NgBaoAnn/hw03-gui-usability/issues/24 | [Ảnh](../evidence/usability/U01.png) |
| U02 | Minor | 3/7 | https://github.com/NgBaoAnn/hw03-gui-usability/issues/25 | [Ảnh](../evidence/usability/U02.png) |
| U03 | Major | 3/7 | https://github.com/NgBaoAnn/hw03-gui-usability/issues/26 | [Ảnh](../evidence/usability/U03.png) |
| U04 | Major | 3/7 | https://github.com/NgBaoAnn/hw03-gui-usability/issues/27 | [Ảnh](../evidence/usability/U04.png) |
| U05 | Minor | 4/7 | https://github.com/NgBaoAnn/hw03-gui-usability/issues/28 | [Ảnh](../evidence/usability/U05.png) |
