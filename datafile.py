# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[1;96m" + "—"*50)
time.sleep(1)
print()
print("\033[1;3;36m          ===== ​​Firewall Audit.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[0m")
print()
def firewall_auditor(**firewall_rules):
    print("\033[1;3;33m Firewall Auditing Start...\033[0m")
    time.sleep(1)
    print()
    total_entries = len(firewall_rules)
    count = 0
    for service,rules in firewall_rules.items():
        print(f"\033[1;3;36m Checking Service >>> {service}\033[0m")
        time.sleep(1)
        if rules == "Block":
            print(f"\033[1;3;31m  {service} -> Blocked\033[0m")
            time.sleep(1)
            count += 1
        elif rules == "Allow":
            print(f"\033[1;3;32m Service: {rules}\033[0m")
            time.sleep(1)
        elif rules == "Ignore":
            print(f"\033[1;3;37m {service} >> is skipping\033[0m")
            time.sleep(1)
            continue
        elif rules == "Emergency_stop":
            print(f"\033[1;3;41m {rules}\n Audit Status Inturrupted\033[0m")
            time.sleep(1)
            break
        else:
            print("\033[1;3;33m REVREW REQUIRED\033[0m")
            time.sleep(1)
    print("\033[1;95m" + "—" *50 + "\033[0m")
    time.sleep(1)
    print(f"\033[1;3;35m Total Services: {total_entries}\033[0m")
    time.sleep(1)
    print(f"\033[1;3;36m Total Blocked Entries: {count}\033[0m")
    time.sleep(1)
    print(f"\033[1;3;36m Audit Status Complated\033[0m")
    time.sleep(1)
firewall_auditor(ssh="Block",HTTPS="Allow",ftp="peview",Dns="Block",Telnet="Ignore",Smtp="Allow",Emergency="Emergency_stop",port=22,os="Lenux")
