# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
print()
print("\033[1;3;35m  ​====== DUMMY Brute-Strike V1 ======  ")
print("\033[0m")
print("\033[1;96m" + "="*50)
print("\033[0m")
print()
import time
file = open ("rockyou.txt","r")
def creck_password():
    count = 1
    for i in file:
        print("\033[1;93m checking: " + i)
        time.sleep(0.05)
        if i == "00000000\n":
            print(f"\033[1;92m {i} password found count {count}\033[0m")
            time.sleep(1)
            break
        count += 1
creck_password()


wordlist = ["admin","password","2212","1612","admin123","boom","9090","guru"]
def crack_password():
    count = 1
    for i in wordlist:
        print("\033[1;93m>>> Cheking password " + i)
        time.sleep(1)
        if i == "9090":
            return f"\033[1;92m>>> {i} password found count {count}\033[0m"
            time.sleep(1)
        else:
            print(f"\033[1;91m password not found  {count}\033[0m")
        count += 1
result = crack_password()
print(result)
#crack_password()
