// Run with an installed Playwright module on NODE_PATH. Never patches SUT behavior.
const { chromium, firefox, webkit } = require('playwright');
const fs = require('node:fs/promises');
const os = require('node:os');
const assert = require('node:assert/strict');
const { execFileSync } = require('node:child_process');
const items = require('../checklists/items.json');
const base = 'http://localhost:5173';
const productsUrl = 'http://localhost:3000/api/products';
const [engine = 'chrome'] = process.argv.slice(2);
assert(['chrome', 'firefox', 'webkit'].includes(engine), 'Unknown browser');
assert(items.length > 40 && new Set(items.map(x => x[0])).size === items.length);
assert(new Set(items.map(x => x[1])).size === 4);

async function main() {
  const browser = engine === 'chrome'
    ? await chromium.launch({ channel: 'chrome', headless: true })
    : await ({ firefox, webkit }[engine]).launch({ headless: true });
  const browserName = engine === 'chrome' ? 'Google Chrome' : engine === 'firefox' ? 'Firefox (Playwright build)' : 'Playwright WebKit (NOT Safari)';
  const env = `${browserName} ${browser.version()} / macOS ${execFileSync('sw_vers',['-productVersion'],{encoding:'utf8'}).trim()} (Darwin ${os.release()})`;
  const products = await (await fetch(productsUrl)).json();
  assert(products.length > 0 && products.some(x => x.id === 1));
  const dir = `evidence/gui/${engine}`;
  await fs.mkdir(dir, { recursive: true });
  const results = [];
  for (const [id, aspect, screen, criterion, reference] of items) {
    const context = await browser.newContext({ viewport: { width: 1280, height: 900 }, locale: 'vi-VN' });
    const page = await context.newPage();
    page.setDefaultTimeout(6000);
    let actual = '', passed = false, state = 'Executed', evidence = '';
    const observations = [];
    page.on('console', m => { if (m.type() === 'error') observations.push(m.text()); });
    const home = async () => { await page.goto(base); await page.locator('main h2').first().waitFor(); };
    const detail = async (pid = 1) => { await page.goto(`${base}/product/${pid}`); await page.locator('main input[type=number]').waitFor(); };
    const cart = async () => {
      await page.getByRole('link', { name: 'Giỏ hàng', exact: true }).click();
      await page.waitForURL('**/cart');
      await page.getByRole('heading', { name: /^Giỏ Hàng$|^Giỏ hàng của bạn đang trống$/ }).waitFor();
    };
    const search = async q => {
      const done = page.waitForResponse(r => r.url().startsWith(productsUrl) && r.request().method() === 'GET');
      await page.getByPlaceholder('Tìm kiếm...').fill(q);
      await page.getByPlaceholder('Tìm kiếm...').press('Enter');
      await done;
      await page.waitForTimeout(150);
    };
    const addHome = async () => { await home(); await page.getByRole('button', { name: 'Thêm vào giỏ', exact: true }).first().click(); };
    const check = (condition, value) => { passed = Boolean(condition); actual = String(value); };
    const text = () => page.locator('main').innerText();
    const label = l => l.evaluate(el => Boolean(el.labels?.length || el.getAttribute('aria-label') || el.getAttribute('aria-labelledby')));
    const hasEmptyIllustration = () => page.locator('main img, main svg, main [role=img]').count();
    try {
      switch (id) {
        case 'G01': await home(); {const n=await page.locator('main h1').count();check(n===1,`h1=${n}`);} break;
        case 'G02': await detail(); {const n=await page.locator('main h1').count();check(n===1 && await page.locator('main h1').innerText()===products[0].name,`h1=${n}; ${await page.locator('main h1').innerText()}`);} break;
        case 'G03': await addHome(); await cart(); {const n=await page.locator('main h1').count();check(n===1,`h1=${n}`);} break;
        case 'G04': await home(); {const t=await page.locator('main .text-red-500').first().innerText();check(t.includes('₫') && /[.,]/.test(t),t);} break;
        case 'G05': await detail(); {const t=await page.locator('main .text-red-600').first().innerText();check(t.includes('₫') && t.replace(/\D/g,'')===String(products[0].price),t);} break;
        case 'G06': await detail(); {const t=await text();check(t.includes(products[0].name)&&t.includes(products[0].description),t);} break;
        case 'G07': await home(); {await page.locator('main img').first().evaluate(img=>img.decode().catch(()=>{}));const r=await page.locator('main img').first().evaluate(el=>({fit:getComputedStyle(el).objectFit,w:el.clientWidth,h:el.clientHeight,nw:el.naturalWidth,nh:el.naturalHeight}));check(r.nw>0 && (r.fit!=='cover'||Math.abs(r.w/r.h-r.nw/r.nh)<0.05),JSON.stringify(r));} break;
        case 'G08': case 'G09': if(id==='G09')await page.setViewportSize({width:390,height:844});await home(); {const r=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth}));check(r.scroll<=r.width,JSON.stringify(r));} break;
        case 'G10': await page.setViewportSize({width:390,height:844});await detail(); {const b=await page.getByRole('button',{name:'Thêm vào giỏ hàng',exact:true}).boundingBox();check(b.x>=0 && b.x+b.width<=390,JSON.stringify(b));} break;
        case 'G11': await detail(); {const c=await page.getByRole('button',{name:'Thêm vào giỏ hàng',exact:true}).evaluate(el=>getComputedStyle(el).backgroundColor);check(c==='rgb(37, 99, 235)',c);} break;
        case 'G12': await home(); {const a=await page.locator('main img').evaluateAll(es=>es.map(x=>x.alt));check(a.every(x=>x.trim()),JSON.stringify(a));} break;
        case 'G13': await home();check(await label(page.getByPlaceholder('Tìm kiếm...')),'label/aria association='+await label(page.getByPlaceholder('Tìm kiếm...')));break;
        case 'G14': await home();await search('iPhone'); {const names=await page.locator('main h2').allTextContents();check(names.length>0&&names.every(n=>n.includes('iPhone')),JSON.stringify(names));} break;
        case 'G15': await home();await search('iPhone');await search(''); {const n=await page.locator('main h2').count();check(n===products.length,`products=${n}`);} break;
        case 'G16': await home();await search('iPhone&limit=1'); {const names=await page.locator('main h2').allTextContents();check(names.length===0,JSON.stringify(names));} break;
        case 'G17': await detail(); {const v=await page.locator('input[type=number]').inputValue();check(v==='1',v);} break;
        case 'G18': case 'G19': case 'G20': case 'G21': case 'G22': {
          await detail();const value={G18:'2',G19:'0',G20:'-1',G21:'1.5',G22:''}[id];
          await page.locator('main input[type=number]').fill(value);
          await page.getByRole('button',{name:'Thêm vào giỏ hàng',exact:true}).click();
          await page.getByRole('button',{name:'Thêm vào giỏ hàng',exact:true}).click();
          await cart();const rows=await page.locator('tbody tr').count();
          const qty=rows?await page.locator('tbody tr').first().locator('td').nth(2).innerText():'';
          check(id==='G18'?rows===1&&qty==='2':rows===0,`input=${JSON.stringify(value)}; cart rows=${rows}; quantity=${qty}; ${await text()}`);
        } break;
        case 'G23': await detail();check(await label(page.locator('main input[type=number]')),'label/aria association='+await label(page.locator('main input[type=number]')));break;
        case 'G24': await home();await page.getByPlaceholder('Tìm kiếm...').fill('<b data-hw03-probe="1">HW03 probe</b>'); {const n=await page.locator('main b[data-hw03-probe]').count();check(n===0,`Rendered HTML elements=${n}; benign markup only, no script executed`);} break;
        case 'G25': await home();await page.getByRole('link',{name:'Xem chi tiết',exact:true}).first().click();await page.waitForURL('**/product/1');await page.locator('main input[type=number]').waitFor();check(page.url().endsWith('/product/1')&&await page.locator('main h1').innerText()===products[0].name,page.url());break;
        case 'G26': await detail();await page.getByRole('link',{name:'EShop',exact:true}).click();await page.locator('main h2').first().waitFor();check(page.url()===base+'/',page.url());break;
        case 'G27': await home();await cart();check(page.url().endsWith('/cart'),await text());break;
        case 'G28': await page.goto(base+'/cart');await page.getByRole('link',{name:'Tiếp tục mua sắm',exact:true}).click();await page.locator('main h2').first().waitFor();check(page.url()===base+'/',page.url());break;
        case 'G29': await home();await search('iPhone');await page.getByRole('link',{name:'Xem chi tiết',exact:true}).click();await page.locator('main input[type=number]').waitFor();await page.goBack();await page.locator('main h2').first().waitFor();{const q=await page.getByPlaceholder('Tìm kiếm...').inputValue();const n=await page.locator('main h2').count();check(q==='iPhone'&&n===1,`query=${JSON.stringify(q)}; products=${n}`);}break;
        case 'G30': case 'G31': if(id==='G30')await detail();else{await addHome();await cart();}{const n=await page.locator('main nav,main [aria-label*=breadcrumb i],main [aria-label*="đường dẫn" i]').count();check(n>0,`breadcrumb regions=${n}`);}break;
        case 'G32': await page.goto(base+'/cart'); {const l=page.getByRole('link',{name:'Giỏ hàng',exact:true});const a=await l.getAttribute('aria-current');const cls=await l.getAttribute('class');check(a==='page'||(cls||'').split(/\s/).some(c=>['active','font-bold','underline'].includes(c)),`aria-current=${a}; class=${cls}`);}break;
        case 'G33': await home();{const trace=[];for(let n=0;n<5;n++){await page.keyboard.press('Tab');trace.push(await page.evaluate(()=>document.activeElement.placeholder||document.activeElement.textContent));}check(trace[4]==='Tìm kiếm...',JSON.stringify(trace));}break;
        case 'G34': await home();await page.getByPlaceholder('Tìm kiếm...').focus();await page.keyboard.type('iPhone');await page.keyboard.press('Enter');await page.waitForTimeout(500);await page.keyboard.press('Tab');await page.keyboard.press('Tab');await page.keyboard.press('Enter');await page.waitForTimeout(500);check(page.url().endsWith('/product/1'),page.url());break;
        case 'G35': await addHome();await cart();await page.getByRole('link',{name:/Mua tiếp/}).click();await page.locator('main h2').first().waitFor();check(page.url()===base+'/',page.url());break;
        case 'G36': await addHome();await page.getByRole('button',{name:'Thêm vào giỏ',exact:true}).first().click();await cart();{const n=await page.locator('tbody tr').count();const q=await page.locator('tbody tr').first().locator('td').nth(2).innerText();check(n===1&&q==='2',`rows=${n}; first quantity=${q}`);}break;
        case 'G37': await page.route('**/api/products?*',async route=>{await new Promise(r=>setTimeout(r,1600));await route.continue();});await page.goto(base);{const t=await text();check(/đang tải|loading/i.test(t),`Artificial API delay 1600ms; observed: ${t}`);}break;
        case 'G38': await home();await search('HW03-no-such-product-731');{const t=await text();check(/không (có|tìm thấy)|chưa có|no results/i.test(t),t);}break;
        case 'G39': await addHome();{const t=await page.locator('body').innerText();const live=await page.locator('[role=status],[role=alert],[aria-live]').count();const nav=await page.locator('header nav').innerText();check(live>0||/đã thêm/i.test(t)||/\d/.test(nav),`live regions=${live}; nav=${nav}`);}break;
        case 'G40': await detail();await page.getByRole('button',{name:'Thêm vào giỏ hàng',exact:true}).click();await cart();{const n=await page.locator('tbody tr').count();check(n===1,`After one click: cart rows=${n}; ${await text()}`);}break;
        case 'G41': await detail();await page.getByRole('button',{name:'Thêm vào giỏ hàng',exact:true}).click();await page.getByRole('button',{name:'Thêm vào giỏ hàng',exact:true}).click();check(await page.getByRole('button',{name:'Đã thêm',exact:true}).isVisible(),'After second click: Đã thêm');break;
        case 'G42': await addHome();{const t=await page.getByRole('link',{name:'Giỏ hàng',exact:true}).innerText();const n=await page.getByRole('link',{name:'Giỏ hàng',exact:true}).locator('span').count();check(n>0||/\d/.test(t),`link=${t}; badge elements=${n}`);}break;
        case 'G43': await addHome();await cart();{let dialog=false;page.once('dialog',async d=>{dialog=true;await d.dismiss();});await page.getByRole('button',{name:'Xóa',exact:true}).click();const n=await page.locator('[role=dialog]').count();const rows=await page.locator('tbody tr').count();check(dialog||n>0,`confirmation=${dialog}; dialog elements=${n}; remaining cart rows=${rows}`);}break;
        case 'G44': await page.goto(base+'/cart');{const n=await hasEmptyIllustration();const t=await text();check(n>0&&/trống/.test(t),`illustrations=${n}; ${t}`);}break;
        case 'G45': await addHome();await cart();{const t=await text();check(t.includes('Tổng cộng'),t);}break;
        case 'G46': await page.goto(base+'/product/999999');await page.waitForTimeout(1200);{const t=await text();check(/không tồn tại|không tìm thấy|not found/i.test(t)&&!/Đang tải/.test(t),t);}break;
        case 'G47': await page.route('**/api/products?*',r=>r.fulfill({status:503,contentType:'application/json',body:JSON.stringify({error:'HW03 controlled network failure'})}));await page.goto(base);await page.waitForTimeout(500);{const t=await text();check(/lỗi|thử lại|không thể|error/i.test(t),`Controlled HTTP 503; ${t}`);}break;
        case 'G48': await page.route('**/api/products/1',r=>r.fulfill({status:503,contentType:'application/json',body:JSON.stringify({error:'HW03 controlled network failure'})}));await page.goto(base+'/product/1');await page.waitForTimeout(700);{const t=await text();check(/lỗi|thử lại|không thể|error/i.test(t)&&!/Đang tải/.test(t),`Controlled HTTP 503; ${t}`);}break;
      }
    } catch(e) {state='Blocked';actual=`Harness error (not a product failure): ${e.message}`;}
    // Annotation is added AFTER measurement and outside the application main region.
    if (!passed || id==='G02') {
      await page.evaluate(({id,env,criterion,actual})=>{
        const panel=document.createElement('form');panel.id='hw03-evidence-annotation';panel.setAttribute('aria-label','Test evidence annotation, not SUT');
        panel.style.cssText='position:fixed;bottom:0;left:0;right:0;z-index:2147483647;background:#111827;color:white;padding:10px 14px;font:12px/1.4 Arial;pointer-events:none;border-top:3px solid #f59e0b';
        for(const value of ['TEST EVIDENCE ANNOTATION | '+id+' | '+env,'Email: 23120207@student.hcmus.edu.vn | MSSV: 23120207 | Họ tên: Nguyễn Bảo An',location.href+' | '+new Date().toISOString(),criterion,actual.slice(0,450)]){const line=document.createElement('div');line.textContent=value;panel.append(line);}
        document.body.append(panel);
      },{id,env,criterion,actual});
      evidence=`${dir}/${id}.png`;await page.screenshot({path:evidence,fullPage:true});
    }
    results.push({id,aspect,screen,criterion,reference,status:state==='Blocked'?'Blocked':passed?'Passed':'Failed',notes:actual,evidence,environment:env,timestamp:new Date().toISOString(),consoleErrors:observations});
    console.log(`${engine} ${id} ${results.at(-1).status}: ${actual.slice(0,140)}`);
    await context.close();
  }
  await browser.close();
  const commit=execFileSync('git',['-C','.work/sut','rev-parse','HEAD'],{encoding:'utf8'}).trim();
  await fs.writeFile(`evidence/runs/${engine}.json`,JSON.stringify({environment:env,engine,sutCommit:commit,startedAt:results[0].timestamp,results},null,2)+'\n');
  const counts=Object.fromEntries(['Passed','Failed','Blocked'].map(s=>[s,results.filter(r=>r.status===s).length]));
  console.log(JSON.stringify(counts));
  if(counts.Blocked)process.exitCode=2;
}
main().catch(e=>{console.error(e);process.exitCode=1;});
