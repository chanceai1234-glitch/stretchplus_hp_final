import ftplib
import os

FTP_HOST = "stretch-plus.co.jp"
FTP_USER = "gravity@stretch-plus.co.jp"
FTP_PASS = "gravitystretch_21314"
REMOTE_DIR = "stretch-plus.co.jp/reports"

weekly_sh = """#!/bin/bash
/usr/bin/python3 -m pip install --user python-dotenv google-analytics-data anthropic
/usr/bin/python3 /home/gravity/stretch-plus.co.jp/reports/report_weekly.py
"""

monthly_sh = """#!/bin/bash
/usr/bin/python3 -m pip install --user python-dotenv google-analytics-data anthropic
/usr/bin/python3 /home/gravity/stretch-plus.co.jp/reports/report_monthly.py
"""

with open("run_weekly.sh", "w") as f:
    f.write(weekly_sh)

with open("run_monthly.sh", "w") as f:
    f.write(monthly_sh)

print("Connecting to FTP...")
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.cwd(REMOTE_DIR)

for file in ["run_weekly.sh", "run_monthly.sh"]:
    print(f"Uploading {file}...")
    with open(file, "rb") as f:
        ftp.storbinary(f"STOR {file}", f)
    # 実行権限を付与 (755)
    ftp.sendcmd(f"SITE CHMOD 755 {file}")

ftp.quit()
print("Upload complete!")
