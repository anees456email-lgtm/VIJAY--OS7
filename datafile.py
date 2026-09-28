# this script does not target any real systems and was created solely for educational purposes.
import time
print ("======================================")
print ("\033[1;3;36m Mini Cyber Firewall Simulator\033[0m")
print ("======================================")
print()
system_health = 100
while True:
    user_input = input("Enter Network Traffic (1: safe, 2: Malware, 3: DDos,0: Exit: ")
    if user_input == "1":
        print (f"\033[1;3;4;32m[✓] {user_input}: Safe Data Allowed[✓]\033[0m")
        continue
    elif user_input == "2":
        print (f"\033[1;93m[!] {user_input}: Malware Blocked Health Drop[!]\033[0m")
        system_health -= 20

        if system_health <= 0:
            print  ("\033[1;91m[~]System Crashed[~]\033[0m")
            break
    elif user_input == "3":
        print (f"\033[1;91m[!!] {user_input}: DDOS ATTACK! SYSTEM LOCKDOWN\033[0m")
        break
    elif user_input == "0":
        print (f"\033[1;35m[*]Firewall Going Offline...\033[0m")
        break
    else:
        print ("\033[1;96m[?]Unknwon traffic![?]\033[0m")
    print (f"\033[1;94m[-]Current System Health: {system_health}%\033[0m")
