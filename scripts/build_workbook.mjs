import fs from 'node:fs/promises';
import assert from 'node:assert/strict';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const chrome=JSON.parse(await fs.readFile('evidence/runs/chrome.json','utf8'));
const firefox=JSON.parse(await fs.readFile('evidence/runs/firefox.json','utf8'));
const wb=Workbook.create();
const summary=wb.worksheets.add('Summary');
const checks=wb.worksheets.add('Checklist');
const sus=wb.worksheets.add('SUS');
for(const s of [summary,checks,sus]){
  s.showGridLines=false;
  s.getRange('A1:L65').format.font={name:'Arial',size:11,color:'#172033'};
  s.getRange('A1:L65').format.verticalAlignment='center';
}
function header(s,range){s.getRange(range).format={fill:'#24354B',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:30,wrapText:true};}
summary.getRange('A2').values=[['HW03 G2 - Kết quả kiểm thử']];
summary.getRange('A2').format.font={size:16,bold:true};
summary.getRange('A4:D4').values=[['Môi trường','Passed','Failed','Chưa thực thi']];header(summary,'A4:D4');
summary.getRange('A5:A7').values=[['Chrome'],['Firefox'],['Safari - chưa chạy trọn bộ']];
for(const [row,col]of [[5,'F'],[6,'G']]){
  summary.getRange(`B${row}:D${row}`).formulas=[[`=COUNTIFS(Checklist!${col}8:${col}55,"Passed")`,`=COUNTIFS(Checklist!${col}8:${col}55,"Failed")`,`=48-B${row}-C${row}`]];
}
summary.getRange('B7:D7').values=[['Chưa có','Chưa có','Xem ghi chú']];
summary.getRange('A10:B15').values=[['Phạm vi','Home/Search, Detail, Cart'],['Checklist thiết kế',48],['Số IA',4],['Nhóm bug',23],['Người tham gia thật',0],['SUS trung bình','Chưa có dữ liệu thật']];
summary.getRange('A18').values=[['CHƯA ĐỦ ĐIỀU KIỆN NỘP: thiếu pilot/7 phiên thật, human review, nền tảng thứ ba chạy trọn bộ và demo.']];
summary.getRange('A18').format.font={color:'#9A3412',size:11};
summary.getRange('A20').values=[['Nguồn: đề HW03 §6, §14; kết quả gốc evidence/runs/chrome.json và firefox.json.']];
summary.getRange('A:A').format.columnWidth=43;
summary.getRange('B:B').format.columnWidth=48;
summary.getRange('C:D').format.columnWidth=19;
summary.getRange('A4:D15').format.rowHeight=29;
const matrix=chrome.results.map((a,i)=>{const b=firefox.results[i];assert(a.id===b.id);return[a.id,a.aspect,a.screen,a.criterion,a.reference,a.status,b.status,a.notes.slice(0,220),b.notes.slice(0,220),a.evidence,b.evidence];});
checks.getRange('A2').values=[['Checklist GUI G2 - 48 mục']];checks.getRange('A2').format.font={size:16,bold:true};
checks.getRange('A4').values=[['Nguồn: EShop README FR-05/06/07 và GUI §8; heuristic được đánh dấu trong cột Reference.']];
checks.getRange('A5').values=[['Notes rút gọn; xem JSON gốc để đọc đầy đủ. Sinh viên chưa human review/tự bổ sung.']];
checks.getRange('A7:K7').values=[['ID','IA','Screen','Expected','Reference','Chrome','Firefox','Chrome Notes','Firefox Notes','Chrome screenshot','Firefox screenshot']];header(checks,'A7:K7');
checks.getRange('A8:K55').values=matrix;
checks.getRange('A8:K55').format.wrapText=true;
checks.getRange('A8:K55').format.rowHeight=110;
for(const [col,width]of [['A',9],['B',10],['C',12],['D',58],['E',28],['F',13],['G',13],['H',65],['I',65],['J',42],['K',42]])checks.getRange(`${col}:${col}`).format.columnWidth=width;
checks.freezePanes.freezeRows(7);checks.freezePanes.freezeColumns(1);
checks.tables.add('A7:K55',true,'GuiChecklist');
checks.getRange('F8:G55').conditionalFormats.add('containsText',{text:'Failed',format:{fill:'#FEE2E2',font:{color:'#991B1B'}}});
sus.getRange('A2').values=[['SUS - nhập dữ liệu thật sau mỗi phiên']];sus.getRange('A2').format.font={size:16,bold:true};
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
wb.recalculate();
for(const [sheetName,range,name]of [['Summary','A1:D20','summary'],['Checklist','A7:G13','checklist'],['SUS','A2:L14','sus']]){
  const blob=await wb.render({sheetName,range,scale:1.5,format:'png'});
  await fs.writeFile(`tmp/${name}-preview.png`,new Uint8Array(await blob.arrayBuffer()));
}
const inspected=await wb.inspect({kind:'table',range:'Summary!A4:D7',include:'values,formulas',tableMaxRows:5,tableMaxCols:4});
console.log(inspected.ndjson);
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:20}});console.log(errors.ndjson);
const output=await SpreadsheetFile.exportXlsx(wb);await output.save('checklists/gui_checklist_g2.xlsx');
