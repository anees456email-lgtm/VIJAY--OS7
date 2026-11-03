# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[1;94m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m         ====== DUMMY PORT SCANNER ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;94m" + "-"*50)
time.sleep(1)
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
import time
def scan_port(*port):
    for p in port:
        if p == 8080:
#            continue
            print("\033[1;41m--> honeypot port skipping...\033[0m")
            time.sleep(1)
#            break
            continue
        print(f"\033[1;93m>>> Scanning port {p}\033[0m")
        time.sleep(1)
scan_port(77,80,8080,21,55,22)
