# Những việc Bảo An cần làm để chốt HW03

Hạn nộp Moodle đã kiểm tra: **13:00 ngày 16/11/2026, giờ Việt Nam**, cutoff cùng giờ. Bài cá nhân, phạm vi G2 đã xác nhận. Hồ sơ hiện là bản nháp có bằng chứng kiểm thử thật; chưa có nghiên cứu usability với người tham gia.

## 1. Rà soát và bổ sung checklist bằng quan sát của bạn

Mở `checklists/gui_checklist_g2.xlsx`, `checklists/HUMAN_REVIEW.md` và SUT tại http://localhost:5173. Trong Excel có 48 mục, ba cột kết quả Chrome/Firefox/Safari và Notes riêng. Đọc từng tiêu chí, đối chiếu yêu cầu và ảnh bug; đánh dấu chấp nhận/sửa/loại trong phiếu human review. Tái hiện các lỗi bạn chưa hiểu trước khi xác nhận. Có thể bắt đầu với B18 (thêm giỏ lần đầu), B09 (số lượng không hợp lệ), B14 (giỏ trùng dòng).

Tự tìm các điểm mà bộ AI chưa bao phủ và ghi vào bảng “Mục sinh viên tự bổ sung”. Đề không quy định số mục tự bổ sung tối thiểu; mỗi mục phải có ý nghĩa riêng. Cần ghi: IA, màn hình, bước thao tác, kết quả kỳ vọng, vì sao AI bỏ sót, quan sát thật và ảnh nếu Failed. Các ví dụ AI đã gợi ý chỉ là gợi ý; ghi đúng nguồn đóng góp của bạn.

Gửi các mục bạn tự bổ sung cho Codex trước khi chốt. Codex sẽ thêm chúng vào checklist/Excel, chạy trên ba browser khi có thể, tạo ảnh/bug cần thiết và cập nhật số lượng. Không cần tự sửa mã kiểm thử hoặc file `items.json`.

Đầu ra cần bạn điền: `checklists/HUMAN_REVIEW.md`. Sau khi đọc báo cáo, sửa `reports/AI_CRITIQUE.md` theo trải nghiệm thật của bạn, giữ phần phản biện 200–300 từ. Bản hiện tại là AI soạn, chưa được xác nhận là ý kiến của bạn.

## 2. Chuẩn bị và chạy một pilot trước

Đọc `usability/PROTOCOL.md`. Pilot là phiên thử để sửa kịch bản/thời lượng trước P1–P7, không cộng vào 7 phiên chính thức. Dùng một người riêng cho pilot là cách tránh người tham gia đã quen luồng khi vào mẫu chính thức.

Giữ SUT hiện tại, không sửa các bug đã biết trước phiên. Dữ liệu seed có AirPods Pro 2 giá 6 triệu; mục tiêu ngân sách 7 triệu trong kịch bản là khả thi. Mỗi phiên mở cửa sổ riêng tư mới, giỏ trống. Không cần đăng ký, đăng nhập hay thanh toán.

Đọc cho người pilot mục tiêu này, không hướng dẫn nút bấm:

> Bạn muốn mua một chiếc tai nghe để nghe nhạc và có ngân sách tối đa 7 triệu đồng. Hãy dùng cửa hàng này để chọn sản phẩm phù hợp, xem những thông tin bạn cần trước khi quyết định, rồi cho một chiếc vào giỏ. Bạn dừng khi tin rằng giỏ hàng đã đúng. Chưa cần đặt hàng hay thanh toán.

Ghi ngày giờ, người pilot, sự đồng ý tham gia/ghi hình/ghi âm, vấn đề gặp phải, thời lượng thật, điều chỉnh kịch bản sau pilot vào `usability/sessions/PILOT.md`. Nếu không cần chỉnh thì ghi điều đó sau khi đã chạy, không để nguyên mẫu trống.

## 3. Tuyển 7 người thật ngoài lớp và điều hành 7 phiên riêng

Người đang học cùng lớp môn này không hợp lệ. Ưu tiên người có mua sắm trực tuyến, không làm IT/testing. Có thể mời trực tiếp bạn bè/người thân phù hợp. Bạn tự liên hệ; Codex chưa gửi lời mời cho ai.

Câu mời có thể dùng:

> Mình đang làm bài kiểm thử giao diện cửa hàng demo. Bạn có thể dành khoảng 15–20 phút thao tác một nhiệm vụ mua hàng rồi trả lời vài câu hỏi không? Mình kiểm tra sản phẩm, không đánh giá bạn. Nếu bạn đồng ý, mình xin ghi màn hình; quyền ghi âm sẽ hỏi riêng. Giảng viên có thể liên hệ xác minh việc tham gia.

Điền P1–P7 trong `usability/participants.csv`: họ tên thật, liên hệ đã che 4 số giữa, xác nhận ngoài lớp, nghề/ngành hoặc kinh nghiệm phù hợp, ngày giờ phiên, quyền ghi hình và quyền ghi âm. Ví dụ **định dạng** SĐT: `090****123`; không dùng ví dụ làm thông tin người tham gia. Giữ liên hệ gốc riêng tại `usability/private/` nếu cần cho TA xác minh, không đưa vào GitHub/ZIP.

Mỗi phiên làm lần lượt:

1. Mở cửa sổ riêng tư mới vào SUT, giỏ trống. Dùng cùng máy/browser và kích thước đã chọn cho các phiên; ghi lại môi trường.
2. Xin đồng ý tham gia, ghi hình và ghi âm riêng. Nói: “Mình đang kiểm tra sản phẩm, không kiểm tra năng lực của bạn. Bạn cứ nói ra điều đang nghĩ khi thao tác.”
3. Bắt đầu quay màn hình nếu được đồng ý. Trên Mac bấm **Shift–Command–5**, chọn vùng ghi và Record. Chỉ bật microphone khi người tham gia đồng ý. Tránh quay thông báo và cửa sổ cá nhân. [Hướng dẫn Apple](https://support.apple.com/en-gb/102618).
4. Đọc nguyên văn mục tiêu đã chốt sau pilot. Bắt đầu bấm giờ khi người tham gia thao tác. Không nói trước lỗi, sản phẩm cần chọn hoặc việc phải bấm Thêm lần thứ hai.
5. Quan sát và ghi mốc thời gian, thao tác, do dự, lỗi, câu nói nguyên văn. Có thể hỏi “Bạn đang nghĩ gì?”. Chỉ hỗ trợ khi họ thực sự bị chặn; ghi chính xác lời hỗ trợ và thời điểm.
6. Kết thúc khi họ tuyên bố xong và bạn đã ghi nhận trạng thái giỏ, hoặc họ dừng/bị chặn/hết 10 phút theo protocol. Ghi đúng kết quả độc lập/có hỗ trợ/bị chặn/dừng; không tự chuyển lỗi thành thành công.
7. Cho điền SUS ngay sau thao tác, rồi hỏi bốn câu mở ở bước 4 dưới đây. Lưu ghi chú và bằng chứng vào phiên tương ứng.
8. Sau phiên thật, tạo một commit cho phiên đó. Nếu chưa quen Git, gửi dữ liệu cho Codex ngay sau mỗi phiên để Codex kiểm tra và commit. Không đợi đủ bảy phiên rồi tạo lịch sử như thể đã commit từng phiên từ trước.

Sửa `usability/sessions/P1.md` đến `P7.md` bằng quan sát thực tế. Lưu video thực tế riêng tại `usability/private/recordings/`, ghi đường dẫn trong ghi chú. Trước khi nộp, Codex sẽ chuẩn bị bản bằng chứng phù hợp kích thước/quyền riêng tư; không xóa bản gốc. Thư mục `private/` được bỏ khỏi Git và ZIP tự động hiện tại, nên phải báo đường dẫn cho Codex để xử lý, không chỉ để video ở đó rồi coi như đã đính kèm bài.

Nếu làm qua cuộc gọi, người tham gia dùng máy SUT của bạn qua chia sẻ/điều khiển màn hình hoặc một môi trường thử đã chuẩn bị; `localhost` của họ không tự trỏ tới máy bạn. Cách ít thiết lập nhất là cho từng người dùng trực tiếp cùng máy bạn. Bài không yêu cầu mua hàng hoặc nhập thông tin thanh toán thật.

## 4. Thu SUS và trả lời mở, không cần tự tính

Đưa `usability/SUS_QUESTIONNAIRE.md` cho từng người sau thao tác. Mỗi người trả lời đủ 10 câu, mỗi câu một số nguyên 1–5. Giữ nguyên thứ tự và chiều câu hỏi. Không gợi ý mức điểm.

Ghi điểm gốc vào `usability/sus_responses.csv`, mỗi dòng P1–P7 có Q1–Q10. Bạn có thể nhập vào sheet `SUS` của Excel thay cho CSV rồi báo cho Codex dùng Excel làm nguồn; không cần nhập hai lần. Không thay ô trống bằng 0 hoặc 3.

Hỏi và ghi câu trả lời thực tế cho cả bốn chủ đề:

- Clarity: Thông tin/nhãn nào khó hiểu? Bạn nghĩ nó có nghĩa gì?
- Error recovery: Khi kết quả không như mong đợi, bạn đã thử làm gì?
- Speed: Đoạn nào mất thời gian nhất, phải chờ hoặc làm lại?
- Trust: Điều gì khiến bạn tin hoặc chưa tin sản phẩm, giá và số lượng trong giỏ?

Codex sẽ tính SUS từng người/trung bình, tổng hợp thời gian và tỉ lệ hoàn thành từ ghi chú, nhóm pain point, xếp severity và liên kết bug. Bạn không cần tự tính điểm hay viết lại toàn bộ báo cáo. Không phải người tham gia nào cũng cần cho điểm thấp hoặc phát hiện lỗi mới.

## 5. Tự quay video demo và đưa lên YouTube

Bạn đã chọn tự quay video dùng cho bài nộp. File `skills/gui-usability-evaluator/video/gui-g2-demo.mp4` chỉ là tài liệu tham khảo do Codex ghi; không được gán thành video bạn tự quay. Dùng kịch bản ở `skills/gui-usability-evaluator/DEMO.md` để chuẩn bị.

Có thể quay khoảng 3–5 phút theo nhịp sau (đây là thời lượng gợi ý, đề yêu cầu demo trọn màn hình/luồng):

1. 0:00–0:30: giới thiệu họ tên/MSSV, phạm vi G2 và mở file skill.
2. 0:30–1:00: cho agent đọc skill và đặc tả. Prompt gợi ý: “Dùng skill tại skills/gui-usability-evaluator/SKILL.md để kiểm thử luồng tìm tai nghe, xem chi tiết và thêm giỏ trên EShop localhost. Đối chiếu tiêu chí, ghi quan sát và bằng chứng thật.” Đây là mẫu để bạn dùng khi quay, không phải prompt đã diễn ra trong lịch sử cũ.
3. 1:00–3:00: ghi agent thực thi luồng thật từ đầu đến cuối; cho thấy tìm kiếm, mở chi tiết, thêm một lần và kiểm tra giỏ, sau đó thao tác thử lại theo bug đã ghi. Giải thích đúng quan sát bạn thấy trên video.
4. 3:00–4:00: mở kết quả checklist, ảnh G40, báo cáo B18 và Issue #18 để cho thấy cách truy vết bằng chứng.
5. Phần cuối: nêu ngắn cách tái sử dụng skill cho màn hình khác và một điểm bạn đã phản biện/sửa. Dừng ghi, mở lại video để kiểm tra chữ và âm thanh nếu có.

Để có URL theo yêu cầu đề: mở [YouTube Studio](https://studio.youtube.com/), dùng tài khoản của bạn, chọn Create → Upload videos, chọn bản video bạn tự quay, điền tiêu đề/mô tả đúng nội dung, hoàn tất các câu hỏi của YouTube, chọn **Unlisted** và lưu. Mở link bằng cửa sổ ẩn danh để kiểm tra người có link xem được. Gửi URL cho Codex để gắn vào README/báo cáo. Video này không thay cho bằng chứng các phiên usability. [Hướng dẫn tải video](https://support.google.com/youtube/answer/57407?co=GENIE.Platform%3DDesktop&hl=en), [quyền xem Unlisted](https://support.google.com/youtube/answer/157177).

Theo lựa chọn hiện tại, Codex không đăng video tham khảo lên YouTube. Khi chưa có video/URL thật của bạn, báo cáo vẫn ghi thiếu phần này.

## 6. Xác nhận audit, quyền xem GitHub và tự chấm

Đã khôi phục 14 lời nhắn ngày 03/11 và ba đầu ra kế hoạch nguyên gốc từ OpenCode đúng dự án, lưu ở `reports/AI_AUDIT_RECOVERED.md` và `reports/legacy/`. Bạn chỉ cần kiểm tra và bổ sung nếu còn dùng AI/công cụ/chat khác cho HW03 ngoài những bản đã khôi phục và chat Codex hiện tại.

Repo [NgBaoAnn/hw03-gui-usability](https://github.com/NgBaoAnn/hw03-gui-usability) đã public theo yêu cầu của bạn; người chấm có thể mở Issues và ảnh. Không đưa danh sách liên hệ gốc của người tham gia vào repo public. Các bug và ảnh gốc cũng có trong ZIP.

Tự chấm khi đã đọc và hiểu bài theo bốn khoản: Task 1 tối đa 30, Task 2 tối đa 40, Task 3 tối đa 20, skill/demo tối đa 10. Gửi bốn điểm và lý do ngắn; tổng là điểm ba chữ số dùng đặt tên ZIP. Codex sẽ kiểm tra tổng và đồng bộ bảng tự chấm, không ký xác nhận thay bạn.

## 7. Gửi lại cho Codex để chốt hồ sơ

Bạn có thể gửi mẫu sau trong chat, kèm đường dẫn các file đã điền:

```text
Tôi đã rà soát bài; ghi chú tại checklists/HUMAN_REVIEW.md.
Các mục tôi tự bổ sung: [ID/nội dung, lý do AI bỏ sót, quan sát/ảnh].
Pilot: usability/sessions/PILOT.md.
7 phiên: usability/sessions/P1.md ... P7.md.
Danh sách liên hệ đã che: usability/participants.csv.
Điểm SUS gốc ở: [CSV hoặc Excel, chọn một nguồn].
Video/ghi chú gốc ở: [đường dẫn trên máy].
YouTube demo: [URL thật].
AI Critique đã sửa tại: reports/AI_CRITIQUE.md.
Tôi đã kiểm tra audit cũ; [không có thêm / còn chat ở ...].
Quyền GitHub cho người chấm: repo đã public.
Tự chấm: Task1=.../30; Task2=.../40; Task3=.../20; Skill=.../10.
```

Sau khi có dữ liệu, Codex sẽ kiểm tra thiếu/sai, bổ sung thực thi checklist, tính SUS, phân tích kết quả, cập nhật bug/Issues nếu có, xuất lại Markdown/PDF/Excel/Git log và đóng ZIP cuối theo tên `23120207_HW03_AI_GUIUsability_<điểm 000–100>.zip`. Bộ hồ sơ đầy đủ mới được trình bạn xác nhận để nộp.

Link nộp: https://courses.fit.hcmus.edu.vn/mod/assign/view.php?id=129903. Khi nộp bài cá nhân, xác nhận **“Em làm một mình”** trong mục Thành viên nhóm. Kiểm tra trạng thái cuối trên Moodle; tệp upload hoặc bản nháp không tự chứng minh đã nộp hoàn tất.
