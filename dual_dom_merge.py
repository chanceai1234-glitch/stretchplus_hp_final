import os
import subprocess

def get_git_file(commit, path):
    result = subprocess.run(["git", "show", f"{commit}:{path}"], capture_output=True, text=True)
    return result.stdout

def merge_faq():
    # FAQ is easy: just wrap both entirely
    pc_faq = get_git_file("PC_STABLE_FINAL", "stretchplus-theme/template-parts/section-faq.php")
    sp_faq = get_git_file("HEAD", "stretchplus-theme/template-parts/section-faq.php")
    
    # Check if we already merged
    with open("stretchplus-theme/template-parts/section-faq.php", "r") as f:
        curr = f.read()
        if "sp-only" in curr and "pc-only" in curr:
            return

    combined = f"""
<!-- ====== DESKTOP FAQ ====== -->
<div class="pc-only">
{pc_faq}
</div>

<!-- ====== MOBILE FAQ (TABS) ====== -->
<div class="sp-only" style="padding: 60px 0;">
    <div class="container">
{sp_faq}
    </div>
</div>
"""
    # Wait, sp_faq already contains <section id="faq">
    # If we nest it, it's fine. 
    # Let's cleanly strip some duplicate wrappers if needed, but nesting is safest.
    
    with open("stretchplus-theme/template-parts/section-faq.php", "w") as f:
        f.write(combined)
    print("✅ section-faq.php dual-dom merged.")

def merge_footer():
    pc_footer = get_git_file("PC_STABLE_FINAL", "stretchplus-theme/footer.php")
    sp_footer = get_git_file("HEAD", "stretchplus-theme/footer.php")
    
    # We want PC footer to be wrapped in pc-only.
    # We want SP footer (the sticky nav, simplified footer) to be injected before <script> in pc_footer.
    
    # Extract SP pieces from sp_footer:
    # 1. simplified footer
    # 2. sticky nav
    # 3. back to top
    
    sp_pieces = ""
    # Look for the start of the SP footer in the HEAD version
    if '<footer id="footer">' in sp_footer:
        sp_footer_block = sp_footer.split('<footer id="footer">')[1].split('</footer>')[0]
        sp_pieces += '\n<footer id="footer" class="sp-only">\n' + sp_footer_block + '\n</footer>\n'
        
    if '<div class="sp-sticky-nav' in sp_footer:
        sp_sticky = sp_footer.split('<div class="sp-sticky-nav')[1].split('</div>\n\n')[0]
        sp_pieces += '\n<div class="sp-sticky-nav' + sp_sticky + '</div>\n'
        
    if '<a href="#" class="back-to-top' in sp_footer:
        bt_top = sp_footer.split('<a href="#" class="back-to-top')[1].split('</a>')[0]
        sp_pieces += '\n<a href="#" class="back-to-top' + bt_top + '</a>\n'

    # Prepare the PC footer by adding pc-only to banner, footer, floating-qr
    out_lines = []
    lines = pc_footer.split('\n')
    inside_script = False
    for line in lines:
        if '<div class="bottom-cta-banner">' in line:
            line = line.replace('<div class="bottom-cta-banner">', '<div class="bottom-cta-banner pc-only">')
        if '<footer id="footer">' in line:
            line = line.replace('<footer id="footer">', '<footer id="footer" class="pc-only">')
        if '<div id="floating-qr">' in line:
            line = line.replace('<div id="floating-qr">', '<div id="floating-qr" class="pc-only">')
            
        if '<script>' in line:
            if not inside_script:
                # Inject SP pieces before scripts
                out_lines.append(sp_pieces)
        out_lines.append(line)
        
    with open("stretchplus-theme/footer.php", "w") as f:
        f.write('\n'.join(out_lines))
    print("✅ footer.php dual-dom merged.")

merge_faq()
merge_footer()
