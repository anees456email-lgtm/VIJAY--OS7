# No real passwords have been used here, nor has it been tested on any real system; this is just a simple Python script created solely for learning purposes.
import time
print ("====================================")
print ("\033[1;3;36m The Fake SSH Brute-Forcer\033[0m")
print ("====================================")
print()
target_password = "admin"
password_list = ["root","7766","password123","admin@123","admin"]
for p in password_list:
    if p == target_password:
        print (f"\033[1;3;4;32m[✓]password cracked :{p}:\033[0m")
        break
    else:
        print (f"\033[1;91m[×]Invild password {p}:[×]\033[0m")
        time.sleep(1)
