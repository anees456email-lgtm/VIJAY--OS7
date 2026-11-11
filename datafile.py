# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m      ===== ​Termux Net-Drop Scanner  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def scan_network(target_ip,*pings):
    print("\033[1;3;35m[+] Network Ping Analyzer Started...\033[0m\n")
    time.sleep(1)
    print(f"\033[1;91m Target Locked: {target_ip}\033[0m")
    time.sleep(1)
    print(f"\033[1;3;33m[*] Total Packet Send: {len(pings)}\033[0m")
    time.sleep(1)
    print(f"\033[1;3;33m[~] Min ping (Fastest): {min(pings)} ms\033[0m")
    time.sleep(1)
    print(f"\033[1;3;33m[!] Max ping (Lag): {max(pings)} ms\033[0m")
    time.sleep(1)
   # print(f"\033[1;3;33m[~] Min ping (Fastest): {min(pings)} ms\033[0m")
   # time.sleep(1)
    dropped_packets = 0
    for ping in pings:
        if ping == 20:
            print(f"\033[1;3;32m[✓] Ping {ping}: Fastest ms\033[0m")
            time.sleep(1)
        elif ping == 300:
            print(f"\033[1;3;31m-> Max  Ping {ping}: ms (Lag)\033[0m")
            time.sleep(1)
            dropped_packets += 1
            continue
        elif ping == 999:
            print(f"\033[1;3;41m[*] High Ping {ping}: Server offline Packet Dropped\033[0m")
            time.sleep(1)
            dropped_packets += 1
            break
        elif ping > 300:
            print(f"\033[1;3;41m--> High Latency Ping <{ping}>\033[0m")
            time.sleep(1)
        else:
            print(f"\033[1;3;34m[+] Normal Ping: {ping} ms\033[0m")
            time.sleep(1)
    print(f"\033[1;3;36m Total Packets Dropped {dropped_packets}\033[0m")
    time.sleep(1)
scan_network("127.0.0.1",45,80,350,300,40,55,20,999)
