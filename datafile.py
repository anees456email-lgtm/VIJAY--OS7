# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m      ===== ​Port_Scanner.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
target_ports = [21,22,80,443,3306,56,77,44,8080,70,45,576]
def port_scanner(*ports):
    print("\033[1;94m[+] Port_Scanner Engine Starting...\033[0m")
    time.sleep(1)
    print(f"\033[1;3;36m[/] Total Target_Ports: {len(target_ports)}\033[0m")
    time.sleep(1)
    for port in ports:
        if port == 80:
            print(f"\033[1;3;32m>>> Port {port}:HTTP\033[0m")
            time.sleep(1)
        elif port == 8080:
            return f"\033[1;3;31m=> Port {port}: is closed\033[0m"
        else:
            print(f"\033[1;3;44m>> Port {port}: Normal Port\033[0m")
            time.sleep(1)
result = port_scanner(*target_ports)
print(result)
time.sleep(1)
