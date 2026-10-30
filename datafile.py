# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[1;94m" + "="*50)
time.sleep(1)
print()
print("\033[1;3;35m    ====== Threat-Level-Analyzer.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[1;94m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def calculate_risk(failed_attempts):
    return failed_attempts * 5
def add_device_bonus(risk_score):
    if risk_score >= 20:
        return risk_score + 10
    else:
        return risk_score
def classify_event(score):
    if score >= 50:
        return "High"
    elif score >= 25:
        return "Medium"
    else:
        return "Low"
def run_analyzer(failed_attempts):
    risk = calculate_risk(failed_attempts)
    status = add_device_bonus(risk)
    total = classify_event(status)
    return total
final = run_analyzer(6)
print(f"\033[1;3;32m {final}\033[0m")
time.sleep(1)

def calculate_score(points):
    return points * 3
def add_bonus(score):
    if score >= 20:
        return score + 10
    else:
        return score
def double_score(score):
    return score * 2
def run_player(points):
   # basic_score = calculate_score(points)
   # bonus_score = add_bonus(basic_score)
   # final_score = double_score(bonus_score)
   # return final_score
#result = run_player(8)
#print(f"\033[1;92m>>> {result}\033[0m")
    final = double_score(add_bonus(calculate_score(points)))
    return final
result = run_player(8)
print(f"\033[1;3;32m>>> {result}\033[0m")





