# No attempt has been made here to crack actual ID passwords, nor has this been tested on a real system; instead, a publicly available text file is used. This Python script demonstrates how a `for` loop handles such a large text file.

file = open("rockyou.txt","r")
count = 1
for i in file:
    print ("\033[1;3;33m Checking: " + i)
    if i == "i love you\n":
        print (f"\033[1;3;4;32m {i} password found {count}\033[0m")
        break
    count += 1

