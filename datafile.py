# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m          ===== ​Port_checker.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def target_scan(ips,*ports):
    print("\033[1;3;35m[+] Scan system ...\033[0m")
    time.sleep(1)
    count = len(ips)
    print(f"\033[1;3;34m Total Ip: {count}\033[0m")
    time.sleep(1)
    print("\033[1;96m" + "="*50)
    time.sleep(1)
    for ip in ips:
        print(f"\033[1;91m Target_ip locked: {ip}\033[0m\n")
        time.sleep(1)
        for port in [44,22,70,21,3309,8280,80,3332,3391,8080,42,79]:
            if port == 21:
                print(f"\033[1;3;46m--> Port {port}: is skipping\033[0m")
                time.sleep(1)
                continue
            elif port == 80:
                print(f"\033[1;3;32m✓ Port {port}: Secure port\033[0m")
                time.sleep(1)
            elif port == 8080:
                print(f"\033[1;3;31m>>> Port {port}: High Alert Port\033[0m")
                time.sleep(1)
                print("\033[1;91m" + "="*50)
                time.sleep(1)
                break
            else:
                print(f"\033[1;3;33m[~] Port {port}: Normal Port\033[0m")
                time.sleep(1)
target_scan(["127.0.0.1","192.0.2.1"])
