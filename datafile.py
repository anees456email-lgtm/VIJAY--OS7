# this script does not target any real systems and was created solely for educational purposes.
import time
print ("======================================")
print ("\033[1;3;36m Mini DirBuster - Web Directory Scanner\033[0m")
print ("======================================")
print()
payloads = ["/login","/admin","/db_backup","/config.php","/users"]
while True:
    ip = input("Enter target ip:(exit to 0): ")
    if ip == "0":
        print ("\033[1;93m[~]Scanner Stooped[~]\033[0m")
        break
    for i in payloads:
        if i == "/admin":
            print (f"\033[1;91m[?] {i} Forbidden! Skipping...\033[0m")
            continue
        elif i == "/config.php":
            print (f"\033[1;3;4;32m[*]BOOM! {i} Sensitive File Found!\033[0m")
            break
        else:
            print (f"\033[1;94m[+]Scanning:{ip} {i} \033[0m")
            time.sleep(1)
