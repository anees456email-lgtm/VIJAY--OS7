# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
print("\033[1;3;35m  ====== DUMMY SYSTEM BYPASS SIMULATOR ======  ")
print("\033[1;96m" + "="*50)
print("\033[0m")
print()
import time
secret_pin = "hunter77"
def bypass_system():
    attempts = 0
    while attempts < 3:
        guess = input("Enter Pin: ")
        attempts += 1
        time.sleep(1)
        if guess == secret_pin:
            return f"\033[1;92m>>> {guess}: password correct system access granted\033[0"
        else:
            print (f"\033[1;91m>>> worng pin {attempts}/3\033[0m")
    return "\033[1;91m>>> SYSTEM LOCKED\033[0m"
result = bypass_system()
print(result)

