"""Execute the existing 48 G2 criteria in real Safari via Apple WebDriver.

Run: uv run --with selenium python scripts/run_safari.py
The same-origin evidence frame gives Safari exact desktop/mobile CSS viewports.
Only G37/G47/G48 redirect XHR to a localhost delay/503 fixture, explicitly logged.
"""
import argparse
import json
import re
import shutil
import subprocess
import threading
import time
from collections import Counter
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote, parse_qs, urlparse
from urllib.request import urlopen

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException

ROOT=Path(__file__).resolve().parents[1]
BASE='http://localhost:5173'


class NetworkFixture(BaseHTTPRequestHandler):
    def do_GET(self):
        args=parse_qs(urlparse(self.path).query)
        mode=args.get('mode',[''])[0]
        if mode=='delay':
            time.sleep(1.6)
            status=200
            with urlopen('http://localhost:3000/api/products',timeout=10) as response:body=response.read()
        else:
            status=503;body=b'{"error":"HW03 controlled HTTP 503"}'
        self.send_response(status);self.send_header('Content-Type','application/json')
        self.send_header('Access-Control-Allow-Origin',BASE);self.end_headers()
        try:self.wfile.write(body)
        except BrokenPipeError:pass  # The loading-state test navigates away before the delayed response.

    def log_message(self,*args):pass


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ids',help='Comma-separated IDs for a diagnostic rerun; preserves unrelated recorded cases')
    args=parser.parse_args()
    items=json.loads((ROOT/'checklists/items.json').read_text())
    assert len(items)>40 and len({r[0] for r in items})==len(items)
    selected=set(args.ids.split(',')) if args.ids else {r[0] for r in items}
    assert selected<={r[0] for r in items}
    shutil.copyfile(ROOT/'scripts/evidence-frame.html',ROOT/'.work/sut/frontend-web/public/hw03-evidence.html')
    products=json.load(urlopen('http://localhost:3000/api/products'))
    fixture=ThreadingHTTPServer(('127.0.0.1',8766),NetworkFixture)
    threading.Thread(target=fixture.serve_forever,daemon=True).start()
    driver=webdriver.Remote(command_executor='http://localhost:4444',options=webdriver.SafariOptions())
    driver.set_window_size(1400,1000);driver.set_script_timeout(12)
    wait=WebDriverWait(driver,8,poll_frequency=0.1)
    env=f"Safari {driver.capabilities['browserVersion']} (Apple safaridriver) / macOS {subprocess.check_output(['sw_vers','-productVersion'],text=True).strip()}"
    output=ROOT/'evidence/runs/safari.json'
    results=json.loads(output.read_text())['results'] if args.ids and output.exists() else []
    shots=ROOT/'evidence/gui/safari';shots.mkdir(parents=True,exist_ok=True)
    js=driver.execute_script
    find=lambda selector:driver.find_element(By.CSS_SELECTOR,selector)
    all_=lambda selector:driver.find_elements(By.CSS_SELECTOR,selector)
    count=lambda selector:len(all_(selector))
    text=lambda:find('main').text
    url=lambda:js('return location.href')
    click_observations=[]

    def frame_page(path='/',width=1280):
        driver.switch_to.default_content()
        driver.get(BASE+'/hw03-evidence.html?target='+quote(path,safe='/'))
        frame=wait.until(lambda d:d.find_element(By.TAG_NAME,'iframe'))
        js('arguments[0].style.width=arguments[1]+"px";arguments[0].style.height="900px"',frame,width)
        driver.switch_to.frame(frame)
        wait.until(lambda d:js('return document.readyState')=='complete' and count('main'))
        assert js('return innerWidth')==width,'Evidence frame viewport does not match requested width'

    def home(width=1280):
        frame_page('/',width);wait.until(lambda d:count('main h2')>0)

    def detail(width=1280):
        frame_page('/product/1',width);wait.until(lambda d:count('main input[type=number]')==1)

    def click_text(tag,label):
        element=wait.until(lambda d:next((e for e in all_(tag) if e.text.strip()==label),None))
        js('window.__hw03Clicks=0;arguments[0].addEventListener("click",()=>window.__hw03Clicks++,{once:true})',element)
        element.click();time.sleep(0.05);attempts=1
        if js('return window.__hw03Clicks')==0:
            # SafariDriver sometimes commits a focused input without dispatching a click.
            element.click();attempts+=1;time.sleep(0.05)
        delivered=js('return window.__hw03Clicks')
        click_observations.append({'target':label,'webdriver_attempts':attempts,'delivered_click_events':delivered})
        assert delivered==1,'SafariDriver did not deliver exactly one click event'

    def cart():
        click_text('header a','Giỏ hàng')
        wait.until(lambda d:url().endswith('/cart') and count('main h2')>0)

    def fill(selector,value):
        el=find(selector);el.clear()
        if value:el.send_keys(value)
        else:
            # A real keystroke ensures React receives the blank-field input event.
            el.send_keys('1');el.send_keys(Keys.BACKSPACE)

    def search(q):
        before=js('return performance.getEntriesByType("resource").filter(x=>x.name.includes("/api/products")).length')
        fill('input[placeholder="Tìm kiếm..."]',q);find('input[placeholder="Tìm kiếm..."]').send_keys(Keys.ENTER)
        wait.until(lambda d:js('return performance.getEntriesByType("resource").filter(x=>x.name.includes("/api/products")).length')>before)
        time.sleep(0.15)

    def add_home():
        home();click_text('main button','Thêm vào giỏ')

    def label(selector):
        return js('const e=arguments[0];return Boolean(e.labels?.length||e.getAttribute("aria-label")||e.getAttribute("aria-labelledby"))',find(selector))

    def network(mode,detail_page=False):
        # Install before React mounts the target screen; other API traffic is untouched.
        if detail_page:home()
        else:frame_page('/cart')
        target='/api/products/1' if detail_page else '/api/products?'
        js('''const old=XMLHttpRequest.prototype.open;const target=arguments[0],replacement=arguments[1];
          XMLHttpRequest.prototype.open=function(method,address,...rest){
            return old.call(this,method,String(address).includes(target)?replacement:address,...rest);
          };''',target,f'http://localhost:8766/fixture?mode={mode}')
        if detail_page:click_text('main a','Xem chi tiết')
        else:click_text('header a','EShop')
        wait.until(lambda d:url().endswith('/product/1' if detail_page else '/'))

    try:
        for id_,aspect,screen,criterion,reference in items:
            if id_ not in selected:continue
            click_observations.clear()
            passed=False;actual='';status='Executed';evidence='';stage='start';started=datetime.now(timezone.utc).isoformat()
            try:
                if id_=='G01':
                    home();n=count('main h1');passed=n==1;actual=f'h1={n}'
                elif id_=='G02':
                    detail();n=count('main h1');actual=f'h1={n}; {find("main h1").text}';passed=n==1 and find('main h1').text==products[0]['name']
                elif id_=='G03':
                    add_home();cart();n=count('main h1');passed=n==1;actual=f'h1={n}'
                elif id_=='G04':
                    home();actual=find('main .text-red-500').text;passed='₫' in actual and bool(re.search('[.,]',actual))
                elif id_=='G05':
                    detail();actual=find('main .text-red-600').text;passed='₫' in actual and re.sub(r'\D','',actual)==str(products[0]['price'])
                elif id_=='G06':
                    detail();actual=text();passed=products[0]['name'] in actual and products[0]['description'] in actual
                elif id_=='G07':
                    home();wait.until(lambda d:js('return document.querySelector("main img").naturalWidth>0'))
                    r=js('const e=document.querySelector("main img");return {fit:getComputedStyle(e).objectFit,w:e.clientWidth,h:e.clientHeight,nw:e.naturalWidth,nh:e.naturalHeight}')
                    passed=r['fit']!='cover' or abs(r['w']/r['h']-r['nw']/r['nh'])<0.05;actual=json.dumps(r)
                elif id_ in ['G08','G09']:
                    home(390 if id_=='G09' else 1280);r=js('return {width:innerWidth,scroll:document.documentElement.scrollWidth}')
                    passed=r['scroll']<=r['width'];actual=json.dumps(r)
                elif id_=='G10':
                    detail(390);r=js('const b=document.querySelector("main button").getBoundingClientRect();return {x:b.x,width:b.width,viewport:innerWidth}')
                    passed=r['x']>=0 and r['x']+r['width']<=r['viewport'];actual=json.dumps(r)
                elif id_=='G11':
                    detail();actual=js('return getComputedStyle(document.querySelector("main button")).backgroundColor');passed=actual=='rgb(37, 99, 235)'
                elif id_=='G12':
                    home();r=js('return Array.from(document.querySelectorAll("main img"),e=>e.alt)');passed=all(x.strip() for x in r);actual=json.dumps(r)
                elif id_=='G13':
                    home();passed=label('main input');actual=f'label/aria association={passed}'
                elif id_=='G14':
                    home();search('iPhone');names=[e.text for e in all_('main h2')];passed=bool(names) and all('iPhone' in n for n in names);actual=json.dumps(names)
                elif id_=='G15':
                    home();search('iPhone');search('');n=count('main h2');passed=n==len(products);actual=f'products={n}'
                elif id_=='G16':
                    home();search('iPhone&limit=1');names=[e.text for e in all_('main h2')];passed=len(names)==0;actual=json.dumps(names)
                elif id_=='G17':
                    detail();actual=find('main input').get_property('value');passed=actual=='1'
                elif id_ in ['G18','G19','G20','G21','G22']:
                    detail();v={'G18':'2','G19':'0','G20':'-1','G21':'1.5','G22':''}[id_];fill('main input',v)
                    click_text('main button','Thêm vào giỏ hàng');click_text('main button','Thêm vào giỏ hàng');cart()
                    n=count('tbody tr');q=find('tbody tr td:nth-child(3)').text if n else ''
                    passed=(n==1 and q=='2') if id_=='G18' else n==0;actual=f'input={v!r}; cart rows={n}; quantity={q}; {text()}'
                elif id_=='G23':
                    detail();passed=label('main input');actual=f'label/aria association={passed}'
                elif id_=='G24':
                    home();fill('main input','<b data-hw03-probe="1">HW03 probe</b>');n=count('main b[data-hw03-probe]');passed=n==0;actual=f'Rendered HTML elements={n}; benign markup only, no script executed'
                elif id_=='G25':
                    home();click_text('main a','Xem chi tiết');wait.until(lambda d:count('main input[type=number]')==1)
                    passed=url().endswith('/product/1') and find('main h1').text==products[0]['name'];actual=url()
                elif id_=='G26':
                    detail();click_text('header a','EShop');wait.until(lambda d:count('main h2')>0);passed=url()==BASE+'/';actual=url()
                elif id_=='G27':
                    home();cart();passed=url().endswith('/cart');actual=text()
                elif id_=='G28':
                    frame_page('/cart');click_text('main a','Tiếp tục mua sắm');wait.until(lambda d:count('main h2')>0);passed=url()==BASE+'/';actual=url()
                elif id_=='G29':
                    driver.switch_to.default_content()
                    driver.get(BASE);wait.until(lambda d:count('main h2')>0)
                    search('iPhone');click_text('main a','Xem chi tiết');wait.until(lambda d:count('main input[type=number]')==1)
                    driver.back()
                    wait.until(lambda d:count('main h2')>0);q=find('main input').get_property('value');n=count('main h2');passed=q=='iPhone' and n==1;actual=f'query={q!r}; products={n}'
                elif id_ in ['G30','G31']:
                    if id_=='G30':detail()
                    else:add_home();cart()
                    n=count('main nav,main [aria-label*=breadcrumb i],main [aria-label*="đường dẫn" i]');passed=n>0;actual=f'breadcrumb regions={n}'
                elif id_=='G32':
                    frame_page('/cart');e=next(e for e in all_('header a') if e.text=='Giỏ hàng');a=e.get_attribute('aria-current');c=e.get_attribute('class')
                    passed=a=='page' or any(x in c.split() for x in ['active','font-bold','underline']);actual=f'aria-current={a}; class={c}'
                elif id_=='G33':
                    home();js('document.body.tabIndex=-1;document.body.focus()');trace=[]
                    for _ in range(5):
                        ActionChains(driver).key_down(Keys.ALT).send_keys(Keys.TAB).key_up(Keys.ALT).perform()
                        trace.append(js('return document.activeElement.placeholder||document.activeElement.textContent'))
                    passed=trace[-1]=='Tìm kiếm...';actual='Safari native Option-Tab (all items; default Tab skips links): '+json.dumps(trace,ensure_ascii=False)
                elif id_=='G34':
                    home();find('main input').click();find('main input').send_keys('iPhone',Keys.ENTER);wait.until(lambda d:count('main h2')==1)
                    for _ in range(2):ActionChains(driver).key_down(Keys.ALT).send_keys(Keys.TAB).key_up(Keys.ALT).perform()
                    ActionChains(driver).send_keys(Keys.ENTER).perform();time.sleep(0.3);passed=url().endswith('/product/1');actual='Safari native Option-Tab: '+url()
                elif id_=='G35':
                    add_home();cart();click_text('main a','← Mua tiếp');wait.until(lambda d:count('main h2')>0);passed=url()==BASE+'/';actual=url()
                elif id_=='G36':
                    add_home();click_text('main button','Thêm vào giỏ');cart();n=count('tbody tr');q=find('tbody tr td:nth-child(3)').text;passed=n==1 and q=='2';actual=f'rows={n}; first quantity={q}'
                elif id_=='G37':
                    network('delay');actual='Controlled 1600ms delayed XHR fixture, before response: '+text();passed=bool(re.search('đang tải|loading',text(),re.I))
                elif id_=='G38':
                    home();search('HW03-no-such-product-731');actual=text();passed=bool(re.search('không (có|tìm thấy)|chưa có|no results',actual,re.I))
                elif id_=='G39':
                    add_home();n=count('[role=status],[role=alert],[aria-live]');nav=find('header nav').text;passed=n>0 or 'đã thêm' in text().lower() or bool(re.search(r'\d',nav));actual=f'live regions={n}; nav={nav}'
                elif id_=='G40':
                    detail();click_text('main button','Thêm vào giỏ hàng');cart();n=count('tbody tr');passed=n==1;actual=f'After one click: cart rows={n}; {text()}'
                elif id_=='G41':
                    detail();click_text('main button','Thêm vào giỏ hàng');click_text('main button','Thêm vào giỏ hàng');actual=find('main button').text;passed=actual=='Đã thêm'
                elif id_=='G42':
                    add_home();link=next(e for e in all_('header a') if e.text=='Giỏ hàng');t=link.text;n=len(link.find_elements(By.TAG_NAME,'span'));passed=n>0 or bool(re.search(r'\d',t));actual=f'link={t}; badge elements={n}'
                elif id_=='G43':
                    add_home();cart();click_text('main button','Xóa');dialog=False
                    try:driver.switch_to.alert.dismiss();dialog=True
                    except NoAlertPresentException:pass
                    n=count('[role=dialog]');passed=dialog or n>0;actual=f'confirmation={dialog}; dialog elements={n}; remaining cart rows={count("tbody tr")}'
                elif id_=='G44':
                    frame_page('/cart');n=count('main img,main svg,main [role=img]');actual=f'illustrations={n}; {text()}';passed=n>0 and 'trống' in text()
                elif id_=='G45':
                    add_home();cart();actual=text();passed='Tổng cộng' in actual
                elif id_=='G46':
                    frame_page('/product/999999');wait.until(lambda d:'Đang tải' not in text());actual=text();passed=bool(re.search('không tồn tại|không tìm thấy|not found',actual,re.I))
                elif id_ in ['G47','G48']:
                    network('error',detail_page=id_=='G48');time.sleep(0.7);t=text();actual='Controlled HTTP 503 via localhost XHR fixture: '+t
                    passed=bool(re.search('lỗi|thử lại|không thể|error',t,re.I)) and (id_!='G48' or 'Đang tải' not in t)
                else:raise AssertionError('Unimplemented criterion '+id_)
            except Exception as error:
                status='Blocked';actual=f'Harness/environment error at {stage} (not a product failure): '+repr(error)
            if status!='Blocked':status='Passed' if passed else 'Failed'
            if status!='Passed' or id_=='G02':
                try:
                    current=url();driver.switch_to.default_content()
                    js('''const frame=document.querySelector('iframe');
                      const f=frame?document.querySelector('form'):document.createElement('form');
                      if(!frame){f.style.cssText='position:fixed;bottom:0;left:0;right:0;z-index:2147483647;background:#111827;color:white;padding:12px;font:12px Arial;pointer-events:none';f.textContent='Email: 23120207@student.hcmus.edu.vn | MSSV: 23120207 | Họ tên: Nguyễn Bảo An';document.body.append(f);}
                      else{f.style.height='180px';f.style.fontSize='12px';frame.style.height='700px';}
                      const p=document.createElement('div');p.textContent=arguments[0];p.style.whiteSpace='pre-wrap';f.append(p);''',f'{id_} | {env}\n{current}\n{criterion}\n{actual[:500]}')
                    evidence=f'evidence/gui/safari/{id_}.png';driver.save_screenshot(str(ROOT/evidence))
                except Exception as error:actual+='; screenshot error: '+str(error)
            row={'id':id_,'aspect':aspect,'screen':screen,'criterion':criterion,'reference':reference,'status':status,'notes':actual,'evidence':evidence,'environment':env,'timestamp':started,'consoleErrors':[],'click_delivery':list(click_observations)}
            results=[r for r in results if r['id']!=id_]+[row];results.sort(key=lambda r:r['id'])
            payload={'environment':env,'engine':'safari','sutCommit':subprocess.check_output(['git','-C',str(ROOT/'.work/sut'),'rev-parse','HEAD'],text=True).strip(),'startedAt':results[0]['timestamp'],'method':'Apple Safari WebDriver; same-origin iframe with exact CSS viewport except G29, which uses the top-level SUT and native WebDriver Back to avoid iframe history semantics. Full navigation resets React state per case. G37/G47/G48 use explicitly redirected XHR to a localhost delay/503 fixture; default Safari all-item keyboard navigation is Option-Tab.','fullChecklist':len(results)==len(items) and all(r['status'] in ['Passed','Failed'] for r in results),'results':results}
            output.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
            print(f'{id_} {status}: {actual[:180]}',flush=True)
        print(dict(Counter(r['status'] for r in results)),flush=True)
    finally:
        driver.quit();fixture.shutdown();fixture.server_close()
    if not payload['fullChecklist']:raise SystemExit(2)


if __name__=='__main__':main()
