import os

files_to_fix = [
    'stretchplus-theme/footer.php',
    'index.html',
    'redesign/index.html'
]

search_string = """            // Animate flow cards sequentially
            document.querySelectorAll('.flow-card').forEach(el => {
                observer.observe(el);
            });"""

replace_string = """            // Animate flow cards sequentially
            document.querySelectorAll('.flow-card').forEach(el => {
                observer.observe(el);
            });
            
            // Animate standard reveal elements
            document.querySelectorAll('.reveal').forEach(el => {
                observer.observe(el);
            });"""

for f in files_to_fix:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if "document.querySelectorAll('.reveal').forEach" not in content:
            content = content.replace(search_string, replace_string)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
        print(f"Fixed {f}")
