with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

edl_screen = '''
  <div class="screen" id="screen-edl">
    <section class="section" data-bail="edl" data-index="0">
      <div class="info-banner" style="background:rgba(224,82,82,.08);border-color:#E05252"><svg viewBox="0 0 24 24" style="stroke:#E05252;fill:none;stroke-width:2;flex-shrink:0;width:16px;height:16px"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg><p>État des lieux contradictoire — art. 3-2 loi 89-462.</p></div>
      <div class="card">
        <div class="card-header"><div class="card-icon" style="background:#E05252"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg></div><div><div class="card-title">Type</div></div></div>
        <div class="chips" id="edl-type-chips"><div class="chip active" onclick="selectEDLType(this,\'entree\')">Entrée</div><div class="chip" onclick="selectEDLType(this,\'sortie\')">Sortie</div><div class="chip" onclick="selectEDLType(this,\'comparatif\')">Comparatif</div></div>
        <div class="field" style="margin-top:12px"><label>Date</label><input type="date" id="edl-date"></div>
        <div class="field"><label>Adresse</label><input type="text" placeholder="15 avenue Victor Hugo, 75016 Paris" id="edl-adresse"></div>
      </div>
      <div class="card">
        <div class="card-header"><div class="card-icon ic-dark"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div><div><div class="card-title">Bailleur</div></div></div>
        <div class="field-row"><div class="field"><label>Nom</label><input type="text" placeholder="Dupont" id="edl-bailleur-nom"></div><div class="field"><label>Prénom</label><input type="text" placeholder="Marie" id="edl-bailleur-prenom"></div></div>
        <div class="field"><label>Téléphone</label><input type="tel" placeholder="+33 6 00 00 00 00" id="edl-bailleur-tel"></div>
      </div>
      <div class="card">
        <div class="card-header"><div class="card-icon ic-blue"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div><div><div class="card-title">Locataire</div></div></div>
        <div class="field-row"><div class="field"><label>Nom</label><input type="text" placeholder="Martin" id="edl-locataire-nom"></div><div class="field"><label>Prénom</label><input type="text" placeholder="Lucas" id="edl-locataire-prenom"></div></div>
        <div class="field"><label>Téléphone</label><input type="tel" placeholder="+33 6 00 00 00 00" id="edl-locataire-tel"></div>
      </div>
      <div class="sec-divider"><span>Pièces d\'identité</span></div>
      <div class="card">
        <div class="card-header"><div class="card-icon" style="background:linear-gradient(135deg,#1B6CA8,#0D1B2A)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><circle cx="8" cy="11" r="2"/><path d="M14 9h4M14 13h3"/></svg></div><div><div class="card-title">Carte d\'identité</div><div class="card-sub">Photographiez les CNI</div></div></div>
        <div class="id-trigger-wrap">
          <div class="id-trigger" id="id-trig-edl-bailleur" onclick="openCamera(\'edl-bailleur\')"><div class="id-trigger-icon"><svg viewBox="0 0 24 24"><path d="M23 19a2 2 0 01-2 2H3a2 2 0 01-2-2V8a2 2 0 012-2h4l2-3h6l2 3h4a2 2 0 012 2z"/><circle cx="12" cy="13" r="4"/></svg></div><img class="id-trigger-img" id="id-thumb-edl-bailleur" alt=""><div class="id-badge">✓</div><div class="id-trigger-label">Bailleur</div></div>
          <div class="id-trigger" id="id-trig-edl-locataire" onclick="openCamera(\'edl-locataire\')"><div class="id-trigger-icon"><svg viewBox="0 0 24 24"><path d="M23 19a2 2 0 01-2 2H3a2 2 0 01-2-2V8a2 2 0 012-2h4l2-3h6l2 3h4a2 2 0 012 2z"/><circle cx="12" cy="13" r="4"/></svg></div><img class="id-trigger-img" id="id-thumb-edl-locataire" alt=""><div class="id-badge">✓</div><div class="id-trigger-label">Locataire</div></div>
        </div>
      </div>
    </section>
    <section class="section" data-bail="edl" data-index="1">
      <div class="card">
        <div class="card-header"><div class="card-icon ic-orange"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div><div><div class="card-title">Compteurs</div></div></div>
        <div class="field"><label>Électricité (kWh)</label><input type="number" placeholder="00000
python3 inject_edl2.py
cat > inject_edl3.py << 'PYEOF'
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

edl_js = """
BAIL_CONFIG['edl'] = {
  name: 'État des Lieux', color: '#E05252',
  steps: ['Parties & CNI', 'Compteurs & Clés', 'Pièces', 'Signatures & PDF']
};
const PIECES_DEFAULT = [
  {nom:'Entrée / Couloir',icone:'🚪'},{nom:'Salon / Séjour',icone:'🛋️'},
  {nom:'Cuisine',icone:'🍳'},{nom:'Chambre 1',icone:'🛏️'},
  {nom:'Salle de bain',icone:'🚿'},{nom:'WC',icone:'🚽'}
];
let edlPieces=[],edlType='entree',pieceCounter=0,currentPieceId=null;

function startEDL(){
  activeBail='edl'; current=0;
  edlPieces=PIECES_DEFAULT.map((p,i)=>({...p,id:i,etat:'Bon',obs:'',photos:[]}));
  pieceCounter=PIECES_DEFAULT.length;
  const cfg=BAIL_CONFIG['edl'];
  document.getElementById('nav-title').textContent=cfg.name;
  document.getElementById('btn-next').style.background='linear-gradient(135deg,'+cfg.color+',#0D1B2A 130%)';
  document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));
  document.getElementById('screen-edl').classList.add('active');
  document.getElementById('topnav').style.display='block';
  document.getElementById('progress-wrap').style.display='block';
  document.getElementById('bottomnav').style.display='flex';
  renderPieces(); showSection(); initAllSignatures(); setTodayDates();
}

function selectEDLType(el,type){
  edlType=type;
  document.querySelectorAll('#edl-type-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}

function renderPieces(){
  const container=document.getElementById('edl-pieces-list');
  if(!container) return;
  container.innerHTML=edlPieces.map(p=>`
    <div class="card" style="margin-bottom:10px">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px">
        <div style="display:flex;align-items:center;gap:8px">
          <span style="font-size:22px">${p.icone}</span>
          <div class="card-title" style="font-size:15px">${p.nom}</div>
        </div>
        <button onclick="removePiece(${p.id})" style="background:none;border:none;color:var(--muted);font-size:18px;cursor:pointer">✕</button>
      </div>
      <div class="field" style="margin-bottom:10px">
        <label>État général</label>
        <div class="chips">
          ${['Bon','Usage','Mauvais','À remplacer'].map(e=>
            `<div class="chip ${p.etat===e?'active':''}" onclick="setPieceEtat(${p.id},'${e}',this)">${e}</div>`
          ).join('')}
        </div>
      </div>
      <div class="field" style="margin-bottom:10px">
        <label>Observations</label>
        <textarea placeholder="Ex: traces sur les murs..." style="min-height:60px" onchange="setPieceObs(${p.id},this.value)">${p.obs}</textarea>
      </div>
      <div>
        <label style="display:block;font-size:11px;font-weight:600;color:var(--sky);letter-spacing:.5px;text-transform:uppercase;margin-bottom:8px">Photos (${p.photos.length})</label>
        <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center">
          ${p.photos.map((ph,pi)=>`
            <div style="position:relative">
              <img src="${ph}" style="width:70px;height:50px;border-radius:6px;object-fit:cover;border:1.5px solid var(--border)">
              <button onclick="removePiecePhoto(${p.id},${pi})" style="position:absolute;top:-6px;right:-6px;width:18px;height:18px;border-radius:50%;background:var(--danger);border:none;color:#fff;font-size:10px;cursor:pointer">✕</button>
            </div>
          `).join('')}
          <button onclick="addPiecePhoto(${p.id})" style="width:70px;height:50px;border:1.5px dashed var(--border);border-radius:6px;background:var(--surface);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;cursor:pointer;color:var(--muted);font-size:10px;font-weight:600">
            📷 Photo
          </button>
        </div>
      </div>
    </div>
  `).join('');
}

function addPiece(){
  const noms=['Chambre 2','Bureau','Débarras','Cave','Garage','Terrasse','Balcon'];
  edlPieces.push({id:pieceCounter++,nom:noms[pieceCounter%noms.length]||'Pièce '+pieceCounter,icone:'🏠',etat:'Bon',obs:'',photos:[]});
  renderPieces();
}

function removePiece(id){edlPieces=edlPieces.filter(p=>p.id!==id);renderPieces();}
function setPieceEtat(id,etat,el){const p=edlPieces.find(p=>p.id===id);if(p)p.etat=etat;el.closest('.chips').querySelectorAll('.chip').forEach(c=>c.classList.remove('active'));el.classList.add('active');}
function setPieceObs(id,obs){const p=edlPieces.find(p=>p.id===id);if(p)p.obs=obs;}
function removePiecePhoto(id,pi){const p=edlPieces.find(p=>p.id===id);if(p){p.photos.splice(pi,1);renderPieces();}}

function addPiecePhoto(pieceId){
  currentPieceId=pieceId;
  const modal=document.getElementById('doc-cam-modal');
  modal.querySelector('.doc-cam-title').textContent='📷 Photo de la pièce';
  modal.classList.add('open');
  window._pieceMode=true;
  startDocStream();
}

const _origConfirmDoc=window.confirmDocPhoto;
window.confirmDocPhoto=function(){
  if(window._pieceMode && currentPieceId!==null){
    const dataURL=document.getElementById('doc-cam-preview').src;
    const p=edlPieces.find(p=>p.id===currentPieceId);
    if(p)p.photos.push(dataURL);
    window._pieceMode=false; currentPieceId=null;
    closeDocCamera(); renderPieces(); showToast('✓ Photo ajoutée');
  } else { if(typeof _origConfirmDoc==='function')_origConfirmDoc(); }
};

function updateEDLRecap(){
  const labels={entree:'Entrée',sortie:'Sortie',comparatif:'Comparatif Entrée/Sortie'};
  const s=id=>{const el=document.getElementById(id);if(el)el.textContent=document.getElementById(id.replace('edl-recap-','edl-'))?.value||'—';};
  document.getElementById('edl-recap-type').textContent=labels[edlType]||edlType;
  document.getElementById('edl-recap-date').textContent=document.getElementById('edl-date')?.value||'—';
  document.getElementById('edl-recap-adresse').textContent=document.getElementById('edl-adresse')?.value||'—';
  document.getElementById('edl-recap-bailleur').textContent=(document.getElementById('edl-bailleur-nom')?.value||'')+' '+(document.getElementById('edl-bailleur-prenom')?.value||'');
  document.getElementById('edl-recap-locataire').textContent=(document.getElementById('edl-locataire-nom')?.value||'')+' '+(document.getElementById('edl-locataire-prenom')?.value||'');
  document.getElementById('edl-recap-nb-pieces').textContent=edlPieces.length+' pièce'+(edlPieces.length>1?'s':'');
}

async function generateEDLPDF(){
  showToast('Génération PDF état des lieux...');
  const {jsPDF}=window.jspdf;
  const doc=new jsPDF({orientation:'portrait',unit:'mm',format:'a4'});
  const margin=15,pageW=210,contentW=pageW-margin*2;
  let y=20;
  const labels={entree:'ENTRÉE',sortie:'SORTIE',comparatif:'ENTRÉE / SORTIE'};
  doc.setFillColor(224,82,82); doc.rect(0,0,210,32,'F');
  doc.setTextColor(255,255,255); doc.setFontSize(16); doc.setFont('helvetica','bold');
  doc.text('ÉTAT DES LIEUX — '+(labels[edlType]||''),margin,14);
  doc.setFontSize(10); doc.setFont('helvetica','normal');
  doc.text(document.getElementById('edl-adresse')?.value||'',margin,22);
  doc.text('Le '+(document.getElementById('edl-date')?.value||''),210-margin,22,{align:'right'});
  y=42;
  doc.setFillColor(245,247,251); doc.rect(margin,y-4,contentW/2-2,22,'F'); doc.rect(margin+contentW/2+2,y-4,contentW/2-2,22,'F');
  doc.setTextColor(27,108,168); doc.setFontSize(8); doc.setFont('helvetica','bold');
  doc.text('BAILLEUR',margin+4,y+2); doc.text('LOCATAIRE',margin+contentW/2+6,y+2);
  doc.setTextColor(30,30,30); doc.setFontSize(9); doc.setFont('helvetica','normal');
  doc.text((document.getElementById('edl-bailleur-nom')?.value||'')+' '+(document.getElementById('edl-bailleur-prenom')?.value||''),margin+4,y+9);
  doc.text((document.getElementById('edl-locataire-nom')?.value||'')+' '+(document.getElementById('edl-locataire-prenom')?.value||''),margin+contentW/2+6,y+9);
  y+=30;
  doc.setFillColor(224,82,82); doc.rect(margin,y-4,contentW,7,'F');
  doc.setTextColor(255,255,255); doc.setFontSize(9); doc.setFont('helvetica','bold');
  doc.text('COMPTEURS',margin+2,y+1); y+=12;
  [['Électricité','edl-elec'],['Gaz','edl-gaz'],['Eau froide','edl-eau-froide'],['Eau chaude','edl-eau-chaude']].forEach(([l,id])=>{
    const v=document.getElementById(id)?.value; if(!v) return;
    doc.setTextColor(100,100,100); doc.setFontSize(8); doc.setFont('helvetica','normal'); doc.text(l,margin+2,y);
    doc.setTextColor(30,30,30); doc.setFontSize(9); doc.setFont('helvetica','bold'); doc.text(v,margin+50,y);
    doc.setDrawColor(220,220,220); doc.line(margin,y+1,margin+contentW,y+1); y+=7;
  });
  y+=4;
  doc.setFillColor(224,82,82); doc.rect(margin,y-4,contentW,7,'F');
  doc.setTextColor(255,255,255); doc.setFontSize(9); doc.setFont('helvetica','bold');
  doc.text('ÉTAT DES PIÈCES',margin+2,y+1); y+=12;
  for(const piece of edlPieces){
    if(y>250){doc.addPage();y=20;}
    doc.setFillColor(245,247,251); doc.rect(margin,y-3,contentW,8,'F');
    doc.setTextColor(30,30,30); doc.setFontSize(10); doc.setFont('helvetica','bold');
    doc.text(piece.nom,margin+2,y+2);
    const ec={Bon:[56,168,122],Usage:[232,168,56],Mauvais:[224,82,82],'À remplacer':[155,89,182]}[piece.etat]||[100,100,100];
    doc.setFillColor(...ec); doc.roundedRect(margin+contentW-25,y-2,24,7,2,2,'F');
    doc.setTextColor(255,255,255); doc.setFontSize(7); doc.text(piece.etat,margin+contentW-13,y+2,{align:'center'});
    y+=10;
    if(piece.obs){doc.setTextColor(80,80,80);doc.setFontSize(8);doc.setFont('helvetica','normal');const lines=doc.splitTextToSize(piece.obs,contentW-4);doc.text(lines,margin+2,y);y+=lines.length*5+2;}
    if(piece.photos.length>0){let px=margin;for(const ph of piece.photos.slice(0,3)){if(y>250){doc.addPage();y=20;px=margin;}try{doc.addImage(ph,'JPEG',px,y,55,35);}catch(e){}px+=58;}y+=40;}
    doc.setDrawColor(220,220,220);doc.line(margin,y,margin+contentW,y);y+=6;
  }
  if(y>220){doc.addPage();y=20;}
  doc.setFillColor(224,82,82);doc.rect(margin,y-4,contentW,7,'F');
  doc.setTextColor(255,255,255);doc.setFontSize(9);doc.setFont('helvetica','bold');
  doc.text('SIGNATURES',margin+2,y+1);y+=12;
  const lieu=document.getElementById('edl-lieu')?.value||'';
  const dateSig=document.getElementById('edl-date-sig')?.value||'';
  doc.setTextColor(80,80,80);doc.setFontSize(8);doc.setFont('helvetica','normal');
  doc.text('Fait à '+lieu+', le '+dateSig,margin,y);y+=10;
  ['sig-edl-bailleur','sig-edl-locataire'].forEach((sigId,i)=>{
    const canvas=document.getElementById(sigId);
    const label=i===0?'Bailleur':'Locataire';
    const x=i===0?margin:margin+contentW/2+5;
    doc.setTextColor(27,108,168);doc.setFontSize(8);doc.setFont('helvetica','bold');doc.text(label,x,y);
    if(canvas){const d=canvas.getContext('2d').getImageData(0,0,canvas.width,canvas.height).data;const hasSig=Array.from(d).some((v,idx)=>idx%4===3&&v>0);if(hasSig){try{doc.addImage(canvas.toDataURL('image/png'),'PNG',x,y+2,60,20);}catch(e){}}}
    doc.setDrawColor(200,200,200);doc.line(x,y+22,x+60,y+22);
  });
  const total=doc.internal.getNumberOfPages();
  for(let i=1;i<=total;i++){doc.setPage(i);doc.setFillColor(224,82,82);doc.rect(0,287,210,10,'F');doc.setTextColor(255,255,255);doc.setFontSize(7);doc.text('État des lieux — '+(labels[edlType]||'')+' — Page '+i+'/'+total,105,293,{align:'center'});}
  doc.save('etat_des_lieux_'+edlType+'_'+new Date().toISOString().split('T')[0]+'.pdf');
  showToast('✓ PDF état des lieux téléchargé !');
}
"""

# Injecter le JS avant init()
html = html.replace('updateTime(); setInterval(updateTime,30000); setTodayDates();',
    edl_js + '\nupdateTime(); setInterval(updateTime,30000); setTodayDates();')

# Mettre à jour generatePDF pour EDL
html = html.replace(
    "async function generatePDF(){if(!activeBail){",
    "async function generatePDF(){if(activeBail==='edl'){generateEDLPDF();return;}if(!activeBail){"
)

# Mettre à jour showSection pour recap EDL
html = html.replace(
    "document.getElementById('btn-pdf').style.display =\n    current === cfg.steps.length - 1 ? 'flex' : 'none';",
    "document.getElementById('btn-pdf').style.display =\n    current === cfg.steps.length - 1 ? 'flex' : 'none';\n  if(activeBail==='edl' && current===cfg.steps.length-1) updateEDLRecap();"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('OK etape 3')
