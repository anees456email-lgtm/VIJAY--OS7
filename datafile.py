# This code does not use any real-world elements, nor does it target any real systems or servers; it is simply a basic Python script intended for learning purposes.
import time

C = "\033[96m"
G = "\033[92m"
R = "\033[91m"
Y = "\033[93m"
W = "\033[0m"

banner = f"""
{C}╔══════════════════════════════════════════╗
{C}║ {G} [+] SYSTEM LOGIN - SECURITY GATEWAY    {C} ║
{C}║ {Y} [!] WARNING: MAX 3 ATTEMPTS ALLOWED    {C} ║
{C}╚══════════════════════════════════════════╝{W}
"""
print(banner)
time.sleep(1)

attempts = 1
secret_password = "root"
while attempts <= 3:
    pwd = input("Enter password: ")
    if pwd == "root":
        print (f"\033[1;3;4;32m [*] password entered :{pwd}: is correct [*]\033[0m")
        break
    else:
        print (f"\033[1;3;91m[×]wrong password[×] {attempts}/3 attempts \033[0m")
        attempts += 1
        time.sleep(1)
else:
    print ("\033[1;3;33m [!]ACCOUNT LOCKED! TO MANY FAILED ATTEMPTS[!]\033[0m")
