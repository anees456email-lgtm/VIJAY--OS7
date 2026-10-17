# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
print("\033[1;3;35m  ​====== 4-DIGIT PIN CRACKER ======  ")
print("\033[1;96m" + "="*50)
print("\033[0m")
print()
def brute_force():
    while True:
        choice = input("press 1 to crack pin (press 2 to exit: ")
        if choice == "2":
            time.sleep(1)
            return "\033[1;93m>>> system shutdown...\033[0m"
#            time.sleep(1)
        target = int(input("Enter a 4_Digit Target Pin(1000,9999):"))
        for i in range(1000,10000):
            if i == target:
                time.sleep(1)
                return f"\033[1;3;4;32m>>> Target locked! {i} pin cracked\033[0m" 
#        else:
#           return "\033[1;95m[×] ERROR! ENTER ONLY 4 DIGIT\033[0m"
pin = brute_force()
print(pin)
time.sleep(1)
