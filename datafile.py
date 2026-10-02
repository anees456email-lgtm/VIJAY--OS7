# this script does not target any real systems and was created solely for educational purposes.
import time
print ("--------------------------------------")
print ("======================================")
print ("\033[1;3;34m Dummy Web Directory Brute-Forcer While + For Combo\033[0m")
print ("======================================")
print ("--------------------------------------")
print()
folders = ["admin","login","config","uploads","backup"]
while True:
    user_input = input("Enter target website: (exit to 0: ")
    if user_input == "0":
        print (f"\033[1;93m[~] Scanner Shutting Down [~]\033[0m")
        break
    for i in folders:
        print (f"\033[1;3;32m[*] Cheking {user_input} {i}\033[0m")
        time.sleep(1)

