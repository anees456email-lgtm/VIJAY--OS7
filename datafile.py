# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[1;96m" + "—"*50)
time.sleep(1)
print()
print("\033[1;3;36m          ===== ​​Server Audit.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[0m")
print()
def server_audit(server,**settings):
    print()
    print("\033[1;3;35m Server Auditing Starting...\033[0m")
    time.sleep(1)
    print()
    total_entries = len(settings)
    print(f"\033[1;3;42m Server: {server}\033[0m")
    time.sleep(1)
    if not settings:
        time.sleep(0.05)
        print("\033[1;3;37m No Settings Available\033[0m")
        return
    print()
    alert = 0
    for key,value in settings.items():
        print(f"\033[1;3;32m {key} -> {value}\033[0m")
        time.sleep(1)
        if key == "root_login" and value == "on":
            print("\033[1;3;31m Critical Alert\033[0m")
            time.sleep(1)
            alert += 1
        elif key == "firewall" and value == "off":
            print("\033[1;3;33m Very Critical Alert\033[0m")
            time.sleep(1)
            alert += 1
        elif value == "outdated":
            print("\033[1;3;33m Critical Alert\033[0m")
            time.sleep(1)
            alert += 1
        elif value == "weak":
            print("\033[1;3;41m Most Critical Alert\033[0m")
            time.sleep(1)
            alert += 1
        else:
            print(f"\033[1;3;36m Safe Setting\033[0m")
            time.sleep(1)
    print("\033[1;96m" + "=" *50 + "\033[0m")
    time.sleep(1)
    print(f"\033[1;3;34m Total Entries: {total_entries}\033[0m")
    time.sleep(1)
    if alert == 0:
        print(f"\033[1;3;4;32m Total Alert:({alert}) Server -> [{server}] Is Secure\033[0m")
        time.sleep(1)
    else:
        print(f"\033[1;3;4;31m Total Alert:({alert}) Server >> [{server}] Is Risky\033[0m")
        time.sleep(1)
server_audit("Main_DB")
server_audit("DB_Main",port=22,firewall="off",root_login="on",password="weak",software="outdated")
server_audit("Ubuntu",firewall="on",root_login="off",password="strong",)
