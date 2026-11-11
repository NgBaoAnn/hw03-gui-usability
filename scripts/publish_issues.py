"""Publish verified bugs to the dedicated homework repository, preserving per-issue results."""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = 'NgBaoAnn/hw03-gui-usability'


def main():
    path=ROOT/'bug-reports/issues.json'
    index=json.loads(path.read_text()) if path.exists() else {}
    for bug in json.loads((ROOT/'bug-reports/catalog.json').read_text()):
        if bug['id'] in index:
            continue
        body=(ROOT/bug['file']).read_text()
        body=re.sub(r'GitHub Issue: .*', 'GitHub Issue: current issue', body)
        for img in bug['screenshots']:
            body=body.replace('../'+img,f'https://github.com/{REPO}/blob/codex/hw03-deliverables/{img}?raw=true')
        # Every image stays available in the repository and in the submission archive.
        body+='\n\n### Original screenshot attachments\n\n'
        for img in bug['screenshots']:
            body+=f'![{bug["id"]} {Path(img).stem}](https://github.com/{REPO}/blob/codex/hw03-deliverables/{img}?raw=true)\n\n'
        tmp=ROOT/'tmp'/f'{bug["id"]}-issue.md';tmp.write_text(body)
        result=subprocess.run(['gh','issue','create','--repo',REPO,'--title',f'[{bug["id"]}] {bug["title"]}','--body-file',str(tmp)],text=True,capture_output=True)
        if result.returncode:
            raise RuntimeError(f'{bug["id"]}: {result.stderr}. Stop and inspect remote issues before retrying.')
        url=result.stdout.strip()
        if not re.fullmatch(r'https://github\.com/NgBaoAnn/hw03-gui-usability/issues/\d+',url):
            raise RuntimeError(f'Unexpected result for {bug["id"]}; inspect remote state before retrying')
        index[bug['id']]={'url':url,'number':int(url.rsplit('/',1)[1])}
        path.write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
        print(bug['id'],url,flush=True)


if __name__=='__main__':
    main()
