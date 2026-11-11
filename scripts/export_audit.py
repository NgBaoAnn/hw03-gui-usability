"""Export user-visible prompts/answers from this homework chat, excluding internal reasoning."""
import argparse
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('transcript',type=Path)
    args=parser.parse_args()
    out=['# Nhật ký hội thoại AI - HW03', '', 'Bản xuất lời nhắn người dùng và câu trả lời hiển thị của Codex. Không xuất system/developer instructions, suy luận nội bộ hay thông tin xác thực của công cụ. Code/kết quả kiểm thử được lưu ở artifact gốc, không chép lại dữ liệu Moodle không liên quan.', '']
    n=0
    for line in args.transcript.read_text().splitlines():
        row=json.loads(line);p=row.get('payload',{})
        if row.get('type')!='response_item' or p.get('type')!='message' or p.get('role') not in ['user','assistant']:
            continue
        if p.get('role')=='assistant' and p.get('channel') not in ['commentary','final',None]:
            continue
        text='\n'.join(part.get('text','') for part in p.get('content',[]) if part.get('type') in ['input_text','output_text','text'])
        if not text.strip() or text.lstrip().startswith(('<environment_context>','<external_codex_apps_open_page>','<external_codex_apps_selected_page_part_')):
            continue
        when=datetime.fromisoformat(row['timestamp'].replace('Z','+00:00')).astimezone(ZoneInfo('Asia/Ho_Chi_Minh')).isoformat(timespec='seconds')
        n+=1;out += [f'## {n}. {p["role"]} - {when}', '', text, '']
    Path('reports/AI_TRANSCRIPT.md').write_text('\n'.join(out),encoding='utf-8')
    print(f'Exported {n} visible messages')


if __name__=='__main__':
    main()
