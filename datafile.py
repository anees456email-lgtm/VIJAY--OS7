# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "—"*50)
time.sleep(1)
print()
print("\033[1;3;36m          ===== Sendbox_Analyzer.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def sendbox_test(target_file,*behaviours,quarantine=True):
    print(f"\033[1;3;34m Scanning Target File: {target_file}\033[0m")
    time.sleep(1)
    total_count =len(behaviours)
    print(f"\033[1;3;34m File Behaviours count: {total_count}\033[0m")
    time.sleep(1)
    print(f"\033[1;3;34m Quarantine Status: {quarantine}\033[0m")
    time.sleep(1)
    print("\033[1;96m" + "_" *50 + "\033[0m")
    time.sleep(1)
    for behaviour in behaviours:
        if behaviour == "registry_change":
            print(f"\033[1;3;31m Behaviour [{behaviour}] CRITICAL! Alert Spyware Detected\033[0m")
            time.sleep(1)
        else:
            print(f"\033[1;3;33m Normal Behaviour:  {behaviour}\033[0m")
            time.sleep(1)
    print("\033[1;96m" + "_" *50 + "\033[0m")
    time.sleep(1)
sendbox_test("calculator_exe","calculator_open","registry_change","add_numbers","access","file_txt")
