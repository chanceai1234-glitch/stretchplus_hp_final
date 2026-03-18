import os

files = [
    'stretchplus-theme/template-parts/section-flow.php',
    'redesign/index.html',
    'index.html'
]

replacements = {
    'ご来店いただきましたら、ご予約内容を確認させていただいたあと、シャワールームなどの設備のご説明とともに、完全個室の施術室へご案内いたします。': 'ご来店いただきましたら、ご予約内容を確認させていただいた後、シャワールームなどの設備をご説明させていただいたうえで、施術室へご案内いたします。',
    
    'M・L・2L・3L・4Lとお体のサイズに合わせた施術着をご用意しております。個室にてゆっくりお着替えください。': 'M、L、2L、3L、4Lとお体のサイズに合わせた施術着をご用意しております。個室にてゆっくりお着替えください。<br><br>なお、ご要望に応じて靴下等もご用意ございますので、必要に応じてお申し付けください。',
    
    '<h3 class="step-title-inline">ヒアリング・ご相談</h3>': '<h3 class="step-title-inline">ヒアリング</h3>',
    
    '施術着からお着替えください。室内にウォーターサーバーをご用意しておりますので、水分補給もご自由にどうぞ。': '施術着からお着替えください。室内にウォーターサーバーもご用意しておりますので、必要に応じて、施術後の水分補給にご活用ください。'
}

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")
