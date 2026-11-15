"""Collect new browser-side read-only accessibility checks; never invent a result."""
import json
import shutil
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


class Collector(BaseHTTPRequestHandler):
    def respond(self,status):
        self.send_response(status)
        self.send_header('Access-Control-Allow-Origin','http://localhost:5173')
        self.send_header('Access-Control-Allow-Headers','Content-Type')
        self.send_header('Access-Control-Allow-Methods','POST, OPTIONS')
        self.end_headers()

    def do_OPTIONS(self):self.respond(204)

    def do_POST(self):
        try:
            assert self.path=='/results' and self.headers.get('Origin')=='http://localhost:5173'
            size=int(self.headers['Content-Length']);assert 0<size<16000
            row=json.loads(self.rfile.read(size));engine=row['engine'];ua=row['userAgent']
            assert engine in ['chrome','firefox','safari']
            assert ('Firefox/' in ua) if engine=='firefox' else ('Chrome/' in ua) if engine=='chrome' else ('Safari/' in ua and 'Chrome/' not in ua)
            assert row['id'] in ['G49','G50','G51'] and row['status'] in ['Passed','Failed']
            assert row['observation']['url'].startswith('http://localhost:5173/')
            folder=ROOT/'evidence/accessibility'/engine;folder.mkdir(parents=True,exist_ok=True)
            row['os']='macOS '+subprocess.check_output(['sw_vers','-productVersion'],text=True).strip()
            row['sutCommit']=subprocess.check_output(['git','-C',str(ROOT/'.work/sut'),'rev-parse','HEAD'],text=True).strip()
            (folder/f"{row['id']}.json").write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
            print(engine,row['id'],row['status'],flush=True);self.respond(200)
        except (AssertionError,KeyError,ValueError,TypeError):self.respond(400)

    def log_message(self,*args):pass


if __name__=='__main__':
    shutil.copyfile(ROOT/'scripts/accessibility-frame.html',ROOT/'.work/sut/frontend-web/public/hw03-accessibility.html')
    print('Local collector ready on localhost:8767; no Safari automation permission needed.',flush=True)
    HTTPServer(('127.0.0.1',8767),Collector).serve_forever()
