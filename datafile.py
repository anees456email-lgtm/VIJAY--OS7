# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
print()
print("\033[1;3;35m  ​====== DUMMY TraceBreaker Engine ======  ")
print("\033[0m")
print("\033[1;96m" + "="*50)
print("\033[0m")
print()
threat_level = 0
def scan_network(port_list):
    global threat_level
    scan_count = 0
    for port in port_list:
        scan_count += 1
        if scan_count == 4:
            print("\033[1;91m>> Limit reached\033[0m")
            break
        elif port == 80:
            print(f"\033[1;93m>>> port {port} Skipping...\033[0m")
            time.sleep(1)
            continue
          #  time.sleep(1)
        elif port == 4444:
            threat_level += 1
            print(f"\033[1;91m>>> Malware {port} port Detected\033[0m")
        #    threat_level += 1
            time.sleep(1)
            break
scan_network([21,80,22,443,4444,8080])
print(f"\033[1;93m>>> Final threat_level {threat_level}\033[0m")


