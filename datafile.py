# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m          =====  Mac_Analyzer *args  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def mac_analyzer(target_server,*mac_list):
    print(f"\033[1;3;33m[+] Target Locked: {target_server}\033[0m\n")
    time.sleep(1)
    for mac in mac_list:
        if mac == "AA:BB:CC:DD:EE:FF":
           print("\033[1;3;32m VIP mac skipping...\033[0m")
           time.sleep(1)
           continue
#           print(f"\033[1;3;33m--> Authenticating mac: {mac}\033[0m")
#           time.sleep(1)
        elif mac == "12:34:56:78:9A:BC":
            time.sleep(1)
            return "\033[1;91m[!] Aleart Unkown mac_address\033[0m"
        print(f"\033[1;3;33m--> Authenticating mac:  {mac}\033[0m")
        time.sleep(1)
result = mac_analyzer("main_router","00:1A:2B:3C:4D:5E","F8:1A:67:B2:99:C3","AA:BB:CC:DD:EE:FF","12:34:56:78:9A:BC","FF:FF:FF:FF","11:22:33:44:55")
print(result)
time.sleep(1)
