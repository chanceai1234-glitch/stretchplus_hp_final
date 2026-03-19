import os
import time
import re

filepaths = ['index.html', 'redesign/index.html', 'stretchplus-theme/header.php']
buster = f"?cb={int(time.time()*1000)}\""

for filepath in filepaths:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Replace either ?v=.. or ?cb=..
        html = re.sub(r'\?[v|cb]=[0-9]+"', buster, html)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
            
print("Global Advanced Cache Bust completed.")
