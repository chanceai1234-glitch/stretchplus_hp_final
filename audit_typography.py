import re

def audit_typography(css_file):
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    # Find all blocks
    blocks = re.findall(r'([^{]+)\{([^}]+)\}', content)

    typography_rules = []
    for selector, rules in blocks:
        selector = selector.strip()
        rules = rules.strip()
        
        # Look for font-size or font-family
        font_size = re.search(r'font-size:\s*([^;]+);', rules)
        font_family = re.search(r'font-family:\s*([^;]+);', rules)
        
        if font_size or font_family:
            rule_set = {
                'selector': selector,
                'font-size': font_size.group(1).strip() if font_size else None,
                'font-family': font_family.group(1).strip() if font_family else None
            }
            typography_rules.append(rule_set)

    with open('typography_audit.txt', 'w', encoding='utf-8') as out:
        out.write("--- Typography Audit ---\n")
        for rule in typography_rules:
            if '@media' not in rule['selector']:
                size = rule['font-size'] or 'N/A'
                family = rule['font-family'] or 'N/A'
                out.write(f"{rule['selector'].ljust(40)} | Size: {size.ljust(25)} | Family: {family}\n")

if __name__ == '__main__':
    audit_typography('/Users/ai_stretch/Desktop/stretchplus HPremake final/style.css')
