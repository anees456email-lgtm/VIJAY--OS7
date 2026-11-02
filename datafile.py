# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[1;94m" + "="*50)
time.sleep(1)
print()
print("\033[1;3;36m         ====== DUMMY IP_SCANNER  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def network_scanner(*ip_address):
    for p in ip_address:
        if p == "192.168.1.1":
            print("\033[1;91m--> Adnin Router Bypassing...\033[0m")
            time.sleep(1)
            continue
        print(f"\033[1;93m--> scanning target_ip: {p}\033[0m")
        time.sleep(1)
#        if p == "192.168.1.1":
#        if ip_address == "192.168.1.1":
#            print("\033[1;91m--> Adnin Router Bypassing...\033[0m")
#            time.sleep(1)
#            continue
network_scanner("213.872.0.1","542.752.9.0","625,6,88,0","76.99.534.9","192.168.1.1","652.9.66.0","12.21.0.0")
