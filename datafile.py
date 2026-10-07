# this script does not target any real systems and was created solely for educational purposes.
import time
import os
print("\033[1;95m")
os.system("figlet -f slant 'Dummy Tool'")
print("\033[0m")
print("=" *60)
def login_attack(username,password):
    if username== "hunter07" and password == "1111":
        print(f"\033[1;92m >>> username {username}: >>> password {password} Access Granted\033[0m")
        time.sleep(1)
    else:
        print(f"\033[1;91m[×]wrong username {username}: password >>> {password} Access Decline\033[0m")
        time.sleep(1)
login_attack("admin123","7777")
login_attack("ak","1234")
login_attack("hunter007","4321")
login_attack("hunter07","1111")
login_attack("hunter","1122")
