# this script does not target any real systems and was created solely for educational purposes.
import time
import os
os.system("clear")
print("\033[1;96m" + "="*50)
print("\033[1;3;35m    Dummy ​port_scanner.py ")
print("\033[1;96m" + "="*50)
print("\033[0m")
print()
def check_port(port_no):
    if port_no == 80:
        return "open"
    elif port_no == 22:
        return "Closed"
    else:
        return "Filtered"
terget = int(input("Enter port to scan: "))
port_status = check_port(terget)
if port_status == "open":
    print(f"\033[1;91m>>> port  80 {port_status} Target is Vulnerable\033[0m")
elif port_status == "Closed":
    print(f"\033[1;92m>>> port 22  {port_status} Target is Secure\033[0m")
else:
    print(f"\033[1;93m>>> {port_status} port is Hidden\033[0m")
