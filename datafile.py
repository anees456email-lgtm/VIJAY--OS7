# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m      ===== ​Port_Shield_Tuple_Striker  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def secure_server(server_ip,*ports):
    print("\033[1;3;42m[+] Program Starting...\033[0m\n")
    time.sleep(1)
    for port in ports:
        if port == 443:
#            continue
            print(f"\033[1;3;31m[!] [Warning] port {port} Active Web Traffic. Cannot Block\033[0m")
            time.sleep(1)
            continue
        else:
            print(f"\033[1;3;32m {server_ip}: Secure Port -->  {port}: Successfully Blocked\033[0m")
            time.sleep(1)
secure_server("127.0.0.1",80,90,21,22,443,3890)
print("\033[1;93m" + "="*50)
time.sleep(1)
block_list = ("203.0.113.45",3890,5571,5577,241,443,80,8080)
secure_server(*block_list)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;3;36m No more ports\nProgram finished\033[0m")
time.sleep(1)
