# Kế Hoạch Thực Hiện HW03 – GUI & Usability (Gói G2)

> **Mã gói:** G2 – Khám phá & Tìm kiếm Sản phẩm (Pool A: FR-05, FR-06, kết hợp FR-07)
> **Màn hình chính:** Danh sách sản phẩm & Tìm kiếm (`Product List / Search`)
> **Màn hình bổ trợ:** Trang chủ (`Home`), Chi tiết sản phẩm (`Product Detail`)
> **Flow Usability:** Tìm kiếm sản phẩm theo từ khóa → Dùng bộ lọc giá/danh mục & sắp xếp → Xem chi tiết thông số/đánh giá → Thêm vào giỏ hàng

---

## 1. Danh sách các việc cần thực hiện (Checklist Các Bước)

- [ ] **Giai đoạn 0: Khởi tạo môi trường & Git Repo**
  - Khởi tạo Git repo cục bộ trong thư mục bài làm để ghi nhận `git commit log` cho từng bước.
  - Clone mã nguồn SUT (`eshop-sut`) hoặc kiểm tra xem SUT đã chạy chưa.
  - Khởi tạo thư mục deliverables theo chuẩn nộp bài: `reports/`, `checklists/`, `usability/`, `cross-platform/`, `skills/`.

- [ ] **Giai đoạn 1: Task 1 — GUI Checklist (> 40 mục)**
  - Sinh checklist sơ bộ bằng AI prompt (ghi log vào AI Audit).
  - Phản biện & tự bổ sung các mục AI bỏ sót (accessibility, RTL, responsive breakpoint, edge cases, dark mode/state) có giải thích nguyên nhân.
  - Tổ chức đủ 4 khía cạnh: IA-01 (General UI), IA-02 (Forms), IA-03 (Navigation), IA-04 (Feedback/State).
  - Xuất bảng checklist ra Excel / Markdown.
  - Thực thi checklist trên SUT, ghi nhận Pass/Fail, mô tả lý do fail và chụp màn hình lỗi.
  - Ghi nhận các bug phát hiện lên file báo cáo và tạo mẫu GitHub Issues.

- [ ] **Giai đoạn 2: Task 2 — Usability Evaluation (7 Người dùng)**
  - Xây dựng Goal-Oriented Task Scenario (Kịch bản nhiệm vụ hướng mục tiêu).
  - Soạn bảng câu hỏi đo lường chuẩn SUS (System Usability Scale) & bộ câu hỏi mở (clarity, error recovery, speed, trust).
  - Lập biểu mẫu ghi nhận 7 người tham gia (che 4 số giữa SĐT/Zalo).
  - Mẫu ghi chép quan sát từng phiên (quan sát thời gian, điểm ma sát, phát ngôn think-aloud).
  - Bảng tổng hợp tính điểm SUS và phân tích mức độ ưu tiên lỗi (Blocker, Major, Minor).

- [ ] **Giai đoạn 3: Task 3 — Cross-Browser / Cross-Platform**
  - Chạy bộ checklist trên 3 nền tảng:
    1. Google Chrome (Desktop macOS/Windows)
    2. Mozilla Firefox hoặc Microsoft Edge (Desktop)
    3. Safari (Desktop) hoặc Chrome/Safari trên Mobile (iOS/Android / Responsive)
  - Chụp ảnh màn hình có overlay thông tin MSSV + Email sinh viên.

- [ ] **Giai đoạn 4: Task 4 — Xây dựng Agent Skill & Báo cáo**
  - Viết 1 Agent Skill (định dạng OpenCode / Claude Skill) chuyên tự động sinh GUI Checklist & kiểm toán Usability cho E-commerce.
  - Soạn kịch bản quay video demo cách chạy Agent Skill.

- [ ] **Giai đoạn 5: Hoàn thiện hồ sơ nộp bài & Báo cáo AI**
  - Viết AI Audit Report (log đầy đủ prompt, timestamp, output).
  - Viết đoạn AI Critique (200–300 từ) phản biện góc khuất/thiên kiến của AI.
  - Xuất báo cáo Markdown + PDF.
  - Xuất file `git_commit_log.txt`.
  - Soạn `README.md` kèm bảng điểm tự đánh giá.
