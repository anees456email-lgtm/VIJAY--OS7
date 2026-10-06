# this script does not target any real systems and was created solely for educational purposes.
import time
import os
print("\033[1;95m")
os.system("figlet -f slant 'Safe Parameter'")
print("\033[0m")
def safe_target(ip_address):
    print(f"\033[1;92m[*]Pinging >>> {ip_address}\033[0m")
    time.sleep(1)
safe_target("127,0,0,1")
safe_target("10,11,12,13")
safe_target("22,12,23,14")
safe_target("16,12,32,12")
safe_target("72,88,77,86")

