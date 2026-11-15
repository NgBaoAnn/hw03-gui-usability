// Reproduce supplied usability findings; this is not a human participant session.
const { chromium } = require('playwright');
const fs = require('node:fs/promises');
const assert = require('node:assert/strict');
const { execFileSync } = require('node:child_process');
(async () => {
  execFileSync('python3', ['-c', `import sqlite3
c=sqlite3.connect('.work/sut/backend/database.sqlite')
u=c.execute('SELECT id FROM users WHERE email=?',('hw03-recheck@example.test',)).fetchone()
if not u:
 c.execute('INSERT INTO users(name,email,password,role) VALUES(?,?,?,?)',('HW03 local fixture','hw03-recheck@example.test','Hw03Fixture123!','user'))
 u=(c.execute('SELECT last_insert_rowid()').fetchone()[0],)
c.execute('DELETE FROM orders WHERE user_id=?',u)
for amount,status in [(28000000,'pending'),(1500000,'confirmed'),(45000000,'shipping'),(30000000,'delivered')]:
 c.execute('INSERT INTO orders(user_id,total_amount,status,shipping_address) VALUES(?,?,?,?)',(u[0],amount,status,'HW03 isolated fixture'))
c.commit();c.close()`]);
  await fs.mkdir('evidence/usability', { recursive: true });
  const browser = await chromium.launch({ channel: 'chrome' });
  try {
    const page = await browser.newPage({ viewport: { width: 1366, height: 1000 }, locale: 'vi-VN' });
    const records = [];
    const shot = async (id, observation) => {
      const timestamp = new Date().toISOString();
      await page.evaluate(({id, timestamp, version}) => {
        document.querySelector('#hw03-evidence')?.remove();
        const el = document.createElement('div'); el.id='hw03-evidence';
        el.style.cssText='position:fixed;bottom:0;left:0;right:0;padding:12px;background:#111827;color:white;font:14px/1.5 Arial;z-index:2147483647';
        el.textContent=`${id} | 23120207@student.hcmus.edu.vn | Nguyễn Bảo An | MSSV 23120207 | Chrome ${version} / macOS | ${location.href} | ${timestamp} | Agent tái hiện trên fixture, không phải phiên người tham gia`;
        document.body.append(el);
      }, { id, timestamp, version: browser.version() });
      const evidence=`evidence/usability/${id}.png`;
      await page.screenshot({ path: evidence, fullPage: true });
      records.push({ id, timestamp, observation, evidence, url: page.url() });
    };
    await page.goto('http://localhost:5173/login');
    assert.equal(await page.locator('main h2').innerText(), 'Đăng Ký');
    await shot('U02', 'Route /login có heading Đăng Ký; không phải form đăng ký.');
    const inputs=page.locator('main input');
    await inputs.nth(0).fill('hw03-recheck@example.test');
    await inputs.nth(1).fill('Hw03Fixture123!');
    await page.locator('main form button').click();
    await page.waitForURL('http://localhost:5173/');
    const profileLink=page.locator('a[href="/profile"]');
    await profileLink.waitFor();
    assert((await profileLink.innerText()).includes('Chào'));
    await shot('U01', `Link /profile có nhãn ${await profileLink.innerText()}; không có nhãn Đơn hàng của tôi.`);
    await profileLink.click();
    await page.waitForURL('**/profile');
    await page.locator('tbody tr').nth(3).waitFor();
    const shipping=page.locator('tbody tr').filter({ hasText: 'Đang giao' });
    assert.equal(await shipping.getByRole('button',{name:'Hủy đơn',exact:true}).count(),1);
    await shot('U03', 'Dòng Đang giao vẫn có nút Hủy đơn; chỉ chứng minh affordance UI, chưa khẳng định backend cho hủy shipping.');
    const headers=await page.locator('th').allTextContents();
    assert.deepEqual(headers.map(x=>x.trim()),['Mã ĐH','Ngày đặt','Tổng tiền','Trạng thái','Thao tác']);
    await shot('U05', 'Danh sách đơn không hiển thị tên/ảnh sản phẩm; đây là đề xuất UX, không phải vi phạm FR đã chứng minh.');
    const dialogs=[];
    page.on('dialog', async d=>{dialogs.push({type:d.type(),message:d.message()});await d.accept();});
    const pending=page.locator('tbody tr').filter({hasText:'Chờ xác nhận'});
    await pending.getByRole('button',{name:'Hủy đơn',exact:true}).click();
    await page.getByText('Đã hủy',{exact:true}).waitFor();
    assert.deepEqual(dialogs.map(d=>d.type),['alert']);
    assert.equal(await page.getByRole('dialog').count(),0);
    await shot('U04', `Một click hủy pending; chỉ có alert sau thao tác, không có confirm trước thao tác. Dialog log: ${JSON.stringify(dialogs)}`);
    await fs.writeFile('evidence/usability/recheck.json',JSON.stringify({timestamp:new Date().toISOString(),browser:browser.version(),sutCommit:execFileSync('git',['-C','.work/sut','rev-parse','HEAD'],{encoding:'utf8'}).trim(),method:'Agent recheck with four SQLite fixture orders in isolated clone; no human sessions, no original participant recordings.',results:records},null,2)+'\n');
    console.log(records.map(r=>r.id).join(', '),'reproduced');
  } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
