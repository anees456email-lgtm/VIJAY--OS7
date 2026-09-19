print ("==============================")
print ("\033[1;96m  menu choices \033[0m")
print ("==============================")
print()
while True:
    choice = input("Enter Choice: ")
    if choice == "1":
        print (f"\033[1;4;32m[✓] choice {choice}: system status:ONLINE[✓]\033[0m")
    elif choice == "2":
        print (f"\033[1;4;32m[✓] choice {choice}:  security scan:COMPLETE [✓]\033[0m")
    elif choice == "3":
        confirm = input("confirm reset? (yes/no/exit): ")
        if confirm == "yes":
            print (f"\033[1;3;33m[✓] confirm {confirm}: session reset [✓]\033[0m")
        elif confirm == "no":
            print (f"\033[1;3;34m[!] confirm {confirm}: Reset cancelled[!]\033[0m")
        elif confirm == "exit":
            print (f"\033[1;3;4;35m[~] confirm {confirm}: Console closed[~]\033[0m")
            break
    else:
        print ("\033[1;91m[×]Invalid confimation[×]\033[0m")
