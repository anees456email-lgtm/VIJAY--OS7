# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m         ===== ​Venom_DirBuster.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def web_fuzzer(target_url,*directories,auth_token,proxy_mode):
    print(f"\033[1;3;41m[*] Target Locked: {target_url}\033[0m")
    time.sleep(1)
    if auth_token != "venom123":
        time.sleep(1)
        return "\033[1;3;31m[!] Invlide Token Connection Dropped\033[0m"
    if proxy_mode == True:
        print("\033[1;3;34m[+] Stealth Proxy Active:\033[0m")
        time.sleep(1)
    else:
#        time.sleep(1)
        print("\033[1;3;31m No Proxy Active\033[0m")
        time.sleep(1)
#        return "\033[1;3;31m[!] Invlide Token Connection Dropped\033[0m"
    for i in directories:
        if i == "robots.txt":
            continue
        elif i == "admin_panel":
            time.sleep(1)
            return f"\033[1;3;32m--> Jackpot found: {i}\033[0m"
        else:
            print(f"\033[1;3;33m--> Scanning: {target_url}/ {i}\033[0m")
            time.sleep(1)
result = web_fuzzer("[www.target.com]","images","robots.txt","css","admin_panel","jss",auth_token = "venom123",proxy_mode =True)
print(result)
time.sleep(1)
