import ftplib

FTP_HOST = "stretch-plus.co.jp"
FTP_USER = "gravity@stretch-plus.co.jp"
FTP_PASS = "gravitystretch_21314"
REMOTE_DIR = "stretch-plus.co.jp/public_html/v2/wp-content/themes/stretchplus-theme/template-parts"

local_file = "stretchplus-theme/template-parts/section-hero.php"
remote_file = "section-hero.php"

print("Connecting to FTP...")
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.cwd(REMOTE_DIR)
with open(local_file, "rb") as f:
    ftp.storbinary(f"STOR {remote_file}", f)
ftp.quit()
print("Upload complete!")
