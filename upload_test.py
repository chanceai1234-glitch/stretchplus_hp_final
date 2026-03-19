import ftplib
import io

html_content = b"<h1>FTP Sync Active</h1><p>If you can see this, the FTP connection is pointing to the correct public folder!</p>"
bio = io.BytesIO(html_content)

try:
    ftp = ftplib.FTP('stretch-plus.co.jp', timeout=10)
    ftp.login('gravity@stretch-plus.co.jp', 'gravitystretch_21314')
    ftp.storbinary('STOR detect.html', bio)
    print("Successfully uploaded detect.html to the FTP root.")
    ftp.retrlines('LIST')
    ftp.quit()
except Exception as e:
    print("Upload error:", e)
