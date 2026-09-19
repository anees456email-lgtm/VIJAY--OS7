print ("==============================")
print ("\033[1;96m Menu-based loops\033[0m")
print ("==============================")
print()
while True:
    choice = int(input("Enter Choice: "))
    if choice == 1:
        print (f"\033[1;4;32m[✓] choice {choice}:  System chek complete[✓]\033[0m")
    elif choice == 2:
        print (f"\033[1;4;32m[✓] choice {choice}:  Security chek complete[✓]\033[0m")
    elif choice == 3:
        print (f"\033[1;4;33m[~] choice {choice}:  System status active[~]\033[0m")
    elif choice == 4:
        print (f"\033[1;3;4;34m[*] choice {choice}:  System shutdown[*]\033[0m")
        break
    else:
        print ("\033[1;91m[×]Invlid choice[×]\033[0m")

