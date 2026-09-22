# No real passwords have been used here, nor has it been tested on any real system; this is just a simple Python script created solely for learning purposes.
import time
print ("====================================")
print ("\033[1;3;36m The 3-Strike Vault\033[0m")
print ("====================================")
print()
secret_password = "password123"
count = 1
while count <= 3:
    user_input = input("Enter password: ")
    if user_input == secret_password:
        print (f"\033[1;3;4;32m[✓] {user_input}: Access granted [✓]\033[0m")
        break
    else:
        print (f"\033[1;91m[×]Access Decline[×] {count}/3 count \033[0m")
        count += 1
        time.sleep(1)
