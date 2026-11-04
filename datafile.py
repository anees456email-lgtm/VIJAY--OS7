# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m     ====== Dummy  Anti_Kill-Switch ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def Data_Exfiltration(target_folder,*file_size):
    print("\033[1;93m[+] Program starting...\033[0m")
    time.sleep(1)
    for p in file_size:
        if p > 500:
#            continue
            print(f"\033[1;3;4;32m--> Firewall Aleart high file: {p}\033[0m")
            time.sleep(1)
            continue
        elif p == 0:
#            print(f"\033[1;41m corrupt/trap file: {p}\033[0m")
#            time.sleep(1)
            return f"\033[1;41m corrupt/trap file: {p}\033[0m"
#            break
        else:
            print(f"\033[1;3;42m valid file {p}\033[0m")
            time.sleep(1)
#final_result = Data_Exfiltration("system32") # (22,24,89,700,77,0,66)
#print(final_result)
#Data_Exfiltration("system32",10,50,90,22,25,89,27,77,700,1,22,44,110,0,9)
result = Data_Exfiltration("system32",22,24,89,700,77,0,66,80)
print(result)
time.sleep(1)
