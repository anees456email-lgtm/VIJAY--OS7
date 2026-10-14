# this script does not target any real systems and was created solely for educational purposes.
import time
import os
os.system("clear")
print("\033[1;96m" + "="*50)
print("\033[1;3;35m    Dummy ​bruteforce_cracker.py ")
print("\033[1;94m" + "="*50)
print("\033[0m")
print()
import time
wordlist = ["admin","1122","password123","swag","2212","admin@123"]
def crack_password(target_password):
    attempt = 1
    for i in wordlist:
        print(f"\033[1;93m>>> Trying password {i}:  attempt {attempt}\033[0m")
       # attempt += 1
        time.sleep(1)
        if i == target_password:
            return f"\033[1;3;4;32m>>> Password Cracked: {i}: attempt {attempt}\033[0m"
        attempt += 1
    return "\033[1;91m>>> password not found! in wordlist\033[0m"
result = crack_password("admin@123")
print(result)
time.sleep(1)
