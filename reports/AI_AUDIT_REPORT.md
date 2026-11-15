# AI Audit Report - HW03 G2

Sinh viên: Nguyễn Bảo An - 23120207. Trạng thái: bản ghi việc đã thực hiện, chờ sinh viên rà soát và xác nhận.

Sinh viên đã xác nhận chọn tự quay video dùng cho bài nộp và cho phép public repo `NgBaoAnn/hw03-gui-usability`. Video cũ Codex ghi đã được sinh viên loại khỏi hồ sơ. Ngày 16/11 sinh viên cung cấp https://youtu.be/VGVm_V7L_ks ; đã kiểm tra phát công khai khi không đăng nhập. Repo đã chuyển public và kiểm tra quyền truy cập không đăng nhập; không có dữ liệu người tham gia thực tế trong repo tại thời điểm chuyển.

## Khai báo

“I use AI tools for the following tasks,” gồm: đọc đề và chính sách; kiểm tra thông tin Moodle; đối chiếu phạm vi với mã nguồn/dữ liệu SUT; thiết kế 48 mục checklist; viết và chạy bộ kiểm thử trình duyệt; chụp bằng chứng thật; nhóm và viết báo cáo lỗi; chuẩn bị protocol, SUS và biểu mẫu; viết trình tính SUS; xây dựng agent skill; soạn báo cáo và xuất Excel/PDF/bản zip nháp.

Công cụ AI: OpenAI Codex desktop, agent dựa trên GPT-6 theo thông tin phiên. Phiên hiện tại bắt đầu ngày 11/11/2026, múi giờ Asia/Ho_Chi_Minh. Thời điểm từng prompt/output lấy từ timestamp transcript, không tự ước lượng.

## Prompt, thời điểm và đầu ra

`AI_TRANSCRIPT.md` chứa nguyên văn prompt và câu trả lời hiển thị của chat hiện tại, có ngày giờ từng tin nhắn. Các câu hỏi và câu trả lời về phạm vi G2, email sinh viên, dữ liệu người tham gia cũng được giữ để truy vết quyết định. File này không xuất suy luận nội bộ hay thông tin xác thực.

Đầu ra có thể tái kiểm tra:

| Hoạt động AI | Đầu ra thực tế | Kiểm chứng / trạng thái |
|---|---|---|
| Khám phá yêu cầu | MAIN_REPORT.md §1 | Đối chiếu PDF gốc, policies, assignment/status/section và thread GUI/Usability Moodle |
| Thiết kế checklist | checklists/items.json; gui_checklist_g2.md/.csv/.xlsx | 48 ID duy nhất, 12 mục/IA; chưa có mục sinh viên tự bổ sung |
| Kiểm thử GUI | scripts/run_gui.cjs; scripts/run_safari.py; evidence/runs/*.json | 48 mục trên mỗi browser: Chrome/Firefox bằng Playwright, Safari thật bằng Apple WebDriver; raw results, version, timestamp và SUT commit |
| Chụp ảnh | evidence/gui/ | Browser screenshot thật, có chú thích định danh sau phép đo; không dùng ImageGen |
| Định danh trong form thật | evidence/identity/; cross-platform/IDENTITY.md | Điền tên/MSSV/email vào form đăng ký SUT trên ba browser, để trống mật khẩu, không gửi form và không tạo tài khoản |
| Kiểm tra Safari | evidence/runs/safari.json; evidence/gui/safari/ | Safari 26.2 thật: 19 Passed, 29 Failed, 0 Blocked; giữ thêm 9 quan sát CUA cũ để đối chiếu, không cộng lặp |
| Báo cáo bug | bug-reports/BUG_REPORTS.md và B01–B23.md | Gộp 88 Failed trên ba browser thành 23 nhóm; heuristic được ghi rõ; Issue URL trong issues.json |
| Tích hợp usability | usability/PROTOCOL.md, SUS_QUESTIONNAIRE.md, CSV, sessions/, provenance.json | Hồ sơ 1 pilot + 7 phiên do sinh viên cung cấp và xác nhận; đối chiếu CSV/JSON, không xác minh độc lập danh tính |
| Tính SUS | scripts/calculate_sus.py; sheet SUS | Đối chiếu 70 câu trả lời; trung bình 58,93/100; pilot tách riêng; self-check 0/50/100 và từ chối thiếu/sai thang |
| Xây skill | skills/gui-usability-evaluator/SKILL.md | Kiểm tra cấu trúc skill thành công; Bản gốc và demo-version có đủ tài nguyên; video sinh viên đã cung cấp |
| Demo sinh viên cung cấp | skills/gui-usability-evaluator/DEMO.md; AI_DEMO_TRANSCRIPT.md; evidence/demo/ | YouTube VGVm_V7L_ks phát được; 10:38; bản skill dùng thực tế được giữ nguyên, sáu ảnh gốc và prompt/output đúng chat |
| Khôi phục audit lập kế hoạch | reports/AI_AUDIT_RECOVERED.md; reports/legacy/ | 14 lời nhắn thật ngày 03/11 của OpenCode gắn đúng thư mục; ba đầu ra kế hoạch nguyên gốc kèm hash |
| Đóng gói | scripts/validate_submission.py và package_draft.py | Bản nháp có ghi rõ thiếu sót; chưa nộp Moodle |

## Rà soát và các sửa đổi đã xảy ra

Kế hoạch cũ giả định bộ lọc, sắp xếp, đánh giá sản phẩm và một tai nghe dưới 500.000 ₫; nguồn và dữ liệu chạy không hỗ trợ những giả định này. Codex đã thu hẹp kịch bản theo chức năng thực, ngân sách 7 triệu. Đây là sửa đổi của AI, chưa được ghi là đóng góp phản biện của sinh viên.

Bộ chạy thử ban đầu chưa chờ React chuyển trang xong, dẫn đến một số kết quả sai. Codex thêm điều kiện chờ route và heading giỏ, chạy lại cả Chrome/Firefox. Thống kê cuối lấy từ JSON cuối, không cộng dồn lượt thử. Không sửa logic SUT để che lỗi.

Sau khi sinh viên cho phép Safari WebDriver, sinh viên tự xác thực Touch ID/mật khẩu máy để bật quyền. Không cung cấp mật khẩu cho AI. Safari được chạy với Apple safaridriver. Iframe cùng origin đặt viewport CSS chính xác; riêng Browser Back dùng SUT ở top-level và lệnh Back chuẩn vì lịch sử của iframe không tương đương cửa sổ chính. Mạng chậm/HTTP 503 dùng XHR redirect tới fixture localhost có ghi rõ, không sửa logic SUT.

Sau khi hoàn tất, đã tắt lại Allow remote automation và Show features for web developers về trạng thái ban đầu. Không thay đổi thiết lập bàn phím hoặc các quyền JavaScript/cross-origin khác.

SafariDriver đôi khi blur input sau khi nhập mà chưa phát click. Codex ghi số DOM click, chỉ lặp lệnh WebDriver nếu chưa có click được giao, rồi chạy lại các mục bị ảnh hưởng. Lỗi nút bỏ qua click đầu vẫn được giữ vì click thực đã tới ứng dụng. Những mục từng Blocked không được coi là bug; JSON cuối có đủ 48 kết quả Passed/Failed. Kết quả tổng: 144 lượt, 56 Passed, 88 Failed, 23 nhóm bug. Sinh viên chưa hoàn tất human review. Ngày 15/11 sinh viên bổ sung hồ sơ 1 pilot + 7 phiên và xác nhận đã tự điều phối các phiên thật; Codex kiểm tra phép tính và tính nhất quán.

Không dùng danh sách lớp Moodle làm người tham gia. Không tạo điểm SUS, phát ngôn, thời gian, tên/liên hệ hay kết quả phiên để lấp dữ liệu thiếu. Dữ liệu bổ sung do sinh viên cung cấp; danh tính và việc diễn ra phiên không được Codex xác minh độc lập. Bản public dùng mã P1–P7; danh sách tên/liên hệ đã che chỉ có trong ZIP nộp.

## Lịch sử lập kế hoạch đã khôi phục

Đã khôi phục session OpenCode “Homework requirements overview” gắn chính xác thư mục HW03, từ 15:28 đến 16:08 ngày 03/11/2026. File `AI_AUDIT_RECOVERED.md` chứa 14 lời nhắn user/assistant hiển thị, timestamp thật và cấu hình model từ metadata. Ba bản kế hoạch gốc được giữ trong `reports/legacy/` cùng SHA-256, bao gồm các giả định AI đã đề xuất sai. Không truy xuất các phiên đăng nhập hoặc mạng không liên quan.

Đầu ra tool viết file trong session cũ được đối chiếu với ba file và Git commits thực. Chỉ xuất phần văn bản hiển thị; không đưa suy luận nội bộ hoặc thông tin xác thực vào bài. Bản PDF audit có phụ lục hội thoại cũ và mới. Sinh viên cần kiểm tra và bổ sung nếu đã dùng AI ở những nơi khác không nằm trong hai nguồn đã khôi phục. Các tin nhắn sau thời điểm xuất transcript sẽ được xuất lại trước lần nộp cuối.

## Trạng thái sinh viên rà soát

Chưa xác nhận đã hoàn tất human review/tự bổ sung checklist hoặc duyệt AI Critique. Sinh viên đã xác nhận phạm vi, nguồn Task 2, lựa chọn công khai repo và điểm tự chấm 100/100; các xác nhận đó không thay việc xem xét kết quả thực tế. Không tự ký thay sinh viên.


## Tích hợp dữ liệu Task 2 ngày 15/11/2026

Hồ sơ nhận vào có thông tin sinh viên khác và tên file simulation.json. Codex hỏi nguồn; sinh viên yêu cầu sửa tên/MSSV, rồi xác nhận rõ đây là các phiên thật mình điều phối. Đã sao lưu nguyên gốc riêng, ghi SHA-256, sửa thông tin người nộp, đối chiếu 70 câu trả lời CSV/JSON và tính SUS độc lập (58,93/100). Không tạo thêm câu trả lời hay phát ngôn người tham gia. Phạm vi Task 2 giữ quản lý đơn hàng theo dữ liệu bổ sung, Task 1 giữ G2.

Đã chụp năm ảnh tái hiện trên SUT thật bằng tài khoản và đơn fixture riêng. Đây là bằng chứng trạng thái UI hiện tại, không gán thành ảnh/video nghiên cứu. Đã thay liên kết ảnh thiếu bằng ảnh tái hiện và phân biệt giới hạn bằng chứng. Hồ sơ không có video phiên; không gán việc từ chối ghi hình thành miễn trừ tự động của giảng viên. Dữ liệu nhập cùng lúc được commit theo ngày tích hợp, không lùi ngày hoặc tạo lịch sử cho từng phiên đã qua.


Đính chính sau khi đối chiếu §14 đề tiếng Anh: bản quay phiên được nộp khi có (screen recordings where available). Không đặt việc xin chấp nhận của giảng viên thành một điều kiện đóng gói mới. Giữ nguyên ghi chú từ chối ghi hình và giới hạn không có video.


## Điểm tự chấm và lượt AI rà soát bổ sung

Sinh viên yêu cầu “cho full điểm”; hồ sơ ghi 30/40/20/10 = 100/100 theo lựa chọn đó. Chưa coi mức điểm này là điểm giảng viên hoặc bằng chứng đã hoàn thành các mục còn thiếu. Sinh viên giao AI tự ghi phần rà soát; Codex rà checklist, kết quả, cách gom bug, giới hạn kết luận và viết checklists/AI_REVIEW.md. Lượt này chỉ đối chiếu hồ sơ/bằng chứng đã lưu, không chạy lại GUI. Không gán thành đóng góp tự phát hiện của sinh viên; HUMAN_REVIEW.md và trạng thái human_review_complete vẫn chờ thực tế.


## Ba kiểm tra tiếp cận bổ sung

Theo yêu cầu sinh viên tiếp tục làm phần phản biện/bổ sung, Codex soạn lại AI Critique 278 từ và thêm G49–G51 có giải thích nguyên nhân bỏ sót. Đã dùng native CUA mở Chrome Incognito, Firefox Nightly Playwright build và Safari thật. Trang đo cùng origin đọc lang/computed CSS của SUT trong iframe, gửi JSON đến collector localhost; không đổi logic/style SUT, không bật lại Remote Automation. Chín phép đo được ghi thật cùng chín ảnh cửa sổ. Collector ban đầu trùng tên thuộc tính headers của HTTP handler nên lỗi lưu; đã đổi tên hàm respond và chạy lại, chỉ kết quả được lưu thành công mới dùng trong hồ sơ.

G49 ghi lang=en trên nội dung tiếng Việt. G50 đạt tương phản 3,763127680148142; G51 đạt 3,2957336053312796. Với cỡ chữ 16px đã đo, ngưỡng áp dụng 4,5:1. Công thức JS tự kiểm đen/trắng và cùng màu; Python đối chiếu độc lập sáu phép đo tương phản và ngoại lệ chữ lớn. Nguồn WCAG chính thức nằm trong ADDITIONS.md; đây là heuristic tiếp cận ngoài cam kết FR. Không suy ra kết quả thử screen reader hoặc tần suất khó khăn của người dùng.

Bộ gốc 48 mục được giữ riêng; tổng mới 51 mục, 153 kết quả, 56 Passed/97 Failed, 25 nhóm bug GUI. Hai bug B24/B25 bổ sung Issue #29/#30, cùng năm finding usability thành 30 Issues. Rà soát/bổ sung vẫn ghi do AI theo yêu cầu sinh viên; không tạo lời xác nhận hoặc mục tự phát hiện mang tên sinh viên.


## Ghi nhận đóng góp cá nhân

Theo yêu cầu sinh viên, đã lập reports/PERSONAL_CONTRIBUTION.md và đưa vào báo cáo chính. Mục này đối chiếu các lựa chọn, xác nhận, dữ liệu cung cấp, hỗ trợ xác thực Safari, yêu cầu phản biện/bổ sung, quyết định công bố và tự chấm của Nguyễn Bảo An. Phần tổ chức nghiên cứu ghi theo xác nhận sinh viên; phần kỹ thuật do AI thực hiện được tách rõ. Không thêm tỷ lệ đóng góp tùy ý, chữ ký, mục tự phát hiện hoặc lời xác nhận đã human review. Video demo đã được sinh viên cung cấp ngày 16/11; prompt/output và bằng chứng được bổ sung đúng nguồn.


## Chốt video và hồ sơ nộp ngày 16/11/2026

Video sinh viên gửi: https://youtu.be/VGVm_V7L_ks . YouTube công khai và phát được khi không đăng nhập; UI hiển thị 10:38, metadata làm tròn 639 giây. Không có phụ đề tự động. Đã đối chiếu các khung hình mẫu của bản quay cục bộ dài 638,538 giây và chat demo đúng SUT; không đánh giá độc lập toàn bộ thuyết minh âm thanh. Không đưa file quay 432 MB hoặc URL media có chữ ký vào ZIP.

Chat demo “Kiểm thử luồng EShop hoàn chỉnh” có 9 lời nhắn hiển thị, từ 01:03:18 đến 01:09:59 ngày 16/11, được xuất riêng tại AI_DEMO_TRANSCRIPT.md và ghép vào PDF audit. Nội dung tool/suy luận nội bộ không xuất; sáu ảnh và báo cáo gốc lưu trong evidence/demo/. Skill thực dùng trong video được sao chép nguyên trạng cùng tài nguyên, SHA-256 lưu trong video-verification.json. Demo tạo đơn localhost #9, không phải giao dịch thật; không tính như phiên người tham gia hoặc nền tảng thứ tư của Task 3.

Đã ghi D01–D03 cho các phát hiện mới trong demo, có nguồn FR và ảnh gốc; các phát hiện trùng được liên kết báo cáo hiện có. Giữ nguyên số liệu G2 51 mục/153 kết quả và Task 2. Người dùng tiếp tục giao AI tự bổ sung phần còn thiếu; chưa có bằng chứng tự rà soát/tự phát hiện từ sinh viên, nên không đổi human_review_complete hoặc ký thay. Gói theo tên điểm tự chấm 100 giữ đầy đủ giới hạn trong SUBMISSION_STATUS.json.


## Đính chính nguồn G52 và đo lại Safari ngày 16/11/2026

Bản bổ sung do người dùng cung cấp ghi G52 là sinh viên tự phát hiện, trong khi phần nhật ký bổ sung ghi AI đề xuất. Đã giữ văn bản bổ sung tại AI_SUPPLIED_ADDENDUM.md, phân biệt với nhật ký được xuất trực tiếp từ session hiện tại; chưa xác minh timestamp/nguyên văn phần bổ sung với session gốc. Đã sửa thống nhất G52 là AI đề xuất và thực thi theo yêu cầu sinh viên, không tạo chữ ký hoặc lời xác nhận điện tử thay. Việc sinh viên đã rà soát G49–G51 được ghi nhận theo bản khai cung cấp; chưa có tiêu chí sinh viên tự phát hiện riêng. human_added_check_ids=[]; trạng thái thiếu trong ZIP phản ánh giới hạn này.

Safari G52 trước chỉ đo 390×839. Đã giữ JSON cũ trong G52-390x839-original.json, sửa trang đo đặt cả width=390px/height=844px và chờ innerWidth/innerHeight đúng kích thước trước phép đo. Đã reload bằng native CUA trên Safari thật, ghi JSON và ảnh mới: 390×844; ô số lượng 80×42; nút 185,9×48; Passed. Không bật Remote Automation, không chỉnh logic SUT, không cộng bản đo cũ vào thống kê. Collector localhost được tắt sau lượt đo.

Tổng hiện tại 52 tiêu chí, 156 kết quả (59 Passed, 97 Failed); 25 nhóm bug G2, 5 finding usability và 3 phát hiện demo, tổng 33 Issues. Bằng chứng, CSV/MD/Excel, PDF, các bộ tạo báo cáo, nhật ký Git và ZIP được đồng bộ theo bước hoàn thành thực tế. Không lùi ngày commit. Điểm tự chấm 100 không chứng nhận đáp ứng yêu cầu tự phát hiện hoặc bảo đảm điểm giảng viên.
