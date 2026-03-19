import ftplib

try:
    ftp = ftplib.FTP('stretch-plus.co.jp', timeout=10)
    ftp.login('gravity@stretch-plus.co.jp', 'gravitystretch_21314')
    
    print("Checking for target theme directory...")
    target_path = 'stretch-plus.co.jp/public_html/v2/wp-content/themes/stretchplus-theme'
    
    try:
        ftp.cwd(target_path)
        print("✅ SUCCESS: Found the theme directory!")
        ftp.retrlines('LIST')
    except Exception as e:
        print("❌ FAILED: Could not find", target_path)
        print("Reason:", e)

    ftp.quit()
except Exception as e:
    print("FTP Error:", e)
