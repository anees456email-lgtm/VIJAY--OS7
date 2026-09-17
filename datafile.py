# This is solely for educational purposes; no real-world assets have been used, nor have any real systems been targeted.
import time

C = "\033[96m"
G = "\033[92m"
R = "\033[91m"
Y = "\033[93m"
W = "\033[0m"

banner = f"""
{C}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
{C}█ {G} [+] ADVANCED PORT SCANNER v1.0       {C} █
{C}█ {Y} [!] WARNING: HONEYPOT DETECTION ON   {C} █
{C}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{W}
"""
print(banner)
time.sleep(1)


port = 1
while port <= 100:
    if port == 22:
        print (f"\033[1;3;4;32m port {port}: ssh is open\033[0m")
    elif port == 80:
        print (f"\033[1;3;4;32m port {port}: http is open\033[0m")
    elif port == 99:
        print (f"\033[1;91m[!] port {port}: HONEYPOT DETECTED! DISCONNECTING IMMEDIATELY[!]\033[0m")
        break
    port += 1
    time.sleep(0.01)
