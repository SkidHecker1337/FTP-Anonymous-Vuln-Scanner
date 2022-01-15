import ftplib
import os
import sys
import time
import pyfiglet
os.system("clear")
ascci = pyfiglet.figlet_format("Anonymous login Vuln-Scanner")
print("Author :")
print(ascci)
user = "anonymous"
password = ""
port = 21 

def exploit():
        target = input("[*] Taregt Ip :")
        server = ftplib.FTP()
        print("[*] Trying exploit....")
        time.sleep(2)
        try:
            server.connect(target, port, timeout=10)
            server.login(user, password)
        except ftplib.error_perm:
            print("[*] Target is not vulnerbale to exploit")
            return False
        except ftplib.error_temp:
            print("[*] Error 421")
            return False
        except KeyboardInterrupt:
            print("[*] User pressed ctrl+c....")
            sys.exit()
        else:
            print("[*] Target is vulnerbale to exploit")
            return True
            
exploit()
time.sleep(3)
os.system("python3 main.py")