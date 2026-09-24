# This does not target a real system in any way; rather, it is a straightforward and well-structured Python script created solely for educational purposes.
import time
print ("======================================")
print ("\033[1;3;35m FAKE PORT SCANNER\033[0m")
print ("--------------------------------------")
print()
ports = [22,80,443,445,8080]
for port in ports:
    if port == 445:
        print (f"\033[1;3;4;31m[!] Warning: port {port}:  is open\033[0m")
    else:
        print (f"\033[1;92m[✓] {port} port scanned status secure [✓]\033[0m")
        time.sleep(1)
