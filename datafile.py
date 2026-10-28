# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print()
print("\033[1;3;35m      ====== Phantom_Fuzzer.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def target_api(pin):
    if pin == 1337:
        return True
    else:
        return False
for i in range(1330,1340):
    if target_api(i):
        print(f"\033[1;3;32m [✓] Firewall Baypassed! Pin {i}\033[0m")
        time.sleep(0.05)
        break
    else:
        print(f"\033[1;91m>>>  Api Hit Falied! Pin {i}\033[0m")
        time.sleep(0.05)

attempts = 0
def hit_target(pin):
    if pin % 5 == 0:
        return "Blocked"
    elif pin == 1024:
        return "Hacked"
    else:
        return "Failed"
def start_engine():
    print("\033[1;94m[~] Program Starting...\033[0m")
    time.sleep(1)
    for i in range(1021,1031):
        global attempts
        attempts += 1
        result = hit_target(i)
        if result == "Blocked":
            print(f"\033[1;92m>>> Firewall Aleart Pin! {i} Blocked\033[0m")
            time.sleep(1)
            continue
        elif result == "Hacked":
            print(f"\033[1;93m System cracked in attempts {attempts}:  pin is  <{
i}>\033[0m")
            time.sleep(1)
            break
        else:
            print(f"\033[1;91m wrong Pin {i}\033[0m")
            time.sleep(1)
start_engine()








