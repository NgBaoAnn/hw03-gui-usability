// Record a genuine browser walkthrough of the delivered skill's testing workflow.
const {chromium}=require('playwright');
const fs=require('node:fs/promises');
const assert=require('node:assert/strict');
const crypto=require('node:crypto');
const {execFileSync}=require('node:child_process');
const path=require('node:path');
const base='http://localhost:5173';
const out='skills/gui-usability-evaluator/video';
const esc=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');

(async()=>{
  await fs.mkdir(out,{recursive:true});
  const skill=await fs.readFile('skills/gui-usability-evaluator/SKILL.md','utf8');
  const items=JSON.parse(await fs.readFile('checklists/items.json','utf8'));
  const bug=await fs.readFile('bug-reports/B18.md','utf8');
  assert(items.length>40 && bug.includes('Lần bấm'));
  const browser=await chromium.launch({channel:'chrome'});
  const context=await browser.newContext({viewport:{width:1280,height:800},locale:'vi-VN',recordVideo:{dir:'.work/demo-video',size:{width:1280,height:800}}});
  const page=await context.newPage();page.setDefaultTimeout(10000);
  const video=page.video();const steps=[];const started=new Date().toISOString();
  const slide=async(title,body)=>{
    await page.setContent(`<html lang="vi"><meta charset="utf-8"><style>body{margin:0;padding:42px;background:#102038;color:#eef4ff;font:22px/1.5 Arial;box-sizing:border-box}h1{font-size:34px;color:#fff;margin:0 0 22px}h2{font-size:25px;color:#a6c9ff}pre{white-space:pre-wrap;font:18px/1.5 Arial;background:#172d4d;padding:20px}p{margin:12px 0}.small{font-size:18px;color:#bed0e6}</style><h1>${esc(title)}</h1>${body}</html>`);
  };
  const stage=async(label,observation,hold=7000)=>{
    steps.push({at:new Date().toISOString(),label,observation,url:page.url()});
    await page.evaluate(({label,observation})=>{
      document.getElementById('hw03-demo-caption')?.remove();
      const p=document.createElement('aside');p.id='hw03-demo-caption';p.style.cssText='position:fixed;bottom:0;left:0;right:0;padding:14px 24px;background:#102038;color:white;font:18px/1.4 Arial;z-index:2147483647;border-top:3px solid #93bfff;pointer-events:none';
      for(const t of ['DEMO DO CODEX GHI | 23120207@student.hcmus.edu.vn | Nguyễn Bảo An',label,observation]){const line=document.createElement('div');line.textContent=t;p.append(line);}document.body.append(p);
    },{label,observation});
    await page.waitForTimeout(hold);
  };
  const search=async()=>{
    const response=page.waitForResponse(r=>r.url().includes('/api/products?search=')&&r.status()===200);
    await page.getByPlaceholder('Tìm kiếm...').fill('Tai nghe');await page.getByPlaceholder('Tìm kiếm...').press('Enter');await response;
    await page.getByRole('heading',{level:2,name:'Tai nghe AirPods Pro 2',exact:true}).waitFor();
    assert.equal(await page.locator('main h2').count(),1);
  };
  const openDetail=async()=>{
    await page.getByRole('link',{name:'Xem chi tiết',exact:true}).click();
    await page.waitForURL('**/product/4');await page.locator('main input[type=number]').waitFor();
  };
  const cart=async()=>{
    await page.getByRole('link',{name:'Giỏ hàng',exact:true}).click();await page.waitForURL('**/cart');await page.locator('main h2').waitFor();
  };
  try{
    await slide('HW03 G2 - Demo skill GUI & Usability',`<p>Quy trình kiểm thử do Codex thực hiện theo <b>gui-usability-evaluator</b>.</p><p>Luồng đầy đủ: tìm tai nghe → xem chi tiết → thêm vào giỏ → kiểm chứng kết quả → báo cáo lỗi.</p><p class="small">Nguồn hình: browser thật chạy EShop localhost. Phụ đề mô tả thao tác kiểm thử tự động. Video không có âm thanh.</p>`);
    await stage('1. Xác định mục tiêu và nguồn kiểm thử','SUT EShop; FR-05/FR-06/FR-07; không có dữ liệu người tham gia trong video.',9000);
    const excerpt=skill.split('\n\n').filter(x=>x.startsWith('Read the provided')||x.startsWith('Execute on the actual')||x.startsWith('Prepare one goal')).join('\n\n');
    await slide('Đọc skill được nộp cùng bài',`<p class="small">Trích nguyên văn từ skills/gui-usability-evaluator/SKILL.md</p><pre>${esc(excerpt)}</pre>`);
    await page.waitForTimeout(13000);
    await page.goto(base);await page.locator('main h2').first().waitFor();
    const home=await page.evaluate(()=>({h1:document.querySelectorAll('main h1').length,emptyAlt:Array.from(document.querySelectorAll('main img')).filter(e=>!e.alt).length}));
    assert.equal(home.h1,2);assert.equal(home.emptyAlt,5);
    await stage('2. Đối chiếu checklist trên trang danh sách',`Quan sát thật: ${home.h1} thẻ h1; ${home.emptyAlt} ảnh có alt rỗng. Liên kết G01/G12 và B01/B06.`,9000);
    await search();
    await stage('3. Tìm sản phẩm theo nhu cầu','Từ khóa “Tai nghe” cho đúng 1 kết quả: AirPods Pro 2, giá 6.000.000 ₫.',8000);
    await openDetail();
    assert.equal(await page.locator('main h1').innerText(),'Tai nghe AirPods Pro 2');
    assert.equal(await page.locator('main input[type=number]').inputValue(),'1');
    await stage('4. Mở chi tiết và kiểm tra dữ liệu','Tên đúng sản phẩm đã chọn; số lượng mặc định 1; mục tiêu thêm đúng một sản phẩm.',8000);
    await page.getByRole('button',{name:'Thêm vào giỏ hàng',exact:true}).click();
    await stage('5. Bấm Thêm vào giỏ hàng đúng một lần','Không xuất hiện phản hồi thành công sau click đầu. Tiếp theo mở giỏ để kiểm chứng.',6000);
    await cart();assert.equal(await page.locator('tbody tr').count(),0);
    await stage('6. Xác nhận lỗi bằng trạng thái giỏ thật','Giỏ trống sau một click: tái hiện B18 / G40. Đây là lỗi SUT được ghi vào GitHub Issue #18.',10000);
    await page.getByRole('link',{name:'Tiếp tục mua sắm',exact:true}).click();await page.locator('main h2').first().waitFor();
    await search();await openDetail();
    await page.getByRole('button',{name:'Thêm vào giỏ hàng',exact:true}).click();
    await page.getByRole('button',{name:'Thêm vào giỏ hàng',exact:true}).click();
    assert.equal(await page.getByRole('button',{name:'Đã thêm',exact:true}).count(),1);
    await stage('7. Thử lại với hai click trong cùng trang chi tiết','Click thứ hai mới hiển thị “Đã thêm”. Workaround này được ghi rõ, không đổi kết quả Failed của click đầu.',7000);
    await cart();assert.equal(await page.locator('tbody tr').count(),1);
    const cells=await page.locator('tbody tr').first().locator('td').allTextContents();
    assert(cells[0].includes('AirPods'));assert.equal(cells[2],'1');
    await stage('8. Hoàn tất luồng và xác nhận giỏ','Giỏ có 1 dòng AirPods Pro 2, số lượng 1, thành tiền 6.000.000 ₫. Luồng đã được thực thi từ đầu đến cuối.',9000);
    await slide('Ghi bằng chứng và báo cáo lỗi',`<h2>B18: Lần bấm Thêm đầu tiên ở chi tiết không làm gì</h2><p><b>Bước:</b> Mở chi tiết → bấm một lần → mở giỏ.</p><p><b>Kỳ vọng:</b> Giỏ có sản phẩm ngay sau một lần bấm.</p><p><b>Thực tế trong video:</b> Giỏ trống; lần bấm thứ hai mới thêm.</p><p class="small">Ảnh gốc: evidence/gui/chrome/G40.png<br>Markdown: bug-reports/B18.md<br>Issue: https://github.com/NgBaoAnn/hw03-gui-usability/issues/18</p>`);
    await page.waitForTimeout(12000);
    await slide('Kết quả và khả năng tái sử dụng',`<p>Skill đã dẫn quy trình: đọc yêu cầu, chọn tiêu chí, thực thi luồng thật, kiểm tra dữ liệu và ghi bằng chứng.</p><p>Checklist hiện có 48 mục trên Chrome, Firefox và Safari thật; 23 nhóm bug được truy vết tới ảnh và Issue.</p><p class="small">Khi dùng cho màn hình khác: đọc đặc tả và quan sát SUT trước khi chỉnh tiêu chí. Phiên usability cần dữ liệu người thật ngoài lớp.</p>`);
    await page.waitForTimeout(10000);
  }finally{await context.close();await browser.close();}
  const source=await video.path();
  execFileSync('ffmpeg',['-y','-i',source,'-vf','scale=960:600','-r','20','-c:v','libx264','-preset','fast','-crf','28','-pix_fmt','yuv420p','-movflags','+faststart','-an',path.join(out,'gui-g2-demo.mp4')],{stdio:'ignore'});
  const meta={recordedBy:'Codex, actual Google Chrome/EShop browser session',started,finished:new Date().toISOString(),skillSha256:crypto.createHash('sha256').update(skill).digest('hex'),source:'Live browser recording, no participant impersonation',steps};
  await fs.writeFile(path.join(out,'recording-log.json'),JSON.stringify(meta,null,2)+'\n');
  console.log('Recorded actual skill workflow:',path.join(out,'gui-g2-demo.mp4'));
})().catch(e=>{console.error(e);process.exitCode=1;});
