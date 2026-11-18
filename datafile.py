# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m          ===== Flag_Scanner.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def ctf_scan(blue,*flags,Difficulty="Beginner"):
    print(f"\033[1;3;34m Room name: {blue}\033[0m")
    time.sleep(1)
    print(f"\033[1;3;34m Flags packed: {flags}\033[0m")
    time.sleep(1)
    print(f"\033[1;3;34m Difficulty Mode: {Difficulty}\033[0m")
    time.sleep(1)
    count = len(flags)
    print(f"\033[1;3;34m Total Flags: {count}\033[0m")
    time.sleep(1)
    for flag in flags:
        if flag == "root_hash":
            print(f"\033[1;3;32m--> Bingo Flag [{flag}]: Found\033[0m")
            time.sleep(1)
        else:
            print(f"\033[1;3;33m>> Normal Flag: {flag}\033[0m")
            time.sleep(1)
        print("\033[1;90m" + "="*50)
        time.sleep(1)
ctf_scan("blue","flag1.txt","root_hash","aaa_hacked")
