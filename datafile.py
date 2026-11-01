# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[1;94m" + "="*50)
time.sleep(1)
print()
print("\033[1;3;35m         ====== DUMMY PORT_SCANNER  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def ip_scan(target_ip,*ports):
    print(f"\033[1;93m--> Target locked {target_ip}\033[0m")
    time.sleep(1)
    for port in ports:
        if port == 45:
           # continue
            print(f"\033[1;91m>>> port {port} critical port\033[0m\n")
            time.sleep(1)
            continue
        print(f"\033[1;96m Scanning port {port}\033[0m\n")
        time.sleep(1)
ip_scan("127.0.0.1",80,8080,22,21,45,40,42)
