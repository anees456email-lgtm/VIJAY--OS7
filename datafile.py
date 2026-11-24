# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[1;96m" + "—"*50)
time.sleep(1)
print()
print("\033[1;3;36m          ===== ​target_audit.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[0m")
print()
def audit_target(**info):
    print()
    time.sleep(1)
    print("\033[1;3;35m AUDIT INFO...\033[0m")
    time.sleep(1)
    total_fields = len(info)
    print(f"\033[1;3;34m Total Fields: {total_fields}\033[0m")
    time.sleep(1)
    print("\033[1;96m" + "—" *50 + "\033[0m")
    time.sleep(1)
    if total_fields == 0:
        print("\033[1;3;31m No Data Found\033[0m")
        time.sleep(1)
        return
    print()
    if total_fields <= 2:
        print("\033[1;3;33m Scan level basic\033[0m")
        time.sleep(1)
    else:
        print("\033[1;3;32m Scan Level Detailed\033[0m")
        time.sleep(1)
    round_no = 0
    for key,value in info.items():
        round_no += 1
        print(f"\033[1;3;36m Round {round_no} --> {key}: {value}\033[0m")
        time.sleep(1)
    target_ip = info.get("ip")
    if target_ip is None:
        print("\033[1;3;41m Alert: Target Ip Missing!\033[0m")
        time.sleep(1)
audit_target()
audit_target(ip="127.0.0.1",port=80)
audit_target(host_name="web-srv-01",port=443,ssl="Active",server="Apache")
