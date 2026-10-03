# this script does not target any real systems and was created solely for educational purposes.
import time
print ("--------------------------------------")
print ("======================================")
print ("\033[1;3;35m Dummy Security Console Simulator\033[0m")
print ("======================================")
print ("--------------------------------------")
print()
secret_pin = 7288
attempts = 1
vpn_on = True
ip = "safe"
os_name = "Termux"
threat_detected = False
while attempts <= 3:
    pwd = int(input("Enter code: "))
    if pwd == 7288:
        print(f"\033[1;3;32m>>> {pwd}: is correct Access granted\033[0m")
        time.sleep(1)
        for checkpoint in range(1,4):
            if checkpoint == 1:
                print(f"\033[1;92m[+] {checkpoint} checkpoint: Network Secuirty Scan...[+]\033[0m")
                if vpn_on  == True and ip == "safe":
                    print("\033[1;93m[✓]Access Clear: VPN active ip is safe[✓]\033[0m")
                    time.sleep
                    continue
                else:
                    print("\033[1;91m[×]Security Breach[×]\033[0m")
            elif checkpoint == 2:
                print("\033[1;96m[~]Checkpoint 2 Device Authorization[~]\033[0m")
                if  os_name == "Termux" or os_name == "Kali":
                    print("\033[1;92m>>>Device Verified\033[0m")
                    time.sleep(1)
                    continue
                else:
                    print("\033[1;91m[!]Unknown Device[!]\033[0m")
            elif checkpoint == 3:
                if not threat_detected:
                    print("\033[1;3;4;32m>>> FINAL ACCESS GRANTED <<<\033[0m")
                    time.sleep(1)
                    break
        break
    else:
        print(f"\033[1;91m>>> Wrong pin Access decline {attempts}/3\033[0m") 
        attempts += 1
        time.sleep(1)

else:
    print("\033[1;3;4;31m>> All attempts over system blocked\033[0m")
    time.sleep(1)
