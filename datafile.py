# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m         ===== ​Tuple_Striker_py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def stealth_scan(target_ip,*ports):
    if not ports:
        print(f"\033[1;3;91m Target {target_ip} highly secure no ports open\033[0m")
        time.sleep(1)
    for i in ports:
        print(f"\033[1;3;32m port {i} is open on --> {target_ip}\033[0m")
        time.sleep(1)
stealth_scan("192.168.1.10",22,80,443)
print("\033[1;96m" + "="*50)
time.sleep(1)
result = ("10.0.0.5",21,23,3306,8080)
stealth_scan(*result)
