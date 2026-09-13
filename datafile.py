# Only education purpose
import time
GREEN = "\033[92m"; RED = "\033[91m"; YELLOW = "\033[93m"; RESET = "\033[0m"
print(f"{RED}╔══[ INTRUDER ALERT SYSTEM ]══╗{RESET}")
print(f"{YELLOW}║ {GREEN}BILAL TERMINAL - DAY 8{RESET}{YELLOW}      ║{RESET}")
print(f"{YELLOW}║ {RED}MODE: SCAN // BLOCK{RESET}{YELLOW}          ║{RESET}")
print(f"{RED}╚════════════════════════════╝{RESET}")
print()
users = ["bilal","admin","vijay","hacker","guest"]
for name in users:
    if name == "bilal" or name == "vijay":
        print (f"\033[1;3;32m Access granted: {name} is trusted\033[0m")
    else:
        print (f"\033[1;3;31m[×]Intruder alert: {name} is blocked\033[0m") 
        time.sleep(1)
