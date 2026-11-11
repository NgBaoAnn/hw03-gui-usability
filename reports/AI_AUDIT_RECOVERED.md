# AI Audit khôi phục - phiên lập kế hoạch 03/11/2026

Công cụ: OpenCode. Session: `ses_e5f7a3e5fffeFDT94yjVCVZLI8`. Tiêu đề: Homework requirements overview. Cấu hình model ghi trong log: `{"id":"antigravity-gemini-3.8-flash","providerID":"google","variant":"high"}`. Nguồn đọc chỉ giới hạn session gắn đúng thư mục HW03. Không xuất phiên OAuth, tài khoản, thông tin xác thực hay suy luận nội bộ.

## 1. user - 2026-11-03T15:28:03+07:00

yêu cầu của hw này là làm gì thế

## 2. assistant - 2026-11-03T15:28:22+07:00

Tóm tắt toàn bộ yêu cầu của **HW03 – GUI & Usability** (hệ thống kiểm thử là **EShop**: `https://github.com/ttbhanh/eshop-sut`):

---

### 1. Mục tiêu & Các Task chính (Thang điểm 100)

| Task | Tên nội dung | Yêu cầu trọng tâm | Điểm |
| :--- | :--- | :--- | :---: |
| **Task 1** | **GUI Checklist** | - Thiết kế checklist **> 40 mục** bao phủ 4 khía cạnh: Tiêu chuẩn UI chung (IA-01), Biểu mẫu/Forms (IA-02), Điều hướng/Navigation (IA-03), Trạng thái & Phản hồi (IA-04).<br>- Dùng AI gợi ý checklist ban đầu, sau đó tự rà soát/bổ sung các mục AI bỏ sót kèm giải thích lý do.<br>- Chạy checklist trên SUT, đánh dấu **Passed/Failed**, ghi chú lý do & chụp màn hình các mục Failed.<br>- Báo cáo bug lên **GitHub Issues** và trong báo cáo. | **30** |
| **Task 2** | **Usability Evaluation** | - Chọn 1 luồng End-to-End (E2E) khép kín (ví dụ: *Đăng ký → Thêm giỏ hàng → Áp coupon → Thanh toán*).<br>- Viết kịch bản nhiệm vụ (task scenario) hướng mục tiêu.<br>- Thực hiện **7 phiên thử nghiệm với 7 người dùng thực tế** (ngoài lớp, ưu tiên không học IT).<br>- Thu thập khảo sát chuẩn (**SUS** hoặc **UEQ-S**) + câu hỏi mở.<br>- Phân tích dữ liệu, tính điểm, phân loại điểm nghẽn/vấn đề thiết kế, xếp độ ưu tiên bug. | **40** |
| **Task 3** | **Cross-Browser / Cross-Platform** | - Kiểm thử Task 1 trên ít nhất **3 nền tảng khác nhau** (ví dụ: Chrome, Firefox, Safari/Android Chrome hoặc Expo Go cho Mobile App).<br>- Mỗi ảnh chụp bằng chứng bắt buộc phải **overlay email/MSSV sinh viên**. | **20** |
| **Task 4** | **Agent Skills** | - Xây dựng Agent Skills để tự động hóa/hỗ trợ sinh GUI checklist hoặc usability evaluation.<br>- Nộp kèm code skills và **video demo (link YouTube)**. | **10** |

---

### 2. Các yêu cầu bắt buộc kèm theo (Chống gian lận & Quy chuẩn)
1. **AI Audit Report & AI Critique (Bắt buộc):**
   - Nhật ký chi tiết mọi lần prompt AI (Công cụ, thời gian, prompt, response).
   - Đoạn văn 200–300 từ **AI Critique**: Phản biện điểm AI làm sai, góc khuất/thiên kiến của AI và bài học rút ra.
2. **Quy định chống gian lận (Anti-Cheat):**
   - Danh sách 7 người tham gia thực tế (Họ tên + SĐT/Zalo che 4 số giữa). *TA có thể gọi ngẫu nhiên 2 người để kiểm chứng.*
   - Ảnh chụp màn hình đa nền tảng phải gắn MSSV/email của bạn.
3. **Git Commit Log:**
   - Commit từng bước nhỏ (thiết kế checklist, run checklist, từng phiên usability...) và xuất ra file `git_commit_log.txt`.

---

### 3. Quy chuẩn đóng gói nộp bài
- **Tên file:** `<MSSV>_HW03_AI_GUIUsability_<ĐiểmTựĐánhGiá>.zip` (ví dụ: `23120207_HW03_AI_GUIUsability_095.zip`).
- **Nội dung bên trong:**
  - Báo cáo chính (`.md` và `.pdf`).
  - Báo cáo lỗi (link GitHub Issues + ảnh chụp).
  - Báo cáo AI Audit & AI Critique (`.md` và `.pdf`).
  - File Excel checklist (> 40 mục) + Test summary.
  - Bộ bằng chứng Usability (kịch bản, kết quả SUS/UEQ-S, danh sách 7 người, video/notes).
  - Ảnh chụp màn hình kiểm thử đa nền tảng (có overlay MSSV).
  - File `README.md` (chứa bảng điểm tự đánh giá).
  - `git_commit_log.txt`.

---
*Ghi chú: Đã tóm tắt trực tiếp từ đề bài tiếng Việt `2026.HW03.GUI Usability_Vi.md`.*

## 3. user - 2026-11-03T15:31:05+07:00

có yêu cầu là thành viên trong cùng 1 nhóm không được chọn trùng màn hình chính với flow, có yêu cầu này ko

## 4. assistant - 2026-11-03T15:31:05+07:00

**Có, hoàn toàn chính xác.** 

Yêu cầu này được quy định rõ tại **Mục 5 (Lựa chọn phạm vi kiểm thử - Scope Selection)** trong file đề bài `2026.HW03.GUI Usability_Vi.md` (dòng 88–89):

> **Quy tắc phân công nhóm:** Trong mỗi nhóm, hãy đảm bảo rằng lựa chọn của bạn không bị trùng lặp giữa các thành viên: **không có hai thành viên nào được chọn cùng một màn hình chính cho GUI checklist hoặc cùng một luồng usability**.

Tóm lại:
- **GUI Checklist (Task 1):** Các bạn trong cùng nhóm không được chọn cùng màn hình chính (ví dụ: người chọn Home/Product List thì người khác phải chọn Cart, Checkout, hoặc Admin Dashboard, v.v.).
- **Usability Evaluation (Task 2):** Các bạn trong nhóm không được chọn trùng luồng End-to-End (E2E flow).

---
*Ghi chú: Cần trao đổi và thống nhất màn hình/flow với các bạn trong nhóm trước khi bắt đầu làm để tránh bị trùng.*

## 5. user - 2026-11-03T15:35:55+07:00

tôi chọn G2 
# HW03 – Đăng ký màn hình & flow (tránh trùng)

> Theo đề §5: trong nhóm, **không ai được trùng màn hình chính** (GUI checklist) **hoặc trùng flow** (usability).
> Màn hình **phụ** được phép trùng.
> Bài làm cá nhân — mỗi người tự làm checklist, tự tuyển **7 người tham gia riêng** (không dùng chung người).

## Cách đăng ký
1. Chọn **1 gói** bên dưới (ai đăng ký trước được trước).
2. Ghi tên vào bảng đăng ký cuối file và gửi lại nhóm.
3. Muốn đề xuất gói khác → ghi vào mục "Gói tự đề xuất", nhưng không được trùng màn hình chính / tính năng trọng tâm của flow với gói đã có người.
4. Hạn chốt: **<ngày/giờ>**. Sau khi chốt không đổi (vì log AI và git commit có thời gian).

## Các gói

| Gói | Màn hình chính (Task 1) | Màn hình phụ gợi ý | Flow usability (Task 2) | FR liên quan |
|---|---|---|---|---|
| **G1 – Tài khoản** | Login / Register | Forgot password, Profile | Đăng ký tài khoản → đăng nhập sai bị khóa → khôi phục mật khẩu → cập nhật hồ sơ | FR-01→04 |
| **G2 – Tìm & xem sản phẩm** | Product List / Search | Home, Product Detail | Tìm sản phẩm theo nhu cầu & mức giá → so sánh → thêm vào giỏ | FR-05, 06, 07 |
| **G3 – Thanh toán** | Checkout | Cart, Order History | Giỏ hàng có sẵn → checkout dùng mã giảm giá → kiểm tra đơn trong lịch sử | FR-07→11 |
| **G4 – Quản trị** | Admin Dashboard / Product CRUD | Category, Coupon, CSV import | Admin tạo mã giảm giá mới → sửa giá sản phẩm → xem đơn hàng | FR-12→19 |
| **G5 – Mobile** | Màn hình chính trên Mobile app (Expo) | Product, Cart trên mobile | Mua 1 sản phẩm hoàn chỉnh trên điện thoại | Pool D |

> Nhóm ít hơn 5 người thì bỏ bớt gói, không cần ghép.
> Gói G4 cần người tham gia "đóng vai admin" → nên tìm người từng bán hàng online / quản lý shop.

## Bảng đăng ký

| Thành viên | MSSV | Gói | Màn hình chính | Flow (ghi rõ) | Nền tảng Task 3 (≥3) |
|---|---|---|---|---|---|
| Nguyễn Lê Thế Vinh | 23120190 | G1 – Tài khoản | Login / Register | Đăng ký tài khoản → đăng nhập sai bị khóa → khôi phục mật khẩu → cập nhật hồ sơ |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Gói tự đề xuất (nếu có)

| Thành viên | Màn hình chính | Flow | Khác các gói trên ở điểm nào |
|---|---|---|---|
|  |  |  |  |

## Lưu ý chung
- **Không dùng chung prompt** — chép prompt giữa các bạn là 0 điểm cả hai.
- **Không dùng chung người tham gia** — TA gọi kiểm tra 2 người, trùng sẽ dễ bị nghi.
- Chụp lại bảng đã chốt, mỗi người đưa vào phần *Scope* trong report của mình. 

## 6. assistant - 2026-11-03T15:36:03+07:00

Dòng đăng ký của bạn cho bảng nhóm (bạn điền thông tin MSSV, họ tên và chọn 3 nền tảng kiểm thử cho Task 3):

```markdown
| Nguyễn Bảo An | <MSSV_CỦA_BẠN> | G2 – Tìm & xem sản phẩm | Product List / Search (kèm Home, Product Detail) | Tìm sản phẩm theo nhu cầu & mức giá → xem chi tiết/so sánh → thêm vào giỏ | Chrome (Desktop), Firefox (Desktop), Safari / Edge (hoặc Android Chrome) |
```

---

### Tóm tắt phạm vi công việc gói G2 của bạn:

1. **Task 1 — GUI Checklist (> 40 mục):**
   - **Màn hình trọng tâm:** Trang danh sách sản phẩm & tìm kiếm / lọc (`Product List / Search`), kết hợp màn hình Trang chủ (`Home`) và Chi tiết sản phẩm (`Product Detail`).
   - **Bao phủ 4 khía cạnh:**
     - **IA-01 (General UI):** Typography, màu sắc, khoảng cách (spacing), bố cục grid sản phẩm, responsive, hình ảnh sản phẩm vỡ/placeholder.
     - **IA-02 (Forms):** Thanh tìm kiếm (search input), bộ lọc giá (slider/min-max input), dropdown sắp xếp, chọn số lượng (quantity selector).
     - **IA-03 (Navigation):** Phân trang (pagination / infinite scroll), breadcrumbs (`Trang chủ > Danh mục > Sản phẩm`), click vào card sản phẩm chuyển trang, nút quay lại.
     - **IA-04 (Feedback/State):** Trạng thái tải (skeleton/spinner khi tìm kiếm), trạng thái rỗng ("Không tìm thấy sản phẩm phù hợp"), thông báo toast khi bấm "Thêm vào giỏ", trạng thái hết hàng (Out of Stock badge).

2. **Task 2 — Usability Evaluation (7 người dùng):**
   - **Kịch bản mục tiêu (Goal-oriented scenario):** *"Bạn cần tìm một chiếc tai nghe không dây màu đen có giá dưới 500.000 ₫, xem thông tin bảo hành của sản phẩm đó rồi thêm vào giỏ hàng."*
   - Thu thập kết quả khảo sát qua bảng câu hỏi **SUS** hoặc **UEQ-S**, ghi lại thời gian hoàn thành, các điểm nghẽn (khó tìm bộ lọc, không rõ sản phẩm còn hàng hay không,...) và phân tích.

3. **Task 3 — Cross-Browser / Cross-Platform:**
   - Thực thi checklist trên 3 trình duyệt/môi trường (ví dụ: Google Chrome, Mozilla Firefox, và Microsoft Edge / Apple Safari hoặc Chrome trên Mobile) có overlay email/MSSV.

---
*Ghi chú: Bạn chỉ cần thay `<MSSV_CỦA_BẠN>` và chốt 3 trình duyệt/nền tảng muốn dùng rồi gửi dòng trên vào bảng đăng ký chung của nhóm.*

## 7. user - 2026-11-03T15:41:01+07:00

tôi thấy yêu cầu 3 là phải test trên cross platform, mà g5 lại là mobile là sai rồi, tôi muốn chia 5 phần là 5 module của app và phải test cross platform như yêu cầu 

## 8. assistant - 2026-11-03T15:41:02+07:00

Nhận định của bạn **rất chính xác**. 

Đề bài mục §6 (Task 3) nêu rõ:
> **Task 3 — Cross-Browser / Cross-Platform:**
> - Thực hiện Task 1 trên ít nhất **ba (3) nền tảng khác nhau**.
> - Bao phủ web frontend trên **Chrome, Firefox, và Safari** (hoặc Android Chrome / Expo Go).

Điều đó có nghĩa: **Cross-platform/Cross-browser là yêu cầu bắt buộc cho TẤT CẢ mọi người trong Task 3**, chứ không phải là một module riêng biệt. Nếu để riêng "G5 - Mobile" thì bạn làm G5 sẽ bị lẫn lộn giữa việc chọn scope màn hình với yêu cầu nền tảng của Task 3.

Ứng dụng SUT (EShop) gồm 3 Pool chức năng rõ rệt (Pool A, Pool B, Pool C). Để chia đều cho **5 thành viên**, mỗi người phụ trách **1 module nghiệp vụ rõ ràng** (có màn hình chính + màn hình phụ + flow E2E), và **ai cũng phải test module của mình trên ≥ 3 nền tảng** (Task 3):

---

### Bảng 5 gói đề xuất mới theo 5 Module chức năng

| Gói | Module chức năng | Màn hình chính (Task 1) | Màn hình phụ kèm theo | Flow Usability (Task 2) | FR liên quan |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **G1** | **Xác thực & Tài khoản** | Đăng ký & Đăng nhập (`Register / Login`) | Quên mật khẩu, Hồ sơ cá nhân (`Profile`) | Đăng ký tài khoản mới → Đăng nhập sai quá số lần bị khóa → Quên & reset mật khẩu → Đăng nhập thành công và cập nhật thông tin cá nhân | FR-01, FR-02, FR-03, FR-04 |
| **G2** | **Khám phá & Tìm kiếm Sản phẩm** | Danh sách sản phẩm & Tìm kiếm (`Product List / Search`) | Trang chủ (`Home`), Chi tiết sản phẩm (`Product Detail`) | Tìm kiếm sản phẩm theo từ khóa → Dùng bộ lọc (giá, danh mục) & sắp xếp → Xem chi tiết thông số/đánh giá → Thêm vào giỏ hàng | FR-05, FR-06 |
| **G3** | **Giỏ hàng & Đặt hàng / Thanh toán** | Thanh toán (`Checkout`) | Giỏ hàng (`Cart`), Xác nhận đơn hàng | Kiểm tra giỏ hàng (sửa số lượng/xóa) → Tiến hành Checkout → Nhập địa chỉ & chọn phương thức vận chuyển/thanh toán → Áp mã giảm giá → Hoàn tất đặt hàng | FR-07, FR-08, FR-09 |
| **G4** | **Lịch sử & Theo dõi Đơn hàng** | Lịch sử đơn hàng (`Order History`) | Chi tiết đơn hàng (`Order Details`), Trạng thái đơn (`Order Tracking`) | Đăng nhập → Truy cập lịch sử đơn hàng → Lọc/tìm đơn hàng cũ → Xem chi tiết & theo dõi tiến trình trạng thái đơn hàng (đang giao/hoàn tất) → Yêu cầu hủy/đổi trả (nếu có) | FR-10, FR-11 |
| **G5** | **Quản trị Admin** | Bảng điều khiển (`Admin Dashboard`) | Quản lý sản phẩm & Danh mục CRUD, Quản lý đơn hàng/Coupon | Đăng nhập Admin → Xem thống kê Dashboard → Tạo sản phẩm mới (hoặc import CSV) / tạo mã coupon → Kiểm tra danh sách đơn hàng cần xử lý | FR-12 đến FR-19 |

---

### Bảng đăng ký sửa lại gửi cho nhóm:

```markdown
# HW03 – Đăng ký màn hình & flow (tránh trùng)

> Theo đề §5 & §6: 
> - Mỗi thành viên phụ trách **1 module độc lập** (không trùng màn hình chính và flow usability).
> - **Task 3 là bắt buộc với tất cả mọi người**: Mỗi người tự thực thi checklist của gói mình trên **ít nhất 3 nền tảng khác nhau** (ví dụ: Chrome Desktop, Firefox Desktop, Safari/Edge hoặc Mobile Web/Expo Go).
> - Mỗi người tự tuyển **7 người tham gia usability riêng**.

## Bảng đăng ký

| Thành viên | MSSV | Gói | Màn hình chính | Flow Usability (Task 2) | 3 Nền tảng Task 3 (Dự kiến) |
|---|---|---|---|---|---|
| Nguyễn Lê Thế Vinh | 23120190 | G1 – Xác thực & Tài khoản | Register / Login | Đăng ký → Khóa tài khoản do nhập sai → Quên MK → Cập nhật Profile | Chrome, Firefox, Safari |
| Nguyễn Bảo An | <MSSV> | G2 – Khám phá & Tìm kiếm | Product List / Search | Tìm kiếm → Lọc giá/danh mục → Xem chi tiết → Thêm vào giỏ | Chrome (PC), Firefox (PC), Safari (hoặc Mobile) |
|  |  | G3 – Giỏ hàng & Thanh toán | Checkout / Cart | Giỏ hàng → Áp coupon → Điền địa chỉ & thanh toán → Xác nhận đơn |  |
|  |  | G4 – Quản lý Đơn hàng | Order History / Tracking | Xem lịch sử đơn → Tìm kiếm/lọc đơn → Xem tiến trình đơn hàng |  |
|  |  | G5 – Quản trị Admin | Admin Dashboard | Đăng nhập Admin → Xem thống kê → Thêm sản phẩm/coupon → Xử lý đơn |  |
```

Cách phân chia này giúp:
1. Đúng chuẩn 5 module tách biệt, không ai giẫm chân ai.
2. Đúng tinh thần đề bài: Task 3 (Cross-platform) là kỹ thuật kiểm thử áp dụng cho từng module, chứ không phải một gói bài tập riêng.

---
*Ghi chú: Đã loại bỏ gói mobile riêng lẻ và thay bằng module Lịch sử/Quản lý đơn hàng người dùng (FR-10, FR-11).*

## 9. user - 2026-11-03T15:44:40+07:00

oke tôi chọn G2, giờ thực hiện thôi nào

## 10. assistant - 2026-11-03T15:45:32+07:00

Tôi đã khởi tạo xong kế hoạch và cấu trúc thư mục bài làm cho **Gói G2**:

1. **Đã lập kế hoạch chi tiết (`PLAN_G2.md`)** bám sát 100% barem điểm:
   - **Task 1 (30đ):** GUI Checklist > 40 items cho màn hình Tìm kiếm/Lọc & Chi tiết sản phẩm (IA-01 → IA-04), phản biện phần AI bỏ sót, chạy test, bắt bug.
   - **Task 2 (40đ):** Thiết kế kịch bản Usability E2E, bảng đo chuẩn **SUS**, chuẩn bị khảo sát 7 người dùng thực tế, phân tích dữ liệu.
   - **Task 3 (20đ):** Kiểm thử trên 3 trình duyệt/môi trường (Chrome, Firefox, Safari/Mobile) kèm overlay MSSV.
   - **Task 4 (10đ):** Viết Agent Skill chuyên dụng + kịch bản video demo.
   - **Tài liệu bắt buộc:** AI Audit Log, AI Critique (200–300 từ), Git log, README tự đánh giá.
2. **Đã khởi tạo Git repository** và tạo commit đầu tiên để theo dõi log quá trình làm việc (`git_commit_log.txt`).
3. **Đã tạo sẵn khung thư mục:** `reports/`, `checklists/`, `usability/`, `cross-platform/`, `skills/`, `bug-reports/`.

---

### Bước tiếp theo:
1. Bạn cho mình biết **Họ và tên + MSSV** của bạn để mình cấu hình chuẩn vào các template báo cáo và ảnh chụp overlay.
2. Bạn đã clone/chạy mã nguồn SUT (`eshop-sut`: https://github.com/ttbhanh/eshop-sut) ở máy chưa, hay cần mình hỗ trợ clone và khởi chạy SUT lên localhost trước?

---
*Ghi chú: Đã commit Git bước khởi tạo dự án và tạo sẵn cây thư mục nộp bài.*

## 11. user - 2026-11-03T16:03:01+07:00

lên kế hoạch thực hiện hw trên, phần nào AI làm dc thì AI làm, phần nào cần tôi làm thì phải để tôi làm

## 12. assistant - 2026-11-03T16:03:45+07:00

Kế hoạch phân định rõ ràng giữa **phần AI làm** và **phần Bạn làm** (vừa được commit vào git repo tại file `KE_HOACH_CHI_TIET.md`):

---

### Tóm tắt cốt lõi:

| Bạn làm (Bắt buộc theo Anti-Cheat & Chấm điểm) | AI làm (Trợ lý tự động hóa & Tài liệu) |
| :--- | :--- |
| 1. **Khởi chạy SUT EShop trên máy** (để có môi trường test thực tế). | 1. **Soạn toàn bộ GUI Checklist > 40 mục** (IA-01 → IA-04) + xuất Excel & Markdown. |
| 2. **Chạy checklist trên SUT**: Bấm thực tế, tick Pass/Fail, chụp ảnh các mục Fail. | 2. **Viết kịch bản nhiệm vụ Usability** + Tạo sẵn Form đo lường chuẩn **SUS** & câu hỏi mở. |
| 3. **Tiến hành 7 phiên Usability với 7 người thật**: Lấy thông tin (Họ tên + SĐT che 4 số), ghi nhận điểm SUS. | 3. **Tính toán số liệu Usability**: Tính điểm SUS trung bình, phân loại điểm nghẽn (Blocker/Major/Minor). |
| 4. **Chụp ảnh 3 trình duyệt** (Chrome, Firefox, Safari/Mobile) có **overlay MSSV/Tên**. | 4. **Soạn sẵn mẫu Bug Reports** chuẩn chỉnh để tạo GitHub Issues. |
| 5. **Quay 1 video demo ngắn (3-5 phút)** chạy Agent Skill up YouTube. | 5. **Viết code Agent Skill hoàn chỉnh** (chuẩn OpenCode skill). |
| 6. **Nộp file zip lên Moodle**. | 6. **Viết trọn bộ Báo cáo**, AI Audit Log, AI Critique (200-300 từ), xuất PDF, xuất git log và README tự đánh giá. |

---

### Bắt đầu ngay Bước 1:
Tôi sẽ tiến hành **sinh bộ GUI Checklist > 40 mục** cho gói G2 (Product List / Search & Detail) và **soạn sẵn kịch bản Usability + Form SUS**. 

Cho tôi biết thêm:
1. **Họ tên & MSSV của bạn** (để điền chính xác vào tài liệu và template).
2. Ứng dụng SUT EShop bạn đã chạy lên chưa, hoặc cần tôi clone mã nguồn SUT vào thư mục để kiểm tra trước không?

---
*Ghi chú: Đã cập nhật và commit bảng phân chia trách nhiệm vào `KE_HOACH_CHI_TIET.md`.*

## 13. user - 2026-11-03T16:08:07+07:00

sử dụng @writing-plans để tạo plan

## 14. assistant - 2026-11-03T16:08:47+07:00

Plan complete and saved to `docs/superpowers/plans/2026-11-03-gui-usability-g2.md`. 

Please review the plan. Which execution approach would you prefer?

- **Subagent-driven** - A fresh subagent implements each task and a fresh reviewer checks it before the next one starts, then a whole-branch review at the end. Most thorough; costs a fresh context per task and per review.
- **Native** - I implement every task myself in this session, the way this harness runs work, then one fresh reviewer on the most capable model checks the whole branch. Cheapest and fastest; no independent review until the end. Runs well with a mid-tier session model, since the plan carries the design.

For this plan I recommend **Native**, because the tasks are tightly structured deliverables (checklists, scripts, questionnaires, templates, and reports) that directly build on top of each other within this single workspace.

Does the plan capture what you want, and which approach should we use?

---
*Ghi chú: Bản kế hoạch chi tiết 8 Task đã được lưu và commit tại `docs/superpowers/plans/2026-11-03-gui-usability-g2.md`.*

## Đầu ra nguyên gốc của các lần lập kế hoạch

Các bản kế hoạch dưới đây được giữ như đầu ra AI ban đầu để kiểm toán, kể cả những giả định đã được sửa trong báo cáo hiện tại. Không dùng chúng thay cho kết quả chạy thật.

- [PLAN_G2.md](legacy/PLAN_G2.md); SHA-256 `3dfdb23d0437323c77e71dd75858c8dd44d1fe7e5530de93e053ef75409a54e8`.
- [KE_HOACH_CHI_TIET.md](legacy/KE_HOACH_CHI_TIET.md); SHA-256 `f43d811330a3a6839aa948ec5babc3fbdd72308e00667096cf932ac8a43b1c13`.
- [2026-11-03-gui-usability-g2.md](legacy/2026-11-03-gui-usability-g2.md); SHA-256 `f57e86a645cafea5fe946cbb4a7287bd199268c85d057f177877000766a9fe49`.