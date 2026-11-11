# HW03 - GUI & Usability (G2)

Nguyễn Bảo An - 23120207 - bài cá nhân.

**BẢN NHÁP, CHƯA PHẢI BÀI NỘP HOÀN CHỈNH.** Đã chạy đủ 3 trình duyệt. Còn thiếu pilot/7 phiên thật, human review/tự bổ sung, demo YouTube và điểm tự chấm. Không nộp bản này như bài đã hoàn tất.

## Tài liệu

- `reports/MAIN_REPORT.md` và PDF: phương pháp, kết quả và giới hạn.
- `checklists/gui_checklist_g2.xlsx`, `.md`, `.csv`: 48 mục trên Chrome, Firefox và Safari thật.
- `bug-reports/BUG_REPORTS.md`: 23 nhóm bug, ảnh gốc và Issue links.
- `evidence/runs/`: kết quả máy đọc được; `evidence/gui/`: ảnh gốc.
- `usability/`: protocol, SUS, CSV và mẫu phiên trống để thu dữ liệu thật.
- `reports/AI_AUDIT_REPORT.md`, `AI_CRITIQUE.md` và PDF.
- `skills/gui-usability-evaluator/`: skill và kịch bản demo chưa quay.
- `git_commit_log.txt`: commit thật theo bước đã hoàn tất.

## Điểm tự đánh giá

Sinh viên chưa tự chấm. Không điền 000 thay cho điểm còn thiếu.

| Tiêu chí | Tối đa | Điểm sinh viên tự chấm |
|---|---:|---|
| Task 1 - GUI Checklist | 30 | Chưa chấm |
| Task 2 - Usability Evaluation | 40 | Chưa chấm |
| Task 3 - Cross-Browser | 20 | Chưa chấm |
| Agent Skills và demo | 10 | Chưa chấm |
| Tổng | 100 | Chưa chấm |

# Test summary G2

Cập nhật: 2026-11-11T23:05:27+07:00.

| Chỉ số | Kết quả đã xác minh |
|---|---|
| Màn hình chính | Home / Product List / Search |
| Màn hình đã bao phủ | 3: Home, Product Detail, Cart |
| Luồng GUI do agent thực thi | Tìm kiếm → chi tiết → thêm giỏ; giỏ dùng để kiểm tra kết quả |
| Luồng usability đã thiết kế / chạy với người thật | 1 / 0 |
| Mục checklist thiết kế | 48; mỗi IA 12 mục |
| Chrome | 48 executed; 19 Passed; 29 Failed; 0 Blocked |
| Firefox | 48 executed; 18 Passed; 30 Failed; 0 Blocked |
| Safari | 48 executed; 19 Passed; 29 Failed; 0 Blocked |
| Tổng lượt kiểm tra | 144; 56 Passed; 88 Failed |
| Mục fail ít nhất một môi trường | 30 |
| Nhóm bug | 23; 10 Major; 13 Minor; 0 Blocker theo đánh giá sơ bộ |
| Nền tảng chạy trọn checklist | 3/3: Chrome, Firefox, Safari thật |
| Pilot / phiên chính thức có bằng chứng | 0 / 0 |
| Người tham gia thật | 0/7 |
| SUS | Chưa có dữ liệu để tính |
| Video demo skill | Chưa quay, chưa có YouTube URL |

Kết quả là thực thi tự động bởi Codex, chưa phải xác nhận của sinh viên. Không dùng số bug hay số lượt tự động để suy ra mức hài lòng, tần suất lỗi ở người dùng, hoặc SUS.

## Đóng gói và nộp

Chạy `python3 scripts/validate_submission.py` để kiểm tra phần còn thiếu. Trình đóng gói chỉ tạo bản `23120207_HW03_AI_GUIUsability_DRAFT.zip` khi hồ sơ chưa đủ. Bản cuối cần tên `<MSSV>_HW03_AI_GUIUsability_<000-100>.zip`, có điểm do sinh viên xác nhận. Hạn Moodle: 13:00 ngày 16/11/2026 (Việt Nam), cutoff cùng giờ, tối đa 20 MB mỗi tệp.

Không đưa `usability/private/`, dữ liệu liên hệ gốc, token, node_modules, .git hoặc bản clone SUT vào zip. GitHub hiện private; các ảnh gốc và báo cáo cũng nằm trong zip để không phụ thuộc link.
