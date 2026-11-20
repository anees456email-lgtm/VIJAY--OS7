# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[1;96m" + "—"*50)
time.sleep(1)
print()
print("\033[1;3;36m          ===== Bounty_Audit.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[1;96m" + "—"*50)
time.sleep(1)
print("\033[0m")
print()
def audit_report(program_name,*scores,alert_limit=7.0):
    if not scores:
        time.sleep(1)
        print("\033[1;3;32m No bugs found! system clean\033[0m")
        time.sleep(1)
        return
    print(f"\033[1;3;34m Score auditing starting: {program_name} {alert_limit}\033[0m")
    time.sleep(1)
    total_score = sum(scores)
    print(f"\033[1;3;37m Total score: {total_score}\033[0m")
    time.sleep(1)
    count_score = len(scores)
    print(f"\033[1;3;37m Total bugs count: {count_score}\033[0m")
    time.sleep(1)
    high_score = max(scores)
    print(f"\033[1;3;37m Highest risk score: {high_score}\033[0m")
    time.sleep(1)
    low_score = min(scores)
    print(f"\033[1;3;37m Lowest risk score: {low_score}\033[0m")
    time.sleep(1)
    average_risk_score = sum(scores) / count_score
    print(f"\033[1;3;37m Average risk score: {average_risk_score}\033[0m")
    time.sleep(1)
    print("\033[1;96m" + "-" *50 + "\033[0m")
    time.sleep(1)
    for score in scores:
        if score >= 9.0:
            print(f"\033[1;3;31m>> Critical score: {score}\033[0m")
            time.sleep(1)
        elif score >= alert_limit:
            print(f"\033[1;3;33m--> High score: {score}\033[0m")
            time.sleep(1)
        else:
            print(f"\033[1;3;32m Medium score: {score}\033[0m")
            time.sleep(1)
    print("\033[1;96m" + "-" *50 + "\033[0m")
    time.sleep(1)
score_list = [5,2,7,4,9,5,3]
audit_report("Cloud_core",*score_list)
