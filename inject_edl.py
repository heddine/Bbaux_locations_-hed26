import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Ajouter carte EDL dans bail-grid
bail_card = '''      <div class="bail-card" style="border-left:4px solid #E05252" onclick="startEDL()">
        <div class="bail-icon" style="background:#E05252"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg></div>
        <div class="bail-info"><div class="bail-name">État des Lieux</div><div class="bail-meta">Entrée &amp; Sortie comparatif</div><span class="bail-badge" style="background:rgba(224,82,82,.12);color:#E05252">Photos + Signatures + PDF</span></div>
        <div class="bail-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg></div>
      </div>
    </div>'''

html = html.replace('    </div><!-- /bail-grid -->', bail_card)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('OK etape 1')
