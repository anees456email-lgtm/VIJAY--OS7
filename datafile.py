# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m         ===== ​Traffic Anomaly.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
leaked_chunks_kb = [12,45,10,800,55,2500,30]
def shadow_leak(*leaked_data):
    total_chunks = len(leaked_data)
    print(f"\033[1;3;36m[+] Total Chunks:  {total_chunks}\033[0m")
    time.sleep(1)
    total_leaked = max(leaked_data)
    print(f"\033[1;3;36m[/] Total Max Data:  {total_leaked}\033[0m")
    time.sleep(1)
    min_total = min(leaked_data)
    print(f"\033[1;3;36m[-] Min Data:  {min_total}\033[0m")
    time.sleep(1)
    total_leaked_data = sum(leaked_data)
    print(f"\033[1;3;36m[*] Total Data:  {total_leaked_data}\033[0m")
    time.sleep(1)
    ave_leak = total_leaked_data/total_chunks
    print(f"\033[1;3;34m--> Average: {ave_leak}\033[0m")
    time.sleep(1)
    if total_leaked_data > 2000 or total_leaked > 1500:
        print("\033[1;3;31m>>> CRITICAL! Massive Data Breach Detected!\033[0m")
        time.sleep(1)
    else:
        print("\033[1;91m[✓] Normal Traffic\033[0m")
        time.sleep(1)
shadow_leak(*leaked_chunks_kb)
