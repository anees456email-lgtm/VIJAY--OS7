# this script does not target any real systems and was created solely for educational purposes.
import time
print ("======================================")
print ("\033[1;3;36m Ghost Protocol - Server Bypass & Admin Terminal\033[0m")
print ("======================================")
print()
target_password = "root123"
attempts = 1
while attempts <= 3:
    user_input = input("Enter password: ")
    if user_input == "root123":
        print (f"\033[1;3;4;32m[✓]Access Granted!\n {user_input}: password correct\033[0m")
        break
    else:
        print (f"\033[1;91m[×]Access Denied {attempts}/3\033[0m")
        attempts += 1
        time.sleep(1)
else:
    print ("\033[1;93m[!]All 3 attempts is over system locked\033[0m")
ports = [21,22,80,443]
while True:
    pwd = input("Enter command (1: scan, 0: exit): ")
    if pwd == "1":
        print ("\033[1;3;33m[~] target scanning initiated...\033[0m")
        for i in ports:
                print (f"\033[1;94m[*]Scanning port: {i}")
    elif pwd == "0":
        print ("\033[1;95m[!]System Connection Closed[!]\033[0m")
        break
        time.sleep(1)


