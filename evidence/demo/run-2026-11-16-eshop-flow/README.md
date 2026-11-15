# EShop — run kiểm thử luồng mua hàng

**Trạng thái:** Bản ghi một lượt chạy có hướng dẫn, không phải gói nghiên cứu HW03 hoàn chỉnh.

## Mục tiêu và kịch bản

Tìm “AirPods Pro 2”, mở chi tiết, thêm một sản phẩm vào giỏ, đăng nhập tài khoản test, xác nhận checkout, rồi kiểm tra đơn và giỏ sau khi thành công. Đã đặt đơn trong môi trường localhost để kiểm tra trọn luồng; không có cổng thanh toán thật.

## Môi trường

- SUT: `http://localhost:5173`; Backend API: `http://localhost:3000` (cả hai trả HTTP 200 lúc bắt đầu).
- Revision: `85af3ba875c88283615e22cb108f13e2fccaf0e9`.
- Trình duyệt: ChatGPT in-app browser (IAB); phiên bản engine không được công cụ hiển thị. Không gọi đây là Chrome, Firefox hay Safari.
- Hệ điều hành: macOS 26.2, build 25C56.
- Thời gian bắt đầu: 2026-11-16 01:04 +07 (Asia/Ho_Chi_Minh). Kết thúc ghi nhận: 2026-11-16 01:08 +07.
- Thao tác bằng trình duyệt hiển thị; không giả lập độ trễ hay lỗi mạng.

## Kết quả theo tiêu chí đã chọn

| ID / tham chiếu | Mong đợi | Quan sát thực tế | Kết quả |
|---|---|---|---|
| G14 / FR-05 | Tìm theo tên và chỉ hiện sản phẩm phù hợp | Tìm “AirPods Pro 2” bằng nút Tìm, danh sách còn đúng một sản phẩm | Đạt |
| G02 / FR-06 | Chi tiết có một h1 là tên sản phẩm | AX tree báo heading “Tai nghe AirPods Pro 2” cấp 1; route `/product/4` | Đạt |
| G17 / FR-06 | Số lượng ban đầu là 1 | Ô số lượng hiển thị 1 | Đạt |
| G25 / FR-06 | Mở đúng sản phẩm đã chọn | Trang chi tiết là Tai nghe AirPods Pro 2, giá 6.000.000 ₫ | Đạt |
| G30 / GUI §8 | Có breadcrumb trên trang chi tiết | Không thấy breadcrumb trong giao diện/AX tree | Không đạt |
| G39, G41 / FR-06, GUI §8 | Sau thao tác thêm có toast hoặc badge | Sau khi thêm khi đã đăng nhập, trang không hiện toast hay badge; sản phẩm chỉ được xác nhận sau khi mở giỏ | Không đạt |
| G03 / GUI §8 | Giỏ có hàng có đúng một h1 | AX tree báo heading “Giỏ Hàng” ở cấp 2, không thấy h1 | Không đạt |
| G31 / GUI §8 | Có breadcrumb ở giỏ | Không thấy breadcrumb | Không đạt |
| G42 / GUI §8 | Link giỏ hiển thị badge số lượng | Link “Giỏ hàng” không có số lượng | Không đạt |
| G45 / FR-07 | Tổng có nhãn “Tổng cộng” | UI ghi “Tổng tạm tính” | Không đạt |
| FR-08 | Checkout liệt kê hàng và tổng không chỉnh trực tiếp | Sản phẩm và giá đúng; ô tổng là input/stepper có thể chỉnh | Một phần; tổng chỉnh được là lỗi |
| FR-08 | Khi hoàn tất, giỏ được xóa | UI báo thanh toán thành công và tạo đơn #9, nhưng mở lại giỏ vẫn thấy AirPods Pro 2 x1 | Không đạt |
| FR-11 | Lịch sử đơn hiển thị mã, ngày, tổng, trạng thái | Hồ sơ hiển thị đơn #9, 6.000.000 ₫, “Chờ xác nhận” | Đạt |
| FR-21, FR-22 | Giao diện tiếng Việt, nhãn biểu mẫu rõ | Trang đăng nhập ghi tiêu đề “Đăng Ký”, nhãn “Username” và nút “Sign In” | Không đạt |
| FR-21 | Hành động tích cực dùng xanh dương | Nút thêm ở trang chi tiết và nút xác nhận checkout hiển thị xanh lá | Không đạt |

## Nhật ký rút gọn

1. Trang chủ → tìm AirPods Pro 2 → đúng một kết quả.
2. Trang chi tiết → số lượng mặc định 1. Bấm thêm khi chưa đăng nhập không đổi trạng thái giỏ; sau đó đăng nhập theo tài khoản demo ở README của SUT.
3. Tìm lại sản phẩm và bấm Thêm vào giỏ khi đã đăng nhập → mở giỏ thấy đúng một dòng, số lượng 1.
4. Giỏ → checkout → tổng hiển thị 6.000.000 ₫, ô tổng có thể chỉnh; xác nhận thanh toán.
5. UI báo thành công; hồ sơ ghi nhận đơn #9 đang chờ xác nhận. Giỏ vẫn còn sản phẩm sau đó.

## Ảnh bằng chứng gốc

- [01 — Kết quả tìm kiếm](01-search.png)
- [02 — Chi tiết sau lần bấm thêm đầu tiên](02-detail-after-add-attempt.png)
- [03 — Giỏ trước checkout](03-cart-before-checkout.png)
- [04 — Checkout, tổng là ô chỉnh sửa](04-checkout.png)
- [05 — Thông báo thành công](05-success.png)
- [06 — Sản phẩm còn trong giỏ sau thành công](06-cart-retained.png)

## Annotation nhận diện (ghi sau khi đo; tách biệt khỏi ảnh giao diện)

Nguyễn Bảo An · MSSV 23120207 · 23120207@student.hcmus.edu.vn. Thông tin này chỉ nằm ở annotation báo cáo, không được thêm vào hay sửa ảnh chụp màn hình.

## Giới hạn

Đây là một lượt agent quan sát, không phải phiên người tham gia độc lập; không thu thập SUS hay dữ liệu think-aloud. Chưa kiểm tra lỗi API/network, loading, xóa giỏ, coupon, responsive breakpoint khác, cũng chưa lập checklist >40 mục hay tổ chức pilot + 7 phiên HW03. Bằng chứng phản ánh đúng revision và phiên chạy ở trên. Các lần bấm vào đặt hàng đã ghi một đơn test #9 trong CSDL demo.
