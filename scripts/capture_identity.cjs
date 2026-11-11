// Identity evidence in a real, unsubmitted SUT form; creates no account.
const { chromium, firefox }=require('playwright');
const fs=require('node:fs/promises');
const assert=require('node:assert/strict');
const { execFileSync }=require('node:child_process');
(async()=>{
  await fs.mkdir('evidence/identity',{recursive:true});
  for(const name of ['chrome','firefox']){
    const browser=name==='chrome'?await chromium.launch({channel:'chrome'}):await firefox.launch();
    try{
      const page=await browser.newPage({viewport:{width:1280,height:1000}});
      await page.goto('http://localhost:5173/register');
      const inputs=page.locator('main form input');
      await inputs.nth(0).fill('Nguyễn Bảo An (MSSV: 23120207)');
      await inputs.nth(1).fill('23120207@student.hcmus.edu.vn');
      assert.equal(await inputs.nth(0).inputValue(),'Nguyễn Bảo An (MSSV: 23120207)');
      assert.equal(await inputs.nth(1).inputValue(),'23120207@student.hcmus.edu.vn');
      assert.equal(await inputs.nth(2).inputValue(),'');
      await page.evaluate(({name,version,os})=>{
        const p=document.createElement('div');p.style.cssText='position:fixed;bottom:0;left:0;right:0;padding:14px;background:#111827;color:white;font:14px/1.5 Arial;z-index:2147483647';
        p.textContent=`23120207@student.hcmus.edu.vn | Nguyễn Bảo An | MSSV: 23120207 | ${name} ${version} | macOS ${os} | ${location.href} | ${new Date().toISOString()} | Form định danh chưa gửi, không tạo tài khoản`;
        document.body.append(p);
      },{name,version:browser.version(),os:execFileSync('sw_vers',['-productVersion'],{encoding:'utf8'}).trim()});
      await page.screenshot({path:`evidence/identity/${name}.png`,fullPage:true});
      console.log(name,'identity form captured, no submission');
    }finally{await browser.close();}
  }
})().catch(e=>{console.error(e);process.exitCode=1;});
