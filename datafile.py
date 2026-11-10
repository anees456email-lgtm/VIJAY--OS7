# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m      ===== ​Core-Port Engine  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
#attempts = 0
def scan_port(target_ip,*ports):
    print("\033[1;3;33m[+] Program Engine Starting...\033[0m\n")
    time.sleep(1)
   # global attempts
   # attempts = 1
    for port in ports:
#        while attempts <= 3:
#            print(f"\033[1;3;32m>>> Trying: {port}\033[0m")
#            attempts += 1
#            time.sleep(1)
            if port == 0:
                print(f"\033[1;3;37m  Invalid Port: {port}\033[0m")
                time.sleep(1)
                continue
            elif port == 999:
                print(f"\033[1;3;31m[*] Emergency Port: {port}\033[0m")
                time.sleep(1)
                break
            attempts = 1
            while attempts <= 3:
                print(f"\033[1;3;36m {target_ip}:  Trying Port -> {port}: attempts: {attempts} \033[0m")
                attempts += 1
                time.sleep(1)
                if attempts == 3:
                    print(f"\033[1;3;4;32m>>> Success Port {port} Open\033[0m")
                    time.sleep(1)
                    break
#                else:
#                    print (f"\033[1;3;36m-> Normal Port {port}\033[0m")
#                    time.sleep(1)
scan_port("127.0.0.1",21,22,34,76,80,0,8080,90,81,999,43,29)
print("\033[1;3;35m" + "="*50)
time.sleep(1)
