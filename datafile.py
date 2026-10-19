# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
print()
print("\033[1;3;35m  ​====== DUMMY PORT HUNTER V1  ======  ")
print("\033[0m")
print("\033[1;96m" + "="*50)
print("\033[0m")
print()
def check_port(ip,target_port):
    while True:
        choice = int(input("Enter choice 1 start, (Enter 2 exit: "))
        if choice == 1:
            print("\033[1;93m>>> program start...\033[0m")
            time.sleep(1)
        elif choice == 2:
            print("\033[1;91m>>> program ending...\033[0m")
            time.sleep(1)
            break
        for single_ip in ip:
            print(f"\033[1;95m>>> {single_ip}\033[0m")
            time.sleep(1)
            for port in target_port:
                if port == 443:
                    print(f"\033[1;92m>>> port {port} is secure\033[0m")
                    time.sleep(1)
                elif port == 80:
                    print(f"\033[1;94m>>> port {port} not secure port\033[0m")
                    time.sleep(1)
                else:
                    print (f"\033[1;96m>>  port {port} normal port\033[0m")
                    time.sleep(1)
#        elif choice == "2":
#           return "\033[1;93m>>> program ending...\033[0m"
#result = check_port("ip","target_port")
#print(result)
check_port(["127,0,0,1","8,8,8,8"],[80,22,443,21,8080])

