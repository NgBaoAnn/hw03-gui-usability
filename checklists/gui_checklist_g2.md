# Checklist GUI G2 đã thực thi

48 mục do Codex thiết kế và thực thi tự động. Sinh viên chưa hoàn tất human review/tự bổ sung. Safari chưa chạy trọn bộ.

Bước thao tác tương ứng từng ID nằm trong `scripts/run_gui.cjs`; kết quả đầy đủ trong `evidence/runs/`. Đọc raw JSON khi Notes dưới đây được rút gọn. Ảnh là ảnh gốc từ lượt chạy, chú thích được thêm sau khi đo.

| ID | IA | Màn hình | Tiêu chí | Nguồn | Chrome | Firefox | Notes Chrome (rút gọn) | Ảnh Failed |
|---|---|---|---|---|---|---|---|---|
| G01 | IA-01 | Home | Đúng một h1 mô tả trang danh sách | FR-05; GUI §8 | Failed | Failed | h1=2 | [Chrome](../evidence/gui/chrome/G01.png); [Firefox](../evidence/gui/firefox/G01.png) |
| G02 | IA-01 | Detail | Đúng một h1 là tên sản phẩm | FR-06; GUI §8 | Passed | Passed | h1=1; iPhone 15 Pro Max |  |
| G03 | IA-01 | Cart | Giỏ có hàng có đúng một h1 | GUI §8 | Failed | Failed | h1=0 | [Chrome](../evidence/gui/chrome/G03.png); [Firefox](../evidence/gui/firefox/G03.png) |
| G04 | IA-01 | Home | Giá trên thẻ dùng ký hiệu ₫, có phân cách hàng nghìn | FR-05; GUI §8 | Failed | Failed | 30.000.000 VND | [Chrome](../evidence/gui/chrome/G04.png); [Firefox](../evidence/gui/firefox/G04.png) |
| G05 | IA-01 | Detail | Giá chi tiết đúng dữ liệu và có ký hiệu ₫ | FR-06 | Passed | Passed | 30.000.000 ₫ |  |
| G06 | IA-01 | Detail | Tên và mô tả chi tiết khớp sản phẩm đã chọn | FR-06 | Passed | Passed | iPhone 15 Pro Max /  / 30.000.000 ₫ /  / Điện thoại cao cấp của Apple /  / Số lượng: / Thêm vào giỏ hàng |  |
| G07 | IA-01 | Home | Ảnh sản phẩm giữ đủ nội dung, không bị object-cover cắt ảnh vuông | FR-05; GUI §8 | Failed | Failed | {"fit":"cover","w":281,"h":192,"nw":300,"nh":300} | [Chrome](../evidence/gui/chrome/G07.png); [Firefox](../evidence/gui/firefox/G07.png) |
| G08 | IA-01 | Home | Ở 1280×900 trang không tràn ngang | Heuristic: responsive | Passed | Passed | {"width":1280,"scroll":1280} |  |
| G09 | IA-01 | Home | Ở 390×844 trang không tràn ngang | Heuristic: responsive | Passed | Failed | {"width":390,"scroll":390} | [Firefox](../evidence/gui/firefox/G09.png) |
| G10 | IA-01 | Detail | Ở 390×844 nút thêm giỏ nằm trọn trong viewport | Heuristic: responsive | Passed | Passed | {"x":41,"y":343,"width":185.9375,"height":48} |  |
| G11 | IA-01 | Detail | Nút thêm giỏ dùng màu xanh dương theo quy chuẩn SUT | GUI §8 | Failed | Failed | rgb(22, 163, 74) | [Chrome](../evidence/gui/chrome/G11.png); [Firefox](../evidence/gui/firefox/G11.png) |
| G12 | IA-01 | Home | Ảnh thẻ có alt mô tả sản phẩm | FR-05; GUI §8 | Failed | Failed | ["","","","",""] | [Chrome](../evidence/gui/chrome/G12.png); [Firefox](../evidence/gui/firefox/G12.png) |
| G13 | IA-02 | Home | Ô tìm kiếm có nhãn truy cập bền vững ngoài placeholder | Heuristic: accessibility | Failed | Failed | label/aria association=false | [Chrome](../evidence/gui/chrome/G13.png); [Firefox](../evidence/gui/firefox/G13.png) |
| G14 | IA-02 | Home | Nhấn Enter tìm iPhone và chỉ hiển thị tên phù hợp | FR-05 | Passed | Passed | ["iPhone 15 Pro Max"] |  |
| G15 | IA-02 | Home | Xóa từ khóa rồi submit khôi phục đủ sản phẩm | FR-05 | Passed | Passed | products=5 |  |
| G16 | IA-02 | Home | Ký tự & trong từ khóa được xử lý như văn bản, không tách query parameter | FR-05 | Failed | Failed | ["iPhone 15 Pro Max"] | [Chrome](../evidence/gui/chrome/G16.png); [Firefox](../evidence/gui/firefox/G16.png) |
| G17 | IA-02 | Detail | Số lượng mặc định là số nguyên 1 | FR-06 | Passed | Passed | 1 |  |
| G18 | IA-02 | Detail | Nhập số lượng 2 tạo dòng giỏ đúng số lượng 2 | FR-06; FR-07 | Passed | Passed | input="2"; cart rows=1; quantity=2; Giỏ Hàng / Sản phẩm	Giá	Số lượng	Thành tiền	Thao tác / iPhone 15 Pro Max	30.000.000 ₫	2	60.000.000 ₫	Xóa / Tổng tạm tính: 60.000.000 ₫ / ← Mua tiếp / Tiến |  |
| G19 | IA-02 | Detail | Số lượng 0 bị từ chối trước khi vào giỏ | FR-06 | Failed | Failed | input="0"; cart rows=1; quantity=0; Giỏ Hàng / Sản phẩm	Giá	Số lượng	Thành tiền	Thao tác / iPhone 15 Pro Max	30.000.000 ₫	0	0 ₫	Xóa / Tổng tạm tính: 0 ₫ / ← Mua tiếp / Tiến hành thanh toán | [Chrome](../evidence/gui/chrome/G19.png); [Firefox](../evidence/gui/firefox/G19.png) |
| G20 | IA-02 | Detail | Số lượng âm bị từ chối trước khi vào giỏ | FR-06 | Failed | Failed | input="-1"; cart rows=1; quantity=-1; Giỏ Hàng / Sản phẩm	Giá	Số lượng	Thành tiền	Thao tác / iPhone 15 Pro Max	30.000.000 ₫	-1	-30.000.000 ₫	Xóa / Tổng tạm tính: -30.000.000 ₫ / ← Mua tiếp | [Chrome](../evidence/gui/chrome/G20.png); [Firefox](../evidence/gui/firefox/G20.png) |
| G21 | IA-02 | Detail | Số lượng thập phân bị từ chối thay vì làm tròn âm thầm | FR-06 | Failed | Failed | input="1.5"; cart rows=1; quantity=1; Giỏ Hàng / Sản phẩm	Giá	Số lượng	Thành tiền	Thao tác / iPhone 15 Pro Max	30.000.000 ₫	1	30.000.000 ₫	Xóa / Tổng tạm tính: 30.000.000 ₫ / ← Mua tiếp / Ti | [Chrome](../evidence/gui/chrome/G21.png); [Firefox](../evidence/gui/firefox/G21.png) |
| G22 | IA-02 | Detail | Số lượng bỏ trống bị từ chối, không sinh NaN trong giỏ | FR-06 | Failed | Failed | input=""; cart rows=1; quantity=NaN; Giỏ Hàng / Sản phẩm	Giá	Số lượng	Thành tiền	Thao tác / iPhone 15 Pro Max	30.000.000 ₫	NaN	NaN ₫	Xóa / Tổng tạm tính: NaN ₫ / ← Mua tiếp / Tiến hành thanh | [Chrome](../evidence/gui/chrome/G22.png); [Firefox](../evidence/gui/firefox/G22.png) |
| G23 | IA-02 | Detail | Nhãn Số lượng được liên kết với input | Heuristic: accessibility | Failed | Failed | label/aria association=false | [Chrome](../evidence/gui/chrome/G23.png); [Firefox](../evidence/gui/firefox/G23.png) |
| G24 | IA-02 | Home | Từ khóa chứa HTML được hiển thị nguyên văn, không tạo phần tử HTML | FR-05; SEC-04 | Failed | Failed | Rendered HTML elements=1; benign markup only, no script executed | [Chrome](../evidence/gui/chrome/G24.png); [Firefox](../evidence/gui/firefox/G24.png) |
| G25 | IA-03 | Home | Xem chi tiết mở đúng sản phẩm | FR-06 | Passed | Passed | http://localhost:5173/product/1 |  |
| G26 | IA-03 | Detail | Link EShop đưa về danh sách | GUI §8 | Passed | Passed | http://localhost:5173/ |  |
| G27 | IA-03 | Home | Link Giỏ hàng mở trang giỏ | FR-07 | Passed | Passed | Giỏ hàng của bạn đang trống / Tiếp tục mua sắm |  |
| G28 | IA-03 | Cart | Tiếp tục mua sắm từ giỏ trống về danh sách | FR-07 | Passed | Passed | http://localhost:5173/ |  |
| G29 | IA-03 | Home | Browser Back từ chi tiết giữ từ khóa và kết quả đã tìm | Heuristic: continuity | Failed | Failed | query=""; products=5 | [Chrome](../evidence/gui/chrome/G29.png); [Firefox](../evidence/gui/firefox/G29.png) |
| G30 | IA-03 | Detail | Trang chi tiết có breadcrumb | GUI §8 | Failed | Failed | breadcrumb regions=0 | [Chrome](../evidence/gui/chrome/G30.png); [Firefox](../evidence/gui/firefox/G30.png) |
| G31 | IA-03 | Cart | Trang giỏ có breadcrumb | GUI §8 | Failed | Failed | breadcrumb regions=0 | [Chrome](../evidence/gui/chrome/G31.png); [Firefox](../evidence/gui/firefox/G31.png) |
| G32 | IA-03 | Cart | Navbar highlight Giỏ hàng khi ở /cart | GUI §8 | Failed | Failed | aria-current=null; class=hover:underline | [Chrome](../evidence/gui/chrome/G32.png); [Firefox](../evidence/gui/firefox/G32.png) |
| G33 | IA-03 | Home | Có thể Tab đến ô tìm kiếm theo thứ tự logo, giỏ, đăng nhập, đăng ký, tìm kiếm | GUI §8 | Passed | Passed | ["EShop","Giỏ hàng","Đăng nhập","Đăng ký","Tìm kiếm..."] |  |
| G34 | IA-03 | Home | Có thể tìm và mở chi tiết chỉ bằng bàn phím | Heuristic: keyboard | Passed | Passed | http://localhost:5173/product/1 |  |
| G35 | IA-03 | Cart | Giỏ có hàng có đường quay về danh sách | FR-07 | Passed | Passed | http://localhost:5173/ |  |
| G36 | IA-03 | Cart | Thêm lại cùng sản phẩm gộp một dòng, tăng số lượng | FR-07 | Failed | Failed | rows=2; first quantity=1 | [Chrome](../evidence/gui/chrome/G36.png); [Firefox](../evidence/gui/firefox/G36.png) |
| G37 | IA-04 | Home | Chờ API danh sách có trạng thái loading nhìn thấy | FR-05 | Failed | Failed | Artificial API delay 1600ms; observed: Danh sách sản phẩm / Tìm | [Chrome](../evidence/gui/chrome/G37.png); [Firefox](../evidence/gui/firefox/G37.png) |
| G38 | IA-04 | Home | Không có kết quả có thông báo empty state thân thiện | FR-05; GUI §8 | Failed | Failed | Danh sách sản phẩm / Tìm / Kết quả tìm kiếm cho: HW03-no-such-product-731 | [Chrome](../evidence/gui/chrome/G38.png); [Firefox](../evidence/gui/firefox/G38.png) |
| G39 | IA-04 | Home | Thêm từ thẻ có toast hoặc badge xác nhận | FR-06; GUI §8 | Failed | Failed | live regions=0; nav=Giỏ hàng / Đăng nhập / Đăng ký | [Chrome](../evidence/gui/chrome/G39.png); [Firefox](../evidence/gui/firefox/G39.png) |
| G40 | IA-04 | Detail | Lần bấm Thêm đầu tiên thực sự thêm đúng một sản phẩm | FR-06 | Failed | Failed | After one click: cart rows=0; Giỏ hàng của bạn đang trống / Tiếp tục mua sắm | [Chrome](../evidence/gui/chrome/G40.png); [Firefox](../evidence/gui/firefox/G40.png) |
| G41 | IA-04 | Detail | Thêm thành công có phản hồi trực quan | FR-06; GUI §8 | Passed | Passed | After second click: Đã thêm |  |
| G42 | IA-04 | Cart | Link Giỏ hàng có badge số lượng sau khi thêm | GUI §8 | Failed | Failed | link=Giỏ hàng; badge elements=0 | [Chrome](../evidence/gui/chrome/G42.png); [Firefox](../evidence/gui/firefox/G42.png) |
| G43 | IA-04 | Cart | Xóa sản phẩm yêu cầu xác nhận trước khi mất dữ liệu | FR-07; GUI §8 | Failed | Failed | confirmation=false; dialog elements=0; remaining cart rows=0 | [Chrome](../evidence/gui/chrome/G43.png); [Firefox](../evidence/gui/firefox/G43.png) |
| G44 | IA-04 | Cart | Giỏ trống có hình/icon và thông báo | FR-07; GUI §8 | Failed | Failed | illustrations=0; Giỏ hàng của bạn đang trống / Tiếp tục mua sắm | [Chrome](../evidence/gui/chrome/G44.png); [Firefox](../evidence/gui/firefox/G44.png) |
| G45 | IA-04 | Cart | Tổng tiền mang nhãn Tổng cộng | FR-07 | Failed | Failed | Giỏ Hàng / Sản phẩm	Giá	Số lượng	Thành tiền	Thao tác / iPhone 15 Pro Max	30.000.000 ₫	1	30.000.000 ₫	Xóa / Tổng tạm tính: 30.000.000 ₫ / ← Mua tiếp / Tiến hành thanh toán | [Chrome](../evidence/gui/chrome/G45.png); [Firefox](../evidence/gui/firefox/G45.png) |
| G46 | IA-04 | Detail | ID sản phẩm không tồn tại kết thúc chờ và báo lỗi rõ ràng | Heuristic: error recovery | Passed | Passed | Sản phẩm không tồn tại (Lỗi trắng trang do data rỗng) |  |
| G47 | IA-04 | Home | Lỗi API danh sách có thông báo và khả năng thử lại | Heuristic: error recovery | Failed | Failed | Controlled HTTP 503; Danh sách sản phẩm / Tìm | [Chrome](../evidence/gui/chrome/G47.png); [Firefox](../evidence/gui/firefox/G47.png) |
| G48 | IA-04 | Detail | Lỗi API chi tiết không kẹt ở Đang tải | Heuristic: error recovery | Failed | Failed | Controlled HTTP 503; Đang tải... | [Chrome](../evidence/gui/chrome/G48.png); [Firefox](../evidence/gui/firefox/G48.png) |
