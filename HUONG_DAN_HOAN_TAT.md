# Hồ sơ chuẩn bị nộp HW03 – 23120207

Video sinh viên đã cung cấp: https://youtu.be/VGVm_V7L_ks (10:38), phát được không đăng nhập. Skill đúng bản dùng trong video và tài nguyên ở `skills/gui-usability-evaluator/demo-version/`; transcript và ảnh gốc đã kèm.

Báo cáo chính MD/PDF, Excel 51 mục/153 kết quả trên ba browser, 25 nhóm bug G2, Task 2 (1 pilot + 7 phiên, SUS 58,93), năm finding usability, ba phát hiện mới từ demo, Issues, ảnh, audit/critique MD/PDF, Git log, danh sách liên hệ đã che và điểm tự chấm 100 đều được đóng vào `23120207_HW03_AI_GUIUsability_100.zip`.

## Giới hạn còn ghi trong bài

Sinh viên giao AI tự làm phần phản biện/bổ sung. AI đã làm đầy đủ phần được giao, nhưng việc này chưa chứng minh sinh viên tự rà soát/tự bổ sung như §2 và Task 1 yêu cầu; xem `checklists/HUMAN_REVIEW.md`. Không tự tạo lời xác nhận hoặc đổi tác giả G49–G51. Các phiên usability không có bản quay; dữ liệu do sinh viên cung cấp/xác nhận, không xác minh độc lập danh tính. Các phiên được nhập cùng lúc, chưa có commit tại thời điểm từng phiên. Những giới hạn này có thể ảnh hưởng điểm, dù tự chấm 100.

## Kiểm tra và nộp

`python3 scripts/validate_submission.py` kiểm tra file/bằng chứng và báo rõ yêu cầu chưa có xác nhận. `python3 scripts/package_draft.py --submission` đóng gói theo tên bắt buộc và giữ giới hạn trong SUBMISSION_STATUS.json. Tên file không chứng nhận đã đạt 100 điểm.

Moodle: https://courses.fit.hcmus.edu.vn/mod/assign/view.php?id=129903 ; assignment 40418, hạn/cutoff 13:00 ngày 16/11/2026 Việt Nam, tối đa 20 MB/tệp. Trước thao tác ghi, người dùng duyệt preview cụ thể của CLI, gồm file ZIP và lời cam kết tác giả. Sau thao tác cần kiểm tra trạng thái Submitted và tùy chọn “Em làm một mình” trên Moodle; file xuất hiện chưa tự chứng minh đã nộp cuối.
