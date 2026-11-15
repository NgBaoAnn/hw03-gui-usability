import fs from 'node:fs/promises';
import assert from 'node:assert/strict';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const chrome=JSON.parse(await fs.readFile('evidence/runs/chrome.json','utf8'));
const firefox=JSON.parse(await fs.readFile('evidence/runs/firefox.json','utf8'));
const safari=JSON.parse(await fs.readFile('evidence/runs/safari.json','utf8'));
const additions=JSON.parse(await fs.readFile('checklists/additions.json','utf8'));
const extra=JSON.parse(await fs.readFile('evidence/accessibility/results.json','utf8'));
const total=chrome.results.length+additions.length,lastRow=7+total;
const study=JSON.parse(await fs.readFile('usability/summary.json','utf8'));
const responses=(await fs.readFile('usability/sus_responses.csv','utf8')).trim().split(/\r?\n/).slice(1).map(line=>line.split(',').slice(1).map(Number));
assert(responses.length===7 && responses.every(r=>r.length===10 && r.every(v=>Number.isInteger(v)&&v>=1&&v<=5)));
assert(safari.fullChecklist,'Safari run must be complete');
const wb=Workbook.create();
const summary=wb.worksheets.add('Summary');
const checks=wb.worksheets.add('Checklist');
const sus=wb.worksheets.add('SUS');
for(const s of [summary,checks,sus]){
  s.showGridLines=false;
  s.getRange('A1:N65').format.font={name:'Arial',size:11,color:'#172033'};
  s.getRange('A1:N65').format.verticalAlignment='center';
}
function header(s,range){s.getRange(range).format={fill:'#24354B',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:30,wrapText:true,horizontalAlignment:'center'};}
summary.getRange('A2').values=[['HW03 G2 - Kết quả kiểm thử']];
summary.getRange('A2').format.font={size:16,bold:true};
summary.getRange('A4:D4').values=[['Môi trường','Passed','Failed','Chưa thực thi']];header(summary,'A4:D4');
summary.getRange('A5:A7').values=[['Chrome'],['Firefox'],['Safari (WebDriver + native)']];
for(const [row,col]of [[5,'F'],[6,'G'],[7,'H']]){
  summary.getRange(`B${row}:D${row}`).formulas=[[`=COUNTIFS(Checklist!${col}8:${col}${lastRow},"Passed")`,`=COUNTIFS(Checklist!${col}8:${col}${lastRow},"Failed")`,`=${total}-B${row}-C${row}`]];
}
summary.getRange('A10:B15').values=[['Phạm vi GUI','Home/Search, Detail, Cart'],['Checklist thiết kế',total],['Số IA',4],['Nhóm bug GUI',25],['Phiên usability chính thức',7],['SUS trung bình',null]];
summary.getRange('B15').formulas=[['=SUS!L14']];summary.getRange('B15').setNumberFormat('0.00');
summary.getRange('A17:D18').merge();
const state=JSON.parse(await fs.readFile('submission_state.json','utf8'));
const selfScore=state.self_assessment?Object.values(state.self_assessment).reduce((a,b)=>a+b,0):'chưa chấm';
summary.getRange('A17').values=[[`Sinh viên tự chấm ${selfScore}/100. Video: https://youtu.be/VGVm_V7L_ks . Còn human review/tự bổ sung. AI đã rà soát bổ sung; xem AI_REVIEW.md. Task 2 không có video phiên.`]];
summary.getRange('A17:D18').format.wrapText=true;
summary.getRange('A18').format.font={color:'#9A3412',size:11};
summary.getRange('A20').values=[['Nguồn: đề HW03 §6, §14; evidence/runs/ (48 mục) và evidence/accessibility/results.json (3 mục bổ sung).']];
summary.getRange('A:A').format.columnWidth=43;
summary.getRange('B:B').format.columnWidth=48;
summary.getRange('C:D').format.columnWidth=19;
summary.getRange('A4:D15').format.rowHeight=29;
const matrix=chrome.results.map((a,i)=>{const b=firefox.results[i],c=safari.results[i];assert(a.id===b.id&&a.id===c.id);return[a.id,a.aspect,a.screen,a.criterion,a.reference,a.status,b.status,c.status,a.notes.slice(0,220),b.notes.slice(0,220),c.notes.slice(0,220),a.evidence,b.evidence,c.evidence];});
for(const [id,ia,screen,criterion,reference] of additions){const rows=['chrome','firefox','safari'].map(e=>extra[e].find(r=>r.id===id));matrix.push([id,ia,screen,criterion,reference,...rows.map(r=>r.status),...rows.map(r=>JSON.stringify(r.observation)),...rows.map(r=>r.evidence)]);}
assert(matrix.length===total);
checks.getRange('A2').values=[[`Checklist GUI G2 - ${total} mục (48 gốc + 3 bổ sung)`]];checks.getRange('A2').format.font={size:16,bold:true};
checks.getRange('A4').values=[['Nguồn: EShop README FR-05/06/07 và GUI §8; heuristic được đánh dấu trong cột Reference.']];
checks.getRange('A5').values=[['Notes rút gọn; xem JSON gốc để đọc đầy đủ. Sinh viên chưa human review/tự bổ sung.']];
checks.getRange('A7:N7').values=[['ID','IA','Screen','Expected','Reference','Chrome','Firefox','Safari','Chrome Notes','Firefox Notes','Safari Notes','Chrome screenshot','Firefox screenshot','Safari screenshot']];header(checks,'A7:N7');
checks.getRange(`A8:N${lastRow}`).values=matrix;
checks.getRange(`A8:N${lastRow}`).format.wrapText=true;
checks.getRange(`A8:N${lastRow}`).format.rowHeight=70;
for(const [col,width]of [['A',9],['B',10],['C',12],['D',58],['E',28],['F',13],['G',13],['H',13],['I',65],['J',65],['K',65],['L',42],['M',42],['N',42]])checks.getRange(`${col}:${col}`).format.columnWidth=width;
checks.freezePanes.freezeRows(7);checks.freezePanes.freezeColumns(1);
checks.tables.add(`A7:N${lastRow}`,true,'GuiChecklist').style='TableStyleLight9';
checks.getRange(`F8:H${lastRow}`).conditionalFormats.add('containsText',{text:'Failed',format:{fill:'#FEE2E2',font:{color:'#991B1B'}}});
sus.getRange('A2').values=[['SUS - 7 phiên sinh viên cung cấp']];sus.getRange('A2').format.font={size:16,bold:true};
sus.getRange('A3').values=[['Điểm 1–5, câu lẻ thuận/câu chẵn nghịch; nguồn Brooke: https://hell.meiert.org/core/pdf/sus.pdf']];
sus.getRange('A4:L4').values=[['ID',...Array.from({length:10},(_,i)=>'Q'+(i+1)),'SUS 0–100']];header(sus,'A4:L4');
sus.getRange('A5:A11').values=Array.from({length:7},(_,i)=>['P'+(i+1)]);
sus.getRange('B5:K11').format.fill='#FFFBEB';
sus.dataValidations.add({range:'B5:K11',rule:{type:'whole',operator:'between',formula1:1,formula2:5}});
for(let r=5;r<=11;r++){
  const terms=Array.from({length:10},(_,i)=>i%2===0?`(${String.fromCharCode(66+i)}${r}-1)`:`(5-${String.fromCharCode(66+i)}${r})`);
  sus.getRange(`L${r}`).formulas=[[`=IF(COUNT(B${r}:K${r})<>10,"Chưa đủ dữ liệu",(${terms.join('+')})*2.5)`]];
}
sus.getRange('A14').values=[['SUS trung bình 7 người']];
sus.getRange('L14').formulas=[['=IF(COUNT(L5:L11)=7,AVERAGE(L5:L11),"Chưa đủ 7 người")']];
sus.getRange('A:A').format.columnWidth=29;sus.getRange('B:K').format.columnWidth=8;sus.getRange('L:L').format.columnWidth=23;
sus.getRange('A4:L14').format.rowHeight=28;sus.getRange('L5:L14').setNumberFormat('0.0');
// Recalculation probes are temporary and never exported as participant data.
sus.getRange('B5:K5').values=[Array(10).fill(3)];assert(sus.getRange('L5').values[0][0]===50);
assert(sus.getRange('L14').values[0][0]==='Chưa đủ 7 người');
sus.getRange('B5:K11').values=Array(7).fill(null).map(()=>[5,1,5,1,5,1,5,1,5,1]);assert(sus.getRange('L14').values[0][0]===100);
sus.getRange('B5:K11').clear({applyTo:'contents'});
assert(sus.getRange('L5').values[0][0]==='Chưa đủ dữ liệu');
sus.getRange('B5:K11').values=responses;
wb.recalculate();
assert(Math.abs(sus.getRange('L14').values[0][0]-study.mean_sus)<1e-9);
assert(Math.abs(summary.getRange('B15').values[0][0]-study.mean_sus)<1e-9);
for(const [sheetName,range,name]of [['Summary','A1:D20','summary'],['Checklist','A7:H13','checklist'],['Checklist','A54:H58','additions'],['SUS','A2:L14','sus']]){
  const blob=await wb.render({sheetName,range,scale:1.5,format:'png'});
  await fs.writeFile(`tmp/${name}-preview.png`,new Uint8Array(await blob.arrayBuffer()));
}
const inspected=await wb.inspect({kind:'table',range:'Summary!A4:D7',include:'values,formulas',tableMaxRows:5,tableMaxCols:4});
console.log(inspected.ndjson);
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:20}});console.log(errors.ndjson);
const output=await SpreadsheetFile.exportXlsx(wb);await output.save('checklists/gui_checklist_g2.xlsx');
