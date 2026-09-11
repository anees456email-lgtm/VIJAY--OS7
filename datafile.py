password = 7676
attempts = 0
while attempts < 3:
    i = int(input("entar password: "))
    if i == password:
        print (f"\033[1;3;32m Access granted {i} welcome bs\033[0m")
        break
    else:
        print (f"\033[1;91m Access decline invlide user {attempts+1}:attempts left\033[0m")
        attempts += 1
