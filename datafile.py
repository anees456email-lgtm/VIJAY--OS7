# this script does not target any real systems and was created solely for educational purposes.
import time
import os
# os.system("clear")
print("\033[1;96m" + "="*50)
print("\033[1;3;35m    Dummy ​Secure Login Simulator ")
print("\033[1;94m" + "="*50)
print("\033[0m")
print()
def system_login():
    secret_pin = "7788"
    attempts = 0
    while attempts < 3:
        guess = input("Enter 4-digit PIN: ")
        attempts += 1
        if guess == secret_pin:
            return "\033[1;3;32m>>> Access Granted\033[0m"
        else:
            print(f"\033[1;91m>>> Wrong Pin! try again {attempts}/3\033[0m")
            time.sleep(1)
    return "\033[1;91m>>> Account Locked\033[0m"
final_status = system_login()
# print(f"\033[1;3;32m>>> {final_status}\033[0m")
print(final_status)
