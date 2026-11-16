# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m      ===== ​Score_Audit Analyzer.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
import time
def security_command_center(*scores):
    print("\033[1;3;30m[+] Score Analyzer Starting...\033[0m")
    time.sleep(1)
    total = sum(scores)
    count = len(scores)
    authorize = True
    print(f"\033[1;3;33m[=] Total Scores: {total}\033[0m")
    time.sleep(1)
    print(f"\033[1;3;33m[/] Combined Score: {count}\033[0m")
    time.sleep(1)
    round_no = 1
    while round_no <= 2:
        print(f"\033[1;3;35m[+] Audit Session Start {round_no}\033[0m")
        time.sleep(1)
        round_no += 1
        for score in scores:
            if (total >= 25 and count >= 4)or score >= 9:
                print("\033[1;3;41m--> Priorty Alert\033[0m")
                time.sleep(1)
            else:
                print("\033[1;3;33m[✓] Normal Priority\033[0m")
                time.sleep(1)
            if score >= 8:
                print(f"\033[1;3;31m>> Score {score}: High\033[0m")
                time.sleep(1)
            elif score >= 5:
                print(f"\033[1;3;33m>>> Score {score}: Medium\033[0m")
                time.sleep(1)
            else:
                print(f"\033[1;3;33m--> Score {score}: Low\033[0m")
                time.sleep(1)
        if not authorize:
            print("\033[1;3;35m[✓] Audit Blocked\033[0m")
            time.sleep(1)
        else:
            print("\033[1;92m>>> Audit Approved\033[0m")
            time.sleep(1)
        print("\033[1;3;45m| Audit Round Completed\033[0m")
        time.sleep(1)
    print("\033[1;96m" "="*50)
    time.sleep(1)
    print("\033[1;3;36m Audit Mission Complate\033[0m")
    time.sleep(1)
    print("\033[1;96m" "="*50)
    time.sleep(1)
    print(f"\033[1;3;36m Total Scores {total}\033[0m")
    time.sleep(1)
    print(f"\033[1;3;36m Combined Score: {count}\033[0m")
    time.sleep(1)
security_command_center(8,3,6,2,9)
