# For learning purposes only
attempt = 1
while attempt <= 3:
    user_input = int(input("Enter pin: "))
    if user_input == 246:
        print (f"\033[1;3;32m[✓] {user_input} is correct[✓]\033[0m")
        break
    else:
        print (f"\033[1;91m[×]Wrong pin {attempt}/3 attempt\033[0m")
    attempt += 1
