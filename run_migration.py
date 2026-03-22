import ftplib
import os
import urllib.request
import time

def parse_ftp_creds():
    creds = {}
    with open('ftp_info.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            if 'FTP;' in line or 'FTPサーバー名' in line:
                creds['host'] = line.split(';')[1].strip() if ';' in line else line.split(':')[1].strip()
            elif 'FTPユーザID' in line or 'FTPユーザー名' in line:
                creds['user'] = line.split('：')[1].strip() if '：' in line else line.split(':')[1].strip()
            elif 'パスワード' in line:
                creds['pass'] = line.split('：')[1].strip() if '：' in line else line.split(':')[1].strip()
    return creds

def main():
    creds = parse_ftp_creds()
    print(f"Connecting to FTP {creds['host']}...")
    ftp = ftplib.FTP(creds['host'], timeout=20)
    ftp.login(creds['user'], creds['pass'])
    
    # Upload migrator to /public_html/v2/
    target_dir = "stretch-plus.co.jp/public_html/v2"
    ftp.cwd('/')
    for folder in target_dir.split('/'):
        ftp.cwd(folder)
        
    print("Uploading migrator.php...")
    with open('migrator.php', 'rb') as f:
        ftp.storbinary('STOR migrator.php', f)
        
    ftp.quit()
    
    # Execute the migrator via HTTP
    print("Executing migrator script. Please wait...")
    time.sleep(2)
    response = urllib.request.urlopen("https://stretch-plus.co.jp/v2/migrator.php")
    text = response.read().decode('utf-8')
    
    if "MIGRATION_SUCCESS" in text:
        print("[SUCCESS] Domain swap completed and database options updated.")
    else:
        print("[FAIL] Migration failed or returned unexpected output.")
        print("Response:", text)

        
    print("Cleanup: Removing migrator.php via FTP...")
    ftp = ftplib.FTP(creds['host'], timeout=20)
    ftp.login(creds['user'], creds['pass'])
    ftp.cwd('/')
    for folder in target_dir.split('/'):
        ftp.cwd(folder)
    try:
        ftp.delete('migrator.php')
        print("Migrator script safely deleted.")
    except Exception as e:
        print(f"Could not delete migrator.php: {e}")
    ftp.quit()

if __name__ == "__main__":
    main()
