# this script does not target any real systems and was created solely for educational purposes.
import time
import os
print("\033[1;96m" + "="*50)
print("\033[1;3;36m             DUMMY SCANNER TOOL")
print("="*50 + "\033[0m")
print()
def safe(ip,target_port):
    while True:
        pwd = input("Enter command, (start to 1, (exit to 2 ")
        if pwd == "1":
            print("\033[1;94m>>> Program Starting...\033[0m")
            for port in target_port:
                if port == 80:
                    print(f"\033[1;93m>>> port {port} http\033[0m")
                elif port == 443:
                    print(f"\033[1;95m>>> port {port} https secure port\033[0m")
                else:
                    print(f"\033[1;92m>>> {ip}: port >>>  {port} normal port \033[0m")
                    time.sleep(1)
        elif pwd == "2":
            print("\033[1;91m Program Stooped Stopped...\033[0m")
            time.sleep(1)
            return
safe("127.0.0.1",[22,80,21,443,8080])

