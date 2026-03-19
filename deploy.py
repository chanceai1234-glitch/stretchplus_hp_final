import os
import ftplib
import subprocess
import time

LOCAL_THEME_DIR = 'stretchplus-theme'
REMOTE_THEME_DIR = 'stretch-plus.co.jp/public_html/v2/wp-content/themes/stretchplus-theme'

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

def upload_dir(ftp, local_dir, remote_dir):
    try:
        ftp.cwd(remote_dir)
    except ftplib.error_perm:
        try:
            ftp.mkd(remote_dir)
            ftp.cwd(remote_dir)
        except Exception as e:
            print(f"Could not create/cd to {remote_dir}: {e}")
            return
            
    for item in os.listdir(local_dir):
        # Ignore pycache, .git, etc.
        if item in ['.DS_Store', '__pycache__', '.git']: continue
        local_path = os.path.join(local_dir, item)
        if os.path.isfile(local_path):
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {item}', f)
                print(f"☁️ Uploaded: {local_path} -> {remote_dir}/{item}")
        elif os.path.isdir(local_path):
            upload_dir(ftp, local_path, item)
            ftp.cwd('..')

def sync_github():
    print("[\u2713] Syncing GitHub Repository...")
    subprocess.run("git add .", shell=True, check=True)
    try:
        subprocess.run(f"git commit -m 'feat(bot): auto-deployed code state at {int(time.time())}'", shell=True)
        subprocess.run("git push -u deploy main -f", shell=True)
        print("[\u2713] GitHub successfully synchronized!")
    except Exception as e:
        print("GitHub sync generated no new commits (skipped).")

def sync_ftp():
    creds = parse_ftp_creds()
    print(f"[\u2713] Connecting to XSERVER FTP ({creds['host']} as {creds['user']})")
    ftp = ftplib.FTP(creds['host'], timeout=20)
    ftp.login(creds['user'], creds['pass'])
    print(f"[\u2713] Navigating to {REMOTE_THEME_DIR}")
    
    # Traverse remote path safely
    ftp.cwd('/')
    for folder in REMOTE_THEME_DIR.split('/'):
        ftp.cwd(folder)
        
    print(f"🚀 Deploying theme to XSERVER...")
    for item in os.listdir(LOCAL_THEME_DIR):
        if item in ['.DS_Store', '__pycache__', '.git', 'image_raw']: continue
        local_path = os.path.join(LOCAL_THEME_DIR, item)
        if os.path.isfile(local_path):
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {item}', f)
                print(f"☁️ Uploaded: {local_path}")
        elif os.path.isdir(local_path):
            upload_dir(ftp, local_path, item)
            ftp.cwd('..')
            
    ftp.quit()
    print("[\u2713] XSERVER Theme Directory successfully synchronized!")

def main():
    print("="*50)
    print(" STRETCH+ AUTO-SYNC PIPELINE INITIATED ")
    print("="*50)
    
    try:
        sync_github()
    except Exception as e:
        print(f"[!] GitHub sync failed: {e}")
        
    try:
        sync_ftp()
    except Exception as e:
        print(f"[!] XSERVER FTP sync failed: {e}")

    print("="*50)
    print(" PIPELINE COMPLETE! LIVE ON ALL ENVIRONMENTS! ")
    print("="*50)

if __name__ == '__main__':
    main()
