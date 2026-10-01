# this script does not target any real systems and was created solely for educational purposes.
import time
print ("======================================")
print ("\033[1;3;35m Dummy SSH Brute-Force Simulator Loop Control\033[0m")
print ("======================================")
print()
secret_pin = "hunter777"
attempts = 1
while attempts <= 5:
    pwd = input("Enter pin: ")
    if pwd == "hunter777":
        print (f"\033[1;3;4;32m[✓]  {pwd}: is Correct Access Granted [✓]\033[0m")
        break
    else:
        print (f"\033[1;91m[×]Access Denied[×] {attempts}/5 \033[0m")
        attempts += 1
        time.sleep(1)

else:
    print ("\033[1;93m[!]Aleart: Maximum  attempts reached system lock[!]\033[0m")
