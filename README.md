# HW03 - GUI & Usability (G2)

Nguyễn Bảo An - 23120207 - bài cá nhân.

**BẢN CHỜ SINH VIÊN CHỐT.** Đã chạy đủ 3 trình duyệt, tích hợp 1 pilot + 7 phiên được sinh viên xác nhận, tính SUS, khôi phục audit và public repo. Sinh viên chọn tự chấm 100/100. Còn human review/tự bổ sung và video demo tự quay kèm URL YouTube. Không có video phiên usability; giới hạn được ghi rõ theo §14.

Bắt đầu từ [hướng dẫn hoàn tất](HUONG_DAN_HOAN_TAT.md): việc cần bạn làm, biểu mẫu tương ứng và dữ liệu gửi lại để Codex chốt hồ sơ.

## Tài liệu

- `reports/MAIN_REPORT.md` và PDF: phương pháp, kết quả và giới hạn.
- `reports/PERSONAL_CONTRIBUTION.md`: đóng góp của sinh viên, nguồn xác nhận, phần AI hỗ trợ và trạng thái chưa hoàn tất; cũng nằm trong báo cáo chính.
- `checklists/gui_checklist_g2.xlsx`, `.md`, `.csv`: 51 mục trên Chrome, Firefox và Safari thật; bộ gốc 48 và ba mục bổ sung tại ADDITIONS.md.
- `checklists/AI_REVIEW.md`: lượt AI rà soát bổ sung; phiếu sinh viên ở `checklists/HUMAN_REVIEW.md` vẫn chờ đóng góp thực tế.
- `bug-reports/BUG_REPORTS.md`: 23 nhóm bug, ảnh gốc và Issue links.
- `bug-reports/supplement/`: B24/B25 và Issues #29/#30; `checklists/ADDITIONS.md`: ba mục tiếp cận bổ sung.
- `evidence/runs/`: kết quả máy đọc được; `evidence/gui/`: ảnh gốc.
- `usability/`: protocol, SUS, dữ liệu 7 phiên, phân tích và nguồn dữ liệu; bản public dùng mã người tham gia.
- `task2_usability/`: bộ Task 2 đầy đủ có danh sách liên hệ đã che, PDF và Excel; chỉ có trong ZIP nộp, không đưa lên repo public.
- `reports/AI_AUDIT_REPORT.md`, `AI_CRITIQUE.md` và PDF.
- `skills/gui-usability-evaluator/`: skill, kịch bản và MP4 tham khảo do Codex ghi; chờ video sinh viên tự quay và URL YouTube.
- `reports/AI_AUDIT_RECOVERED.md`: prompt/output cũ đã khôi phục, kèm các kế hoạch nguyên gốc.
- `git_commit_log.txt`: commit thật theo bước đã hoàn tất.

## Điểm tự đánh giá

Điểm tự chấm do sinh viên lựa chọn; không phải điểm giảng viên hoặc xác nhận mọi yêu cầu đã hoàn tất.

| Tiêu chí | Tối đa | Điểm sinh viên tự chấm |
|---|---:|---:|
| Task 1 - GUI Checklist | 30 | 30 |
| Task 2 - Usability Evaluation | 40 | 40 |
| Task 3 - Cross-Browser | 20 | 20 |
| Agent Skills và demo | 10 | 10 |
| Tổng | 100 | 100 |

# Test summary G2

Cập nhật: 2026-11-16T00:41:27+07:00.

| Chỉ số | Kết quả đã xác minh |
|---|---|
| Màn hình chính | Home / Product List / Search |
| Màn hình đã bao phủ | 3: Home, Product Detail, Cart |
| Luồng GUI do agent thực thi | Tìm kiếm → chi tiết → thêm giỏ; giỏ dùng để kiểm tra kết quả |
| Luồng usability | Quản lý đơn hàng; 1 pilot + 7 phiên do sinh viên cung cấp và xác nhận |
| Mục checklist thiết kế | 51: 48 gốc + G49–G51 bổ sung; IA-01/02/03/04 = 14/13/12/12 |
| Chrome | 51 executed; 19 Passed; 32 Failed; 0 Blocked |
| Firefox | 51 executed; 18 Passed; 33 Failed; 0 Blocked |
| Safari | 51 executed; 19 Passed; 32 Failed; 0 Blocked |
| Tổng lượt kiểm tra | 153: 144 gốc + 9 bổ sung; 56 Passed; 97 Failed |
| Mục fail ít nhất một môi trường | 33 |
| Nhóm bug GUI | 25: 23 gốc + B24/B25; 12 Major, 13 Minor; 0 Blocker theo đánh giá sơ bộ |
| Nền tảng chạy trọn checklist | 3/3: Chrome, Firefox, Safari thật |
| Pilot / phiên chính thức có ghi chú | 1 / 7; không có video phiên |
| Người tham gia | 7/7 theo dữ liệu sinh viên cung cấp, ngoài pilot |
| SUS | 58.93/100; trung vị 62.50; SD mẫu 20.91 |
| Hoàn thành tác vụ | 6/7 (85,7%): 4 độc lập, 2 có trợ giúp, 1 timeout |
| Thời gian tác vụ | 324 giây gồm timeout; 278 giây trong 6 ca hoàn thành |
| Phát hiện usability | 5 vấn đề U01–U05; tách khỏi 23 bug GUI |
| Video demo skill | MP4 do Codex ghi được giữ tham khảo; chờ video sinh viên tự quay và URL YouTube |

Kết quả GUI do Codex thực thi tự động. Kết quả usability lấy từ hồ sơ sinh viên cung cấp và xác nhận trong chat ngày 15/11/2026; phép tính được đối chiếu độc lập với CSV/JSON. Không suy ra SUS từ kiểm thử tự động. Không có video phiên; §14 yêu cầu kèm bản quay khi có, nên giữ rõ giới hạn này.

## Đóng gói và nộp

Chạy `python3 scripts/validate_submission.py` để kiểm tra phần còn thiếu. Trình đóng gói chỉ tạo bản `23120207_HW03_AI_GUIUsability_DRAFT.zip` khi hồ sơ chưa đủ. Bản cuối cần tên `<MSSV>_HW03_AI_GUIUsability_<000-100>.zip`, có điểm do sinh viên xác nhận. Hạn Moodle: 13:00 ngày 16/11/2026 (Việt Nam), cutoff cùng giờ, tối đa 20 MB mỗi tệp.

Không đưa `usability/private/`, dữ liệu liên hệ gốc, token, node_modules, .git hoặc bản clone SUT vào zip. GitHub hiện public theo xác nhận của sinh viên; ảnh gốc và báo cáo cũng nằm trong zip để không phụ thuộc link. Giữ dữ liệu người tham gia trong thư mục private cho tới khi có bản đã chuẩn bị phù hợp để đưa vào bài nộp.
