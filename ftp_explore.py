import ftplib

try:
    ftp = ftplib.FTP('stretch-plus.co.jp', timeout=10)
    ftp.login('gravity@stretch-plus.co.jp', 'gravitystretch_21314')
    
    print("=== CURRENT ROOT ===")
    print("PWD:", ftp.pwd())
    ftp.retrlines('LIST')
    
    print("\n=== GOING UP ONE LEVEL ===")
    try:
        ftp.cwd('..')
        print("PWD:", ftp.pwd())
        ftp.retrlines('LIST')
    except Exception as e:
        print("Failed to go up:", e)
        
    print("\n=== GOING UP ANOTHER LEVEL ===")
    try:
        ftp.cwd('..')
        print("PWD:", ftp.pwd())
        ftp.retrlines('LIST')
    except Exception as e:
        print("Failed to go up:", e)

    ftp.quit()
except Exception as e:
    print("FTP Error:", e)
