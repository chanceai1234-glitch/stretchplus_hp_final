import ftplib
import os

FTP_HOST = "stretch-plus.co.jp"
FTP_USER = "gravity@stretch-plus.co.jp"
FTP_PASS = "gravitystretch_21314"
REMOTE_DIR = "stretch-plus.co.jp/reports"

files_to_upload = [
    "report_weekly.py",
    "report_monthly.py",
    ".env",
    "service-account.json"
]

print("Connecting to FTP...")
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)

try:
    ftp.cwd(REMOTE_DIR)
except ftplib.error_perm:
    print(f"Creating directory {REMOTE_DIR}...")
    ftp.cwd("stretch-plus.co.jp")
    try:
        ftp.mkd("reports")
    except Exception as e:
        print(f"Directory may already exist: {e}")
    ftp.cwd("reports")

for file in files_to_upload:
    local_path = os.path.join("/Users/ai_stretch/Desktop/stretchplus HPremake final", file)
    if os.path.exists(local_path):
        print(f"Uploading {file}...")
        with open(local_path, "rb") as f:
            ftp.storbinary(f"STOR {file}", f)
    else:
        print(f"Missing {file}")

ftp.quit()
print("Upload complete!")
