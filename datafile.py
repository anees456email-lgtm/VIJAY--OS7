# For learning purposes only
attempt = 1
while attempt <= 3:
    user_input = input("Enter current language: ")
    if user_input == "python":
        print (f"\033[1;3;32m[✓] {user_input} is correct[✓]\033[0m")
        break
    attempt += 1
