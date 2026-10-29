# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[1;94m" + "="*50)
time.sleep(1)
print()
print("\033[1;3;35m      ====== Relay-Pwn Script  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def find_target():
    return "192.168.1.105"
def scan_port(ip):
    print(f"\033[1;93m[!] Scanning target {ip}\033[0m \n")
    time.sleep(1)
    return 8080
def launch_atack(ip,port):
    print(f"\033[1;3;32m[+] Exploit Successfully [{ip}] on port > {port}\033[0m")
    time.sleep(1)
target = find_target()
open_port = scan_port(target)
launch_atack(target,open_port)






