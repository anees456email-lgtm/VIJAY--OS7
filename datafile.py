# No actual passwords have been used here; this is solely for learning purposes, and no attempt has been made to test it on a real system.
import time

R = "\033[1;31m"
C = "\033[1;36m"
Y = "\033[1;33m"
W = "\033[0m"


banner = f"""{R}
     _  _   _   ___ _  _____ ___ 
    | || | /_\\ / __| |/ / __| _ \\
    | __ |/ _ \\ (__| ' <| _||   /
    |_||_/_/ \\_\\___|_|\\_\\___|_|_\\
{C}
╔══════════════════════════════════╗
║ {Y}   {C}
║ {Y}[!] STATUS: SYSTEM LOCKED        {C}║
╚══════════════════════════════════╝{W}
"""

print(banner)
time.sleep(1)
print(f"{Y}[*] Initiating Brute-Force Attack...{W}\n")
print()
attempts = 1
secret_pin = 7744
while attempts <= 3:
    user_pass = int(input("Entar Password: "))
    if user_pass == secret_pin:
        print (f"\033[1;3;4;32m[✓]Access Granted! {user_pass}: Root shell open[✓]\033[0m")
        break
    else:
        print (f"\033[1;91m[×]Intrusion Detected! worng pin {attempts}/3 [×]\033[0m")
        attempts += 1
        time.sleep(1)
