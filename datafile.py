# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m     ===== IDS Simulator with *args  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def log_analyzer(server_name,*ip_address):
    for ip in ip_address:
        print("\033[1;3;36m[+] Cheking IP...\033[0m")
        time.sleep(1)
        if ip == "127.0.0.1":
            print(f"\033[1;3;32m-->  {ip} local host is skipping...\033[0m")
            time.sleep(1)
            continue
        elif ip == "6.6.6.6":
            time.sleep(0.05)
            return f"\033[1;3;31m>>> Unknown Attacker! SYSTEM LOCKDOWN\033[0m"
#            time.sleep(1)
        else:
            print(f"\033[1;3;33m[*] Safe ip {ip}\033[0m")
            time.sleep(1)
result = log_analyzer("Mainframe","8.8.8.8","111.90.11.6","127.0.0.1","666.767.7.3","6.6.6.6","675.33.22.1")
print(result)
time.sleep(1)
#log_analyzer("Mainframe",8,8,8,8,55, 111,90,11,6, 127,0,0,1, 666,767,7,3, 6,6,6,6, 675,33,22,1)
