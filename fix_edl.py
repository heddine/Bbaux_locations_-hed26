with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Verifier si screen-edl existe deja
if 'screen-edl' in html:
    print('screen-edl deja present')
else:
    print('screen-edl ABSENT - ajout necessaire')
    
# Verifier si startEDL existe
if 'startEDL' in html:
    print('startEDL present')
else:
    print('startEDL ABSENT')
