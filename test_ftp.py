import ftplib

try:
    print("Connecting to stretch-plus.co.jp...")
    ftp = ftplib.FTP('stretch-plus.co.jp', timeout=10)
    ftp.login('gravity@stretch-plus.co.jp', 'gravitystretch_21314')
    print("Logged in successfully. Current directory:", ftp.pwd())
    print("\nListing root directory contents:")
    ftp.retrlines('LIST')
    
    # Check if wp-content exists
    print("\nAttempting to locate wp-content/themes...")
    try:
        ftp.cwd('wp-content')
        print("Successfully navigated to wp-content.")
        ftp.cwd('themes')
        print("Successfully navigated to wp-content/themes.")
        print("\nListing themes directory contents:")
        ftp.retrlines('LIST')
    except Exception as e:
        print("Could not navigate to wp-content/themes. Reason:", e)

    ftp.quit()
except Exception as e:
    print("FTP Error:", e)
