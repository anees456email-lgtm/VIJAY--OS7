# "Username: bilal, Password: 1234 - ye demo login hai"
# This is for learning purposes only. No real passwords have been used in this nor has any attempt been made to try it on any real system.
print("\033[1;31m")
print("""
╔══════════════════════════════════════╗
║                                      ║
║          ☠  BILAL TERMINAL  ☠       ║
║                                      ║
║        ⚠  SECURE SYSTEM  ⚠          ║
║                                      ║
╚══════════════════════════════════════╝
""")
print("\033[1;32m        >>> SYSTEM READY <<<\033[0m")
print()
correct_username = "bilal"
user_pass = 1234
attempts = 1
while attempts <= 3:
    input_username = input("Entar name: ")
    user_pass = int(input("Entar pass: "))

    if input_username == correct_username:
        print (f"\033[1;3;32m username found {input_username} welcome\033[0m")

        if user_pass == 1234:
            print (f"\033[1;3;32m {user_pass} correct password login Successful\033[0m")
            break
        else:
            print (f"\033[1;3;31m Wrong password attempts {attempts}/3 \033[0m")
            attempts += 1
    else:
        print (f"\033[1;3;31m user not found attempts {attempts}/3 \033[0m")
        attempts += 1
print()
if attempts == 4:
    print ("\033[1;3;33m [!] Account Locked [!] \033[0m")

