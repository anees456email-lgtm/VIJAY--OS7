# this script does not target any real systems and was created solely for educational purposes.
import time
print ("======================================")
print ("\033[1;3;35m Brute-Force PIN Cracker Simulator\033[0m")
print ("======================================")
print()
target_pin = 8426
for i in range(1,9001):
    print (f"\033[1;93m [*] Trying pin: {i}\033[0m")
    if i == target_pin:
        print (f"\033[1;3;4;32m[✓]pin cracked! the pin is {i}\033[0m")
        break
        time.sleep(1)
