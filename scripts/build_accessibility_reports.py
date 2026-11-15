"""Validate new measurements independently and build the checklist supplement."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def ratio(a,b):
    def lum(rgb):
        v=[x/255 for x in rgb]
        return sum((x/12.92 if x<=0.04045 else ((x+0.055)/1.055)**2.4)*w for x,w in zip(v,[.2126,.7152,.0722]))
    x,y=lum(a),lum(b)
    return (max(x,y)+.05)/(min(x,y)+.05)


def main():
    assert ratio([0,0,0],[255,255,255])==21 and ratio([24]*3,[24]*3)==1
    items=json.loads((ROOT/'checklists/additions.json').read_text())
    assert [r[0] for r in items]==['G49','G50','G51']
    records={}
    for engine in ['chrome','firefox','safari']:
        records[engine]=[]
        for gid,*_ in items:
            p=ROOT/f'evidence/accessibility/{engine}/{gid}.json';r=json.loads(p.read_text());o=r['observation']
            assert r['engine']==engine and r['id']==gid and p.with_suffix('.png').is_file()
            if gid=='G49':passed=o['declaredLanguage'].lower().split('-')[0]=='vi'
            else:
                computed=ratio(o['foreground'],o['background']);assert abs(computed-o['contrast'])<1e-9
                large=o['fontSizePx']>=24 or (int(o['fontWeight'])>=700 and o['fontSizePx']>=56/3)
                assert o['largeText']==large and o['minimum']==(3 if large else 4.5)
                passed=computed>=o['minimum']
            assert r['status']==('Passed' if passed else 'Failed')
            r['evidence']=str(p.with_suffix('.png').relative_to(ROOT));records[engine].append(r)
    (ROOT/'evidence/accessibility/results.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    assert all(r['status']=='Failed' for rows in records.values() for r in rows),'This report describes the recorded failing snapshot; revise narrative for a new SUT revision.'
    folder=ROOT/'bug-reports/supplement';folder.mkdir(exist_ok=True)
    issues=json.loads((folder/'issues.json').read_text()) if (folder/'issues.json').exists() else {}
    groups=[('B24','Trang tiếng Việt khai báo ngôn ngữ mặc định en',['G49'],'Mở Home, đọc document.documentElement.lang; đối chiếu nội dung tiếng Việt.','Ngôn ngữ mặc định vi hoặc vi-VN tương ứng nội dung.','lang=en trên cả ba browser. Chưa kiểm tra phát âm bằng screen reader thật.','https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html'),('B25','Chữ giá và chữ nút thêm giỏ thiếu tương phản',['G50','G51'],'Đọc computed color/background/font size/weight trên chữ giá Home và nút thêm giỏ Detail ở trạng thái mặc định.','Chữ 16px: tương phản tối thiểu 4.5:1. Không làm tròn tỷ lệ trước khi so ngưỡng.','Home: rgb(239,68,68) trên trắng, 16px/700, tỷ lệ 3.763127680148142. Nút: trắng trên rgb(22,163,74), 16px/400, tỷ lệ 3.2957336053312796. Cùng kết quả trên ba browser.','https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html')]
    catalog=[]
    for bid,title,ids,steps,expected,actual,source in groups:
        screenshots=[r['evidence'] for rows in records.values() for r in rows if r['id'] in ids]
        body=f'''# {bid}: {title}

Severity: **Major** (AI đề xuất). Checklist bổ sung: {', '.join(ids)}. Tác giả bổ sung: Codex theo yêu cầu sinh viên; chưa gán thành mục sinh viên tự phát hiện.

Nguồn kỳ vọng: WCAG accessibility heuristic, chưa có tuyên bố SUT cam kết đạt WCAG. {source}

Tiền điều kiện: SUT revision `{records['safari'][0]['sutCommit']}`; browser native Chrome, Firefox Playwright build, Safari 26.2 trên macOS 26.2. Bằng chứng có UA; phiên bản OS trong UA được browser rút gọn, OS thực lấy từ sw_vers trong JSON.

Bước: {steps}

Kỳ vọng: {expected}

Thực tế: {actual}

Phương pháp: mở trang đo cùng origin qua CUA; iframe SUT chỉ được đọc DOM/CSS. Không sửa style/logic SUT, không gọi screen reader hay giả lập người tham gia. Màu CSS chuyển sang sRGB bằng canvas, lấy màu nền tổng hợp và tính độ sáng tương đối. Self-check đen/trắng=21, cùng màu=1; Python đối chiếu độc lập cả sáu phép đo tương phản. Đây là lỗi theo heuristic tiếp cận, không tự suy ra tác động thực nghiệm ở người dùng.

GitHub Issue: {issues.get(bid,{}).get('url','Chờ đăng')}

'''
        body+='\n'.join(f'![{bid} {Path(p).parent.name} {Path(p).stem}](../../{p})' for p in screenshots)+'\n'
        (folder/f'{bid}.md').write_text(body)
        catalog.append({'id':bid,'title':title,'severity':'Major','checks':ids,'file':f'bug-reports/supplement/{bid}.md','screenshots':screenshots})
    (folder/'catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
    report='''# Bổ sung checklist sau phản biện AI

Ba tiêu chí G49–G51 do Codex đề xuất/thực thi theo yêu cầu sinh viên. Giữ nguyên 48 tiêu chí đầu tại items.json; phần bổ sung AI ở additions.json. Ba mục này đóng góp 9 kết quả Failed. Sau khi AI bổ sung G52 theo yêu cầu sinh viên (kích thước vùng chạm; Passed trên ba browser), hồ sơ có tổng 52 tiêu chí và 156 kết quả: 59 Passed, 97 Failed; 33 tiêu chí fail ít nhất một môi trường, 25 nhóm bug GUI. G52 và đính chính nguồn đóng góp nằm tại HUMAN_REVIEW.md. Năm finding usability tách riêng, tổng 30 GitHub Issues khi đã đăng hai bug mới.

## Vì sao bổ sung

- G49: bộ đầu đo alt và liên kết nhãn nhưng bỏ qua ngôn ngữ tài liệu. Prompt tập trung thành phần nhìn thấy; metadata phục vụ công nghệ hỗ trợ không nổi bật trong ảnh.
- G50: bộ đầu kiểm ký hiệu tiền và bố cục nhưng chưa tính tương phản. Nhận xét màu đẹp/nhìn rõ bằng mắt của AI không thay được phép đo định lượng.
- G51: G11 kiểm quy chuẩn màu xanh dương, G41 kiểm phản hồi thêm thành công. Cả hai không trả lời chữ nút có đủ tương phản hay không; việc thêm kiểm tra này tránh đánh đồng màu đúng chuẩn với dễ đọc.

## Kết quả thực thi

| ID | IA | Màn hình | Chrome | Firefox | Safari | Quan sát |
|---|---|---|---|---|---|---|
'''
    for gid,ia,screen,criterion,ref in items:
        o=next(r for r in records['safari'] if r['id']==gid)['observation']
        observation='lang=en; nội dung tiếng Việt' if gid=='G49' else f"{o['contrast']:.4f}:1 < {o['minimum']}:1; {o['fontSizePx']}px, weight {o['fontWeight']}"
        statuses=[next(r['status'] for r in records[e] if r['id']==gid) for e in records]
        report+='| '+' | '.join([gid,ia,screen,*statuses,observation])+' |\n'
    report+='\n## Bằng chứng và giới hạn\n\nĐã mở các case qua native CUA trên ba browser; JSON gửi về collector localhost, ảnh chụp cửa sổ thật. Trang đo tự kiểm tra công thức trước khi gửi; collector chỉ lưu bản ghi thực tế. Không bật lại Safari Remote Automation. Không suy ra ngôn ngữ đọc thực tế của screen reader. Ảnh chụp có email/tên/MSSV và URL localhost; metadata môi trường đầy đủ ở JSON. Các tiêu chí là WCAG heuristic ngoài cam kết FR của SUT.\n\n'
    for bug in catalog:
        report+=f"- [{bug['id']}: {bug['title']}](../{bug['file']}); Issue: {issues.get(bug['id'],{}).get('url','Chờ đăng')}.\n"
    report+='\nNguồn: [WCAG 3.1.1](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html), [WCAG 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).\n'
    (ROOT/'checklists/ADDITIONS.md').write_text(report)
    print('Verified 9 actual results; built 3 supplementary criteria and 2 bug groups.')


if __name__=='__main__':main()
