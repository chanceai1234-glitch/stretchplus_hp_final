import re

files_to_update = [
    '/Users/ai_stretch/Desktop/stretchplus HPremake final/style.css',
    '/Users/ai_stretch/Desktop/stretchplus HPremake final/redesign/style.css'
]

typography_rules_map = {
    # H2 clamp: 1.8rem, 3vw, 2.4rem
    '#policy h2': 'clamp(1.8rem, 3vw, 2.4rem)',
    '.amenities-container h2': 'clamp(1.8rem, 3vw, 2.4rem)',
    '.shop-info-block h2': 'clamp(1.8rem, 3vw, 2.4rem)',
    '.shop-access-block h2': 'clamp(1.8rem, 3vw, 2.4rem)',
    '#cta-1 h2': 'clamp(1.8rem, 3vw, 2.4rem)',
    '#cta-2 h2': 'clamp(1.8rem, 3vw, 2.4rem)',
    
    # H3 section sub-headings: 1.3rem
    '.about-content h3': '1.3rem',
    '.faq-category h3': '1.3rem',
    '.amenity-content h3': '1.3rem',
    '.step-title-inline': '1.3rem',
    
    # H3 card titles: 1.2rem
    '.policy-card h3': '1.2rem',
    '.pricing-card h3': '1.2rem',
    '.step-details h3': '1.2rem',
    '.trainer-card h3': '1.2rem',
    '.concern-card h3': '1.2rem',
    '.access-card-text h3': '1.2rem',
    
    # P lead text: 1.05rem
    '.about-content p': '1.05rem',
    '.worries-lead': '1.05rem',
    '.policy-lead': '1.05rem',
    '.action-lead': '1.05rem',
    
    # P standard text: 0.95rem
    '.policy-strong': '0.95rem',
    '.worries-card-sub': '0.95rem',
    '.step-details p': '0.95rem',
    '.trainer-card p': '0.95rem',
    '.access-card-text p': '0.95rem',
    '.concern-card p': '0.95rem',
    '.amenity-content p': '0.95rem',
    '.step-desc': '0.95rem'
}

def update_css(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply typography rules
    for selector, new_size in typography_rules_map.items():
        # Match the block for the given selector
        # Regex explanation:
        # Match the selector optionally preceded by whitespace or comma,
        # then any characters up to {
        # then inside the {} block, find `font-size: <something>;`
        
        # We need a robust way to replace font-size inside specific blocks.
        # Since CSS blocks can be complex, let's use a function and re.sub
        
        def replace_font_size(match):
            block_content = match.group(0)
            # Find and replace font-size within this block
            updated_block = re.sub(r'font-size:\s*[^;]+;', f'font-size: {new_size};', block_content)
            return updated_block

        # This regex matches the exact selector followed by '{' and text until '}'
        # Using negative lookahead to ensure we don't match '}' inside the block
        # Added handling for multiple selectors like `.shop-info-block h2,\n.shop-access-block h2 {`
        pattern = re.compile(rf'(?:^|\s|,){re.escape(selector)}(?:\s|,)[^{{]*{{(?:[^{{}}]|)*}}', re.MULTILINE)
        
        # Let's try a safer approach: split by }
        blocks = content.split('}')
        for i, block in enumerate(blocks):
            if selector in block.split('{')[0]:
                if 'font-size:' in block:
                    blocks[i] = re.sub(r'font-size:\s*[^;]+;', f'font-size: {new_size};', block)
                else:
                    # If font-size isn't there, append it (less common, but safe)
                    if '{' in block:
                        parts = block.split('{')
                        blocks[i] = parts[0] + '{\n    font-size: ' + new_size + ';' + parts[1]

        content = '}'.join(blocks)
        
    # Remove font-family from .bottom-cta-banner block
    blocks = content.split('}')
    for i, block in enumerate(blocks):
        if '.bottom-cta-banner' in block.split('{')[0] and 'font-family:' in block:
            blocks[i] = re.sub(r'font-family:\s*[^;]+;', '', block)
    content = '}'.join(blocks)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
for file in files_to_update:
    update_css(file)
    print(f"Updated {file}")
