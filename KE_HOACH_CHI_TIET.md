# KẾ HOẠCH THỰC HIỆN HW03 (GÓI G2) & PHÂN ĐỊNH TRÁCH NHIỆM AI vs BẠN

> **Nguyên tắc cốt lõi (Theo Điều 2 & 11 của đề):**
> - **AI đóng vai trò:** Trợ lý có kỷ luật (AI Assistant) — sinh khung, thiết kế biểu mẫu, viết mã Agent Skill, tính toán thống kê tự động, phân tích dữ liệu sơ bộ, soạn tài liệu Markdown & xuất PDF.
> - **Bạn (Sinh viên) đóng vai trò:** Chủ thể kiểm thử & phản biện (Human Evaluator) — chạy thực tế trên máy, chụp ảnh màn hình có MSSV, tuyển 7 người dùng thực tế và điều phối phiên, xác nhận lỗi, quay video demo skill.

---

## BẢNG PHÂN CHIA TRÁCH NHIỆM CHI TIẾT (AI vs BẠN)

| STT | Nhiệm vụ / Hạng mục | Phần AI thực hiện (Tự động hóa) | Phần BẠN cần thực hiện (Người thật - Bắt buộc) |
| :---: | :--- | :--- | :--- |
| **0** | **Chuẩn bị môi trường & SUT** | Hỗ trợ clone git `eshop-sut`, kiểm tra mã nguồn, hỗ trợ lệnh chạy backend/frontend. | Chạy dự án `eshop-sut` trên máy (localhost:3000 hoặc port chỉ định). |
| **1** | **Task 1: GUI Checklist (>40 items)** | - Thiết kế checklist ban đầu đủ 4 khía cạnh: IA-01, IA-02, IA-03, IA-04.<br>- Soạn phần AI Critique chỉ ra AI hay bỏ sót gì (RTL, Dark Mode, Screen reader, Broken image fallback,...).<br>- Tạo file checklist Excel (`.xlsx`) và Markdown. | - Xem lại checklist, thêm/bớt nếu muốn.<br>- **Mở trình duyệt lên SUT**: Bấm test từng item, xác nhận Pass / Fail.<br>- Chụp ảnh màn hình đối với các mục Fail. |
| **2** | **Task 1: Bug Reports & GitHub Issues** | Soạn sẵn template Bug Report chuẩn công nghiệp (Title, Steps to Reproduce, Expected, Actual, Severity, Environment) dạng Markdown cho từng lỗi bạn tìm thấy. | Copy bug lên **GitHub Issues** của repo bài làm hoặc repo SUT cá nhân, dán kèm ảnh chụp màn hình bằng chứng. |
| **3** | **Task 2: Kế hoạch Usability & Kịch bản** | - Viết Task Scenario hướng mục tiêu (không spoil cách bấm).<br>- Thiết kế Form khảo sát chuẩn SUS (10 câu hỏi chuẩn) + 4 câu hỏi mở (Clarity, Error Recovery, Speed, Trust).<br>- Lập sẵn template ghi chép phiên (observation notes sheet). | - Đọc qua kịch bản, hiểu luồng test.<br>- Chạy 1 buổi pilot thử nghiệm để kiểm tra thời lượng. |
| **4** | **Task 2: Thực hiện 7 phiên Usability** | Chuẩn bị form Google Forms / file khảo sát để bạn gửi người dùng điền hoặc bạn ghi lại nhanh. | **BẮT BUỘC BẠN LÀM (Anti-Cheat):**<br>- Tuyển 7 người thật ngoài lớp (bạn bè, người quen).<br>- Điều hành 7 buổi test (ngồi cùng hoặc qua Google Meet), nhắc họ "think-aloud".<br>- Ghi nhận Họ tên + SĐT/Zalo (che 4 số giữa). *(TA sẽ gọi xác minh ngẫu nhiên 2 người)*.<br>- Cho họ chấm điểm SUS và trả lời câu hỏi mở. |
| **5** | **Task 2: Phân tích kết quả Usability** | - Nhận dữ liệu điểm từ bạn để tự động tính điểm SUS trung bình theo công thức chuẩn.<br>- Phân loại điểm nghẽn (Friction points) theo Blocker / Major / Minor.<br>- Tổng hợp báo cáo phân tích usability hoàn chỉnh. | Cung cấp kết quả điểm số/ghi chép từ 7 phiên thực tế cho AI. |
| **6** | **Task 3: Cross-Browser / Cross-Platform** | Hướng dẫn danh sách các điểm UI nhạy cảm cần soi kỹ giữa các trình duyệt (Chrome, Firefox, Safari/Mobile viewport). | **BẮT BUỘC BẠN LÀM:**<br>- Mở SUT trên ít nhất 3 môi trường (VD: Chrome, Firefox, Safari hoặc Mobile view/Expo Go).<br>- Chụp ảnh màn hình có **overlay Tên + MSSV** (hoặc hiển thị thanh URL localhost + email đăng nhập). |
| **7** | **Task 4: Agent Skill & Video Demo** | **Viết mã Agent Skill hoàn chỉnh** (theo cấu trúc OpenCode / Claude Skill) chuyên tự động sinh GUI checklist và phân tích usability kịch bản E-commerce. | - Tải skill vào agent / OpenCode kiểm tra thử.<br>- **Quay màn hình 1 video ngắn (3-5 phút)** demo cách gọi skill và chạy trên 1 màn hình.<br>- Upload lên YouTube (Unlisted) và gửi link cho AI chèn vào báo cáo. |
| **8** | **AI Audit Report & AI Critique** | Tự động ghi nhận toàn bộ log prompts, thời gian, mô hình và soạn bài viết phản biện AI (AI Critique 200–300 từ) chuẩn yêu cầu. | Đọc lại, ký tên xác nhận theo mẫu `AI Disclosure Form`. |
| **9** | **Đóng gói nộp bài** | - Tự động render toàn bộ báo cáo ra Markdown và chuyển đổi sang PDF.<br>- Xuất file `git_commit_log.txt`.<br>- Tạo file `README.md` kèm bảng điểm tự đánh giá (Self-assessment). | Nén file `.zip` theo đúng định dạng `<MSSV>_HW03_AI_GUIUsability_<Điểm>.zip` và nộp lên Moodle. |

---

## LỘ TRÌNH 5 BƯỚC THỰC HIỆN TỐI ƯU THỜI GIAN

```
[Bước 1: Ngay bây giờ]
AI sinh GUI Checklist (>40 items) + File Excel + Kịch bản Usability + Form SUS.
---------------------------------------------------------------------------------
[Bước 2: Cần máy SUT của bạn]
Bạn khởi chạy SUT -> Chạy checklist (xác nhận Pass/Fail) -> Chụp vài ảnh lỗi Fail.
Chụp ảnh trên 3 trình duyệt (có overlay MSSV).
---------------------------------------------------------------------------------
[Bước 3: Thu thập Usability]
Bạn cho 7 người quen thực hiện kịch bản & điền điểm SUS (15-20p mỗi người).
---------------------------------------------------------------------------------
[Bước 4: AI xây dựng Agent Skill & Báo cáo]
AI viết Agent Skill hoàn chỉnh.
Bạn quay video demo 3 phút upload YouTube lấy link.
---------------------------------------------------------------------------------
[Bước 5: Tổng hợp & Đóng gói]
AI hoàn thiện trọn bộ báo cáo, AI Audit, AI Critique, file zip đúng chuẩn.
```

---
*Ghi chú: Bản kế hoạch đã được lưu vào hệ thống để theo dõi xuyên suốt quá trình làm bài.*