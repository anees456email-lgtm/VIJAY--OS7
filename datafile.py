# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
print("\033[1;3;35m          Dummy ​Port Scanner Simulator (Math Logic) ")
print("\033[1;94m" + "="*50)
print("\033[0m")
print()
def scan_port(start_port,end_port):
    open_ports = 0
    for port in range(start_port,end_port):
        if port % 5 == 0:
            open_ports += 1
    return open_ports
result = scan_port(10,50)
print(f"\033[1;92m>>>  {result}  open port\033[0m")
time.sleep(1)
