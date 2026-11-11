"""Render the three required report PDFs from their Markdown sources."""
import re
from html import escape
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

ROOT=Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(TTFont('ReportArial','/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('ReportArialBold','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
pdfmetrics.registerFontFamily('ReportArial',normal='ReportArial',bold='ReportArialBold',italic='ReportArial',boldItalic='ReportArialBold')
body=ParagraphStyle('Body',fontName='ReportArial',fontSize=10.2,leading=15,spaceAfter=8,textColor=colors.HexColor('#172033'),splitLongWords=True)
title=ParagraphStyle('Title',parent=body,fontName='ReportArialBold',fontSize=18,leading=24,spaceAfter=16)
heading=ParagraphStyle('Heading',parent=body,fontName='ReportArialBold',fontSize=13,leading=18,spaceBefore=12,spaceAfter=8,keepWithNext=True)
entry_heading=ParagraphStyle('EntryHeading',parent=body,fontName='ReportArialBold',fontSize=10.5,leading=15,spaceBefore=7,spaceAfter=4,keepWithNext=True)
cellstyle=ParagraphStyle('Cell',parent=body,fontSize=9.1,leading=13,spaceAfter=0,wordWrap='CJK')
headstyle=ParagraphStyle('HeadCell',parent=cellstyle,fontName='ReportArialBold',textColor=colors.white)


def inline(text):
    text=escape(text.replace('—','-').replace('–','-').replace('`',''))
    text=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
    text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1 (\2)',text)
    return text


def blocks(markdown):
    lines=markdown.splitlines();flow=[];i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line.startswith('|'):
            data=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                values=[s.strip() for s in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',v.replace(' ','')) for v in values):data.append(values)
                i+=1
            if not data:continue
            n=len(data[0]);data=[r+['']*(n-len(r)) for r in data]
            widths=[155,344] if n==2 else [105,175,219] if n==3 else [499/n]*n
            table=Table([[Paragraph(inline(v),headstyle if ri==0 else cellstyle) for v in row] for ri,row in enumerate(data)],colWidths=widths,repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#24354B')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,0),0.7,colors.HexColor('#94A3B8')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F3F6FA')])]))
            flow.extend([table,Spacer(1,10)]);continue
        if line.startswith('# '):flow.append(Paragraph(inline(line[2:]),title));i+=1;continue
        if line.startswith('## '):
            style=entry_heading if re.match(r'## \d+\. (user|assistant) - ',line) else heading
            flow.append(Paragraph(inline(line[3:]),style));i+=1;continue
        if line.startswith('- '):flow.append(Paragraph('• '+inline(line[2:]),body));i+=1;continue
        para=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].lstrip().startswith(('#','|','- ')):
            para.append(lines[i].strip());i+=1
        flow.append(Paragraph(inline(' '.join(para)),body))
    return flow


def page_footer(canvas,doc):
    canvas.saveState();canvas.setFont('ReportArial',8);canvas.setFillColor(colors.HexColor('#64748B'))
    canvas.drawString(48,28,'23120207 - HW03 G2 - Bản nháp, chưa đủ điều kiện nộp')
    canvas.drawRightString(A4[0]-48,28,f'{doc.page}');canvas.restoreState()


def main():
    for name in ['MAIN_REPORT','AI_AUDIT_REPORT','AI_CRITIQUE']:
        source=(ROOT/f'reports/{name}.md').read_text()
        if name=='AI_AUDIT_REPORT':source+='\n\n'+(ROOT/'reports/AI_TRANSCRIPT.md').read_text()
        output=ROOT/f'reports/{name}.pdf'
        doc=SimpleDocTemplate(str(output),pagesize=A4,leftMargin=48,rightMargin=48,topMargin=43,bottomMargin=48,title=f'HW03 G2 - {name}',author='Nguyễn Bảo An',allowSplitting=1)
        doc.build(blocks(source),onFirstPage=page_footer,onLaterPages=page_footer)
        print(output.name,output.stat().st_size)


if __name__=='__main__':main()
