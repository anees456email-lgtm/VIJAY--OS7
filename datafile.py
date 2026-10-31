# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[1;94m" + "="*50)
time.sleep(1)
print()
print("\033[1;3;35m    ====== Brute-Breach Stealer  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def admin_pin():
    return 7778
def firewall_check(pin):
    for i in range(7770,7780):
        if i == pin:
            return "Bypassed"
        else:
            print(f"\033[1;91m Blocked {i}\033[0m")
            time.sleep(1)
def database_dump(status):
    if status == "Bypassed":
        print("\033[1;92m hacked database status Downloaded\033[0m")
        time.sleep(1)
    else:
        print("\033[1;91m Aleart Firewall Blocked your ip\033[0m")
        time.sleep(1)
result = admin_pin()
dump = firewall_check(result)
database = database_dump(dump)
##print(f"\033[1;92m {result}\033[0m")
##time.sleep(1)

def data_staler(battery):
   # battery = 100
    while battery > 0:
        print(f"\033[1;3;33m Downloading Data... battery {battery}%\033[0m\n")
        battery  -= 1
        time.sleep(0.05)
        if battery == 10:
            print(f"\033[1;3;32m>>> Aleart battery cirtril connection dropped:\nbattery {battery}%\033[0m")
            time.sleep(1)
            break
data_staler(20)
#data_staler(50)
#data_staler(100)
