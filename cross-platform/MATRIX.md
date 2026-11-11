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
