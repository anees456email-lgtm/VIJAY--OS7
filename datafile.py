# This is just a simple Python script to learn.
print ("==============================")
print ("\033[1;3;4;36m Modulo + if elif + while\033[0m")
print ("===============================")
print()
attempts = 1
while attempts <= 3:
    code = int(input("Enter valid code: "))
    if code % 5 == 0 and code % 8 == 0:
        print ("\033[1;92m[✓]Super admin! access[✓]\033[0m")
    elif code % 5 == 0:
        print ("\033[1;93m[~]Normal user! access[~]\033[0m")
    else:
        print (f"\033[1;91m[×]Access Decline[×] {attempts}/3 \033[0m")
        attempts += 1
