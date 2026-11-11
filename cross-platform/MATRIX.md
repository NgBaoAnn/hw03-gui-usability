# Ma trận cross-browser

Đã thực thi đầy đủ trên 2 môi trường. Chưa đủ yêu cầu 3 nền tảng. Viewport 390×844 là kiểm tra responsive trong cùng browser, không tính thêm nền tảng.

| Môi trường | Số mục | Passed | Failed | Blocked |
|---|---:|---:|---:|---:|
| Google Chrome 157.0.8103.50 / macOS 26.2 (Darwin 25.2.0) | 48 | 19 | 29 | 0 |
| Firefox (Playwright build) 153.0 / macOS 26.2 (Darwin 25.2.0) | 48 | 18 | 30 | 0 |
| Safari hoặc Android Chrome thật | Chưa chạy trọn bộ | Chưa có | Chưa có | Chưa có |

Khác biệt: G09 Passed trên Chrome, Failed trên Firefox (398px/390px). Những Failed còn lại trùng nhau ở hai môi trường.

Ảnh chụp dùng chú thích có email, MSSV, họ tên, browser/version, OS, URL và timestamp. Chú thích được thêm sau phép đo, không dùng nó làm bằng chứng về nội dung SUT. Ảnh DOM/alt và số liệu viewport cần đọc kèm JSON; screenshot không tự chứng minh thuộc tính ẩn.

Để đóng Task 3: thực thi cả 48 mục trên Safari/Android Chrome thật, chụp riêng Failed với định danh. Không đổi nhãn WebKit thành Safari.

## Safari thật: kiểm tra nhanh, chưa đủ checklist

Safari 26.2, macOS 26.2. Đã quan sát 9 mục qua native UI/CUA trong iframe cùng origin. Chú thích bên ngoài iframe không thay đổi logic SUT. Không cộng các mục này vào thống kê hai lượt chạy đầy đủ.

| ID | Trạng thái | Quan sát | Ảnh gốc |
|---|---|---|---|
| G01 | Failed | Home AX contains two headings with level 1 | [ảnh](../evidence/gui/safari/home.png) |
| G04 | Failed | Home price is 30,000,000 VND | [ảnh](../evidence/gui/safari/home.png) |
| G14 | Passed | Search iPhone using Enter leaves one matching product | [ảnh](../evidence/gui/safari/search.png) |
| G25 | Passed | Xem chi tiết opens product/1 with matching title | [ảnh](../evidence/gui/safari/detail-before.png) |
| G02 | Passed | Detail AX shows one level-1 heading, iPhone 15 Pro Max | [ảnh](../evidence/gui/safari/detail-before.png) |
| G05 | Passed | Detail shows 30,000,000 ₫ | [ảnh](../evidence/gui/safari/detail-before.png) |
| G17 | Passed | Number field defaults to 1 | [ảnh](../evidence/gui/safari/detail-before.png) |
| G40 | Failed | Clicked add-to-cart exactly once then opened cart; cart remains empty | [ảnh](../evidence/gui/safari/cart-after-one-click.png) |
| G44 | Failed | Empty cart has message and continue link but no illustration | [ảnh](../evidence/gui/safari/cart-after-one-click.png) |
