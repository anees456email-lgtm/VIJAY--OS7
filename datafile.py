# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m      ===== ​Packet Analyzer.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def analyze_packet(*packets):
    print("\033[1;3;30m[+] Packet Analyzer Engine...\033[0m")
    time.sleep(1)
    print("\033[1;90m" + "="*50)
    time.sleep(1)
    print(f"\033[1;3;34m Total Packets Received: {len(packets)}\033[0m")
    time.sleep(1)
    print(f"\033[1;3;34m Max Packet Size: {max(packets)}\033[0m")
    time.sleep(1)
    print(f"\033[1;3;34m Total Packets Size: {sum(packets)}\033[0m")
    time.sleep(1)
    print("\033[0m")
    time.sleep(1)
    for packet in packets:
        if packet > 1000:
            print(f"\033[1;3;31m-> ALERT: Massive Packet {packet}: Detected! Blocking Traffic\033[0m")
            time.sleep(1)
        else:
            print(f"\033[1;3;32m>>> Normal Packet {packet}: Allowed\033[0m")
            time.sleep(1)
while True:
    print("\033[1;95m" +"="*50)
    time.sleep(1)
    print("\033[1;95m[1]:Scan Web Traffic| [2] Scan Database Traffic| Exit System:[0]\033[0m")
    time.sleep(1)
    choice = input("Enter option: ")
    if choice == "1":
        analyze_packet(120,50,1500,300)
    elif choice == "2":
        analyze_packet(2500,30,4000,80)
    elif choice == "0":
        print("\033[1;3;33m[-] System Shutting Down...\033[0m")
        time.sleep(1)
        break
    else:
        print("\033[1;3;31m!/] Invalid Command!\033[0m")
        time.sleep(1)
print("\033[1;93m" + "="*50)
time.sleep(1)
