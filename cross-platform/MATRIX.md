# Ma trận cross-browser

Đã thực thi đầy đủ 48 mục trên 3 trình duyệt thật: Chrome, Firefox và Safari. Viewport hẹp là kiểm tra responsive, không tính thêm nền tảng.

| Môi trường | Số mục | Passed | Failed | Blocked |
|---|---:|---:|---:|---:|
| Google Chrome 157.0.8103.50 / macOS 26.2 (Darwin 25.2.0) | 48 | 19 | 29 | 0 |
| Firefox (Playwright build) 153.0 / macOS 26.2 (Darwin 25.2.0) | 48 | 18 | 30 | 0 |
| Safari 26.2 (Apple safaridriver) / macOS 26.2 | 48 | 19 | 29 | 0 |

Khác biệt kết quả: G09: chrome Passed, firefox Failed, safari Passed.

Ảnh chụp dùng chú thích có email, MSSV, họ tên, browser/version, OS, URL và timestamp. Chú thích nằm ngoài SUT và được thêm sau phép đo. Thuộc tính DOM và số liệu viewport cần đọc kèm JSON.

## Phương pháp Safari thật

Apple Safari WebDriver; same-origin iframe with exact CSS viewport except G29, which uses the top-level SUT and native WebDriver Back to avoid iframe history semantics. Full navigation resets React state per case. G37/G47/G48 use explicitly redirected XHR to a localhost delay/503 fixture; default Safari all-item keyboard navigation is Option-Tab.

Safari dùng iframe cùng origin để đặt đúng viewport CSS 1280px/390px mà không thay đổi layout của SUT. Các mục G37/G47/G48 định tuyến XHR mục tiêu đến fixture localhost cho delay/HTTP 503, không đổi logic SUT. Native Option-Tab được dùng để đi qua mọi phần tử trong thiết lập bàn phím Safari mặc định.

Sau khi nhập, SafariDriver đôi khi chỉ blur input mà không phát click. Bộ chạy đo số DOM click và chỉ lặp lệnh khi chưa có click nào được giao; log `click_delivery` ghi lại các lần này. Mỗi hành động logic giao đúng một click, không bấm thêm để che lỗi G40. Những mục bị ảnh hưởng đã được chạy lại; chỉ kết quả cuối mỗi ID được thống kê.

## Đối chiếu với kiểm tra Safari thủ công trước đó

Safari 26.2, macOS 26.2. Trước lượt WebDriver, đã quan sát 9 mục qua native UI/CUA trong iframe cùng origin. Giữ nguyên bằng chứng lịch sử này để đối chiếu, không cộng lặp vào 144 lượt của ba browser.

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

## Định danh trong form SUT

Ngoài overlay trên ảnh Failed, có ba ảnh form đăng ký EShop thật với họ tên, MSSV và email trong trường nhập: xem `IDENTITY.md` và `evidence/identity/`. Form chưa gửi, không tạo tài khoản. Đây là bằng chứng định danh bổ sung, không cộng vào số lượt GUI hoặc usability.
