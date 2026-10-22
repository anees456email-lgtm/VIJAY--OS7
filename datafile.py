# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
print()
print("\033[1;3;35m  ​====== DUMMY NETWORK SCANNER ======  ")
print("\033[0m")
print("\033[1;96m" + "="*50)
print("\033[0m")
print()
target_port = 4444
def port_scanner(start,end):
    for port in range(start,end):
        if port == 80:
            print(f"\033[1;91m>>> port {port} Honeypot trap detected skipping...\033[0m")
            continue
        elif port == 4444:
            print(f"\033[1;3;92m>>> SUCCESS target port {port} is Open\033[0m")
            time.sleep(0.01)
            break
        else:
            print(f"\033[1;93m Scanning port {port} Closed...\033[0m")
            time.sleep(0.01)
port_scanner(70,4450)
