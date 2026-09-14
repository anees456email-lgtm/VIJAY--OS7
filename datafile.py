Y="\033[93m";R="\033[91m";B="\033[1m";W="\033[0m"
print(f"""{B}{Y}
 ╔══════════════════════════════╗
 ║ {R}⚠️  Power of while ⚠️{Y}  ║
 ║ {W}ACCESS DENIED = TRY HARDER{Y}  ║
 ╚══════════════════════════════╝{W}
""")
print()
while True:
    user_input = input("Enter password: ")
    if user_input == "bs313":
        print (f"\033[1;3;4;32m[✓]Access granted {user_input}: correct password\033[0m")
        break
    else:
        print ("\033[1;31m[×]wrong password access decline[×]\033[0m")
