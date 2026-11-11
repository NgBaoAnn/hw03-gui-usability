"""Package a clearly labelled review draft, including evidence and source requirements."""
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path
from validate_submission import check_files, missing_requirements

ROOT=Path(__file__).resolve().parents[1]


def main():
    subprocess.run(['git','log','--graph','--all','--stat'],cwd=ROOT,check=True,stdout=(ROOT/'git_commit_log.txt').open('w'))
    check_files();missing=missing_requirements()
    out=ROOT/'output';out.mkdir(exist_ok=True)
    zip_path=out/'23120207_HW03_AI_GUIUsability_DRAFT.zip'
    entries=[]
    for folder in ['reports','checklists','bug-reports','cross-platform','evidence','usability','skills','scripts']:
        for p in sorted((ROOT/folder).rglob('*')):
            rel=p.relative_to(ROOT)
            if p.is_file() and not any(x in ['private','__pycache__','node_modules'] for x in rel.parts) and not p.name.endswith('.inspect.ndjson'):
                entries.append((p,str(rel)))
    for name in ['README.md','git_commit_log.txt','submission_state.json']:
        entries.append((ROOT/name,name))
    for name in ['2026.HW03.GUI Usability_En.pdf','2026.HW03.GUI Usability_Vi.md','___2026.Homework.Policies.pdf']:
        entries.append((ROOT/name,'requirements/'+name))
    manifest={name:hashlib.sha256(p.read_bytes()).hexdigest() for p,name in entries}
    with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as archive:
        for p,name in entries:archive.write(p,name)
        archive.writestr('DRAFT_STATUS.json',json.dumps({'ready_for_final_submission':False,'missing':missing},ensure_ascii=False,indent=2))
        archive.writestr('SHA256SUMS.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    with zipfile.ZipFile(zip_path) as archive:
        assert archive.testzip() is None
        assert all(hashlib.sha256(archive.read(name)).hexdigest()==digest for name,digest in manifest.items())
        assert 'DRAFT_STATUS.json' in archive.namelist()
    assert zip_path.stat().st_size<=20*1024*1024,'Draft exceeds Moodle per-file limit; split explicitly'
    print(f'{zip_path}\n{len(entries)} files; {zip_path.stat().st_size:,} bytes; {len(missing)} outstanding prerequisites')


if __name__=='__main__':main()
