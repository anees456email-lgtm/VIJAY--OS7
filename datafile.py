# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[1;96m" + "—"*50)
time.sleep(1)
print()
print("\033[1;3;36m          ===== ​Target_Scanner.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[0m")
print()
def scanner_logger(ip,scan_type,*ports,**details):
    print()
    print("\033[1;3;33m Starting Scanner...\033[0m")
    time.sleep(1)
    print(f"\033[1;3;31m Target Ip: {ip}\033[0m")
    time.sleep(1)
    print(f"\033[1;3;35m Scan Type: {scan_type}\033[0m")
    time.sleep(1)
    total_entries = len(details)
    print(f"\033[1;3;34m Total Entries: {total_entries}\033[0m")
    time.sleep(1)
    if len(ports) == 0 and len(details) == 0:
        print("\033[1;3;37m No ports or extra details\033[0m")
        time.sleep(1)
        print("\033[1;96m" + "_" *50 + "\033[0m")
        time.sleep(1)
        return
    for port in ports:
        if port == 8080:
            print(f"\033[1;3;36m>>> Port {port} is Proxy\033[0m")
            time.sleep(1)
        elif port == 443:
            print(f"\033[1;3;31m-> Port {port} is honeypot\033[0m")
            time.sleep(1)
            break
        else:
            print(f"\033[1;3;33m--> Port {port} is Normal\033[0m")
            time.sleep(1)
    for key,value in details.items():
        print(f"\033[1;3;32m {key} --> {value}\033[0m")
        time.sleep(1)
scanner_logger("127.0.0.1","Quick")
scanner_logger("192.168.0.1","fast",21,43,22,3601,8080,77,443,5512,os="Linux",server="Nginx",status="Active")
