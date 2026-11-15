import fs from 'node:fs/promises';
import assert from 'node:assert/strict';
import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';

const path='task2_usability/Task2_Usability_Data.xlsx';
const original='usability/private/task2_original/Task2_Usability_Data.xlsx';
const input=await fs.access(original).then(()=>original,()=>path);
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(input));
const readme=wb.worksheets.getItem('Readme');
const before=await wb.render({sheetName:'Readme',range:'A1:B10',scale:1,format:'png'});
await fs.writeFile('tmp/task2-readme-before.png',new Uint8Array(await before.arrayBuffer()));
const names=['Readme','Profiles','SUS','TaskResults','Timeline','Probes','Findings','Summary'];
for(const name of names) {
 const sheet=wb.worksheets.getItem(name), used=sheet.getUsedRange(), values=used.values;
 const last=String.fromCharCode(64+values[0].length);
 sheet.getRange(`A1:${last}1`).merge();sheet.getRange(`A1:${last}1`).format.rowHeight=44;
 sheet.getRange(`A1:${last}1`).format.wrapText=true;
 for(let r=0;r<values.length;r++) for(let c=0;c<values[r].length;c++) {
  const value=values[r][c];if(typeof value!=='string')continue;
  const updated=value.replaceAll('Phạm Quang Vinh','Nguyễn Bảo An').replaceAll('23120202','23120207').replace('https://github.com/vinh-code/HW03-Software-Testing/issues/10','../bug-reports/usability/U03.md').replace('https://github.com/vinh-code/HW03-Software-Testing/issues/1','../bug-reports/usability/U02.md').replace('../bugs/screenshots/GUI-001.png','../evidence/usability/U02.png').replace('../bugs/screenshots/GUI-030.png','../evidence/usability/U03.png');
  if(updated!==value) used.getCell(r,c).values=[[updated]];
 }
}
readme.getRange('B4').values=[['Nguyễn Bảo An — MSSV: 23120207 — 23120207@student.hcmus.edu.vn']];
readme.getRange('B7').values=[['Người tham gia từ chối ghi hình; chỉ có ghi chú. §14: nộp bản quay khi có.']];
const study=JSON.parse(await fs.readFile('usability/summary.json','utf8'));
const sus=wb.worksheets.getItem('SUS');
for(let i=0;i<7;i++) assert(Math.abs(sus.getRange(`N${i+3}`).values[0][0]-study.participants[i].sus)<1e-9);
const summary=wb.worksheets.getItem('Summary');
summary.getRange('B8:B9').setNumberFormat('0.0%');summary.getRange('B10:B14').setNumberFormat('0.00');
for(const [row,formula] of [[10,'=AVERAGE(SUS!N3:N9)'],[11,'=MEDIAN(SUS!N3:N9)'],[12,'=STDEV(SUS!N3:N9)'],[13,'=MIN(SUS!N3:N9)'],[14,'=MAX(SUS!N3:N9)']]) summary.getRange(`B${row}`).formulas=[[formula]];
const original=sus.getRange('C3:L3').values;
sus.getRange('C3:L3').values=[Array(10).fill(3)];
assert.equal(sus.getRange('N3').values[0][0],50);
sus.getRange('C3:L3').values=original;
wb.recalculate();
assert(Math.abs(summary.getRange('B10').values[0][0]-study.mean_sus)<1e-9);
for(const [sheetName,range,name] of [['Readme','A1:B10','readme'],['SUS','A1:N9','sus'],['Summary','A1:B23','summary'],...names.filter(n=>!['Readme','SUS','Summary'].includes(n)).map(n=>[n,`A1:${String.fromCharCode(64+wb.worksheets.getItem(n).getUsedRange().values[0].length)}3`,n.toLowerCase()])]) {
 const blob=await wb.render({sheetName,range,scale:1.2,format:'png'});
 await fs.writeFile(`tmp/task2-${name}-preview.png`,new Uint8Array(await blob.arrayBuffer()));
}
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:10}})).ndjson);
await (await SpreadsheetFile.exportXlsx(wb)).save(path);
console.log('Updated identity and recalculated SUS; original eight sheets preserved.');
