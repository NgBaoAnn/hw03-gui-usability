"""Recover only this project's homework-planning transcript from OpenCode, read-only."""
import hashlib
import json
import sqlite3
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT=Path(__file__).resolve().parents[1]


def main():
    db=Path.home()/'.local/share/opencode/opencode.db'
    with sqlite3.connect(db.as_uri()+'?mode=ro',uri=True) as con:
        sessions=list(con.execute('SELECT id,title,model FROM session_v2 WHERE directory=? AND title=?',(str(ROOT),'Homework requirements overview')))
        if len(sessions)!=1:raise ValueError('Expected one unambiguous homework planning session')
        sid,title,model=sessions[0]
        out=['# AI Audit khôi phục - phiên lập kế hoạch 03/11/2026','',f'Công cụ: OpenCode. Session: `{sid}`. Tiêu đề: {title}. Cấu hình model ghi trong log: `{model}`. Nguồn đọc chỉ giới hạn session gắn đúng thư mục HW03. Không xuất phiên OAuth, tài khoản, thông tin xác thực hay suy luận nội bộ.','']
        count=0
        for role,raw in con.execute('SELECT type,data FROM session_message WHERE session_id=? ORDER BY seq',(sid,)):
            data=json.loads(raw)
            if role=='user':text=data.get('text','')
            elif role=='assistant':text='\n\n'.join(p.get('text','') for p in data.get('content',[]) if p.get('type')=='text')
            else:continue
            if not text.strip():continue
            when=datetime.fromtimestamp(data['time']['created']/1000,ZoneInfo('Asia/Ho_Chi_Minh')).isoformat(timespec='seconds')
            count+=1;out.extend([f'## {count}. {role} - {when}','',text,''])
    assert count>=14,'Incomplete planning transcript'
    out+=['## Đầu ra nguyên gốc của các lần lập kế hoạch','', 'Các bản kế hoạch dưới đây được giữ như đầu ra AI ban đầu để kiểm toán, kể cả những giả định đã được sửa trong báo cáo hiện tại. Không dùng chúng thay cho kết quả chạy thật.','']
    folder=ROOT/'reports/legacy';folder.mkdir(exist_ok=True)
    for source in ['PLAN_G2.md','KE_HOACH_CHI_TIET.md','docs/superpowers/plans/2026-11-03-gui-usability-g2.md']:
        data=(ROOT/source).read_bytes();dest=folder/Path(source).name;dest.write_bytes(data)
        out.append(f'- [{dest.name}](legacy/{dest.name}); SHA-256 `{hashlib.sha256(data).hexdigest()}`.')
    (ROOT/'reports/AI_AUDIT_RECOVERED.md').write_text('\n'.join(out),encoding='utf-8')
    print(f'Recovered {count} visible planning messages and three original planning artifacts')


if __name__=='__main__':main()
