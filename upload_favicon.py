import ftplib
import os

FTP_HOST = "stretch-plus.co.jp"
FTP_USER = "gravity@stretch-plus.co.jp"
FTP_PASS = "gravitystretch_21314"
REMOTE_DIR = "stretch-plus.co.jp/public_html/v2/wp-content/themes/stretchplus-theme"

files_to_upload = {
    "stretchplus-theme/header.php": "header.php",
    "stretchplus-theme/image_final/favicon.png": "image_final/favicon.png"
}

print("Connecting to FTP...")
try:
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.cwd(REMOTE_DIR)
    
    for local_path, remote_path in files_to_upload.items():
        if os.path.exists(local_path):
            print(f"Uploading {remote_path}...")
            # create directory if it's image_final and might not exist (though it should)
            if "/" in remote_path:
                dir_name = remote_path.split("/")[0]
                try:
                    ftp.cwd(dir_name)
                    ftp.cwd("..")
                except:
                    ftp.mkd(dir_name)
            
            with open(local_path, "rb") as f:
                ftp.storbinary(f"STOR {remote_path}", f)
        else:
            print(f"Missing {local_path}")
            
    ftp.quit()
    print("Upload complete!")
except Exception as e:
    print(f"FTP Error: {e}")
