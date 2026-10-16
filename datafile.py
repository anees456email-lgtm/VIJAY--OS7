# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
print("\033[1;3;35m           ====== PYTHON BANK ATM ====== ")
print("\033[1;96m" + "="*50)
print("\033[0m")
print()
secret_pin = 1234
def login():
    attempts = 0
    while attempts < 3:
        user = int(input("Enter pin: "))
        time.sleep(1)
        attempts += 1
        if user == secret_pin:
            return True
        else:
            print(f"\033[1;91m>>> wrong pin attempts {attempts}/3\033[0m")
#    print(f"\033[1;91m worng pin {attempts}/3\033[0.")
#    return False
def withdraw_money():
    Balance = 5000
    amount = int(input("Enter amount: "))
    if amount > Balance:
        print("\033[1;91m>>> Insufficient Funds!\033[0m")
        time.sleep(1)
    else:
        new_Balance = Balance - amount
        print(f"\033[1;92m>>> Transation Successful! your new Balance {new_Balance}\033[0m")
        time.sleep(1)
    return
login_status = login()
if login_status == True:
    withdraw_money()
else:
    print("\033[1;93m>>> Too many wrong attempts card blocked\033[0m")

