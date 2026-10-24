# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print()
print("\033[1;3;35m      ​   ====== DUMMY BRUTE FORCE ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def try_login(guess):
#    guess = "root123"
    if guess == "root123":
        return True
    else:
        return False
def start_attack(wordlist):
    count = 1
    print("\033[1;94m starting burte force\033[0m\n")
    time.sleep(1)
    for password in wordlist:
        print(f"\033[1;93m>> trying passowrd {password}: count {count}\033[0m")
        count += 1
        time.sleep(1)
        result = try_login(password)
        if result == True:
            print(f"\033[1;3;32m>>> Password {password} Hacked {count - 1}\033[0m")
#            count -= 1
            time.sleep(1)
            break
           # count += 1
passwords = ["root","admin","2211","password","root123"]
start_attack(passwords)
