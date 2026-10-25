# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print()
print("\033[1;3;35m      ​====== Authentication Handler ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
secret_password = 7777
def crack_password(user_pin):
    if user_pin == secret_password:
        return True
    else:
        return False
while True:
    print("\033[1;93m[*]Pin Access Control Engine Starting...\033[0m\n")
    time.sleep(1)
    pin = int(input("Enter pin: "))
    time.sleep(1)
    if crack_password(pin) == True:
        print(f"\033[1;92m Access granted pin {pin}: correct\033[0m")
        time.sleep(1)
        break
    else:
        print("\033[1;91m>>> worng password Try Again\033[0m")
        time.sleep(1)
