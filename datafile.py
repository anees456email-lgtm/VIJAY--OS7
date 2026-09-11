while True:
    user = input("Entar Name: ")
    if user == "Vijay":
        print (f"\033[1;3;32m {user} Access Granted\033[0m")
        break
    else:
        print ("\033[1;91m[×] Invalid user [×]\033[0m")

