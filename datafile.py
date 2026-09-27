# this script does not target any real systems and was created solely for educational purposes.
import time
print ("======================================")
print ("\033[1;3;34m Stealth Port Scanner Simulator\033[0m")
print ("======================================")
print()
print ("--------------------------------------")
print ("\033[1;3;35m[!] Target Locked. Initiating Stealth Port Scan...\033[0m")
print ("--------------------------------------")
print()
for port in range(8075,8085):
    if port == 8080:
        print (f"\033[1;3;4;32m[✓]BINGO: port {port}: is open[✓]\033[0m")
        break
    else:
        print (f"\033[1;91m[×]port {port} closed[×]\033[0m")
        time.sleep(1)

