# this script does not target any real systems and was created solely for educational purposes.
import time
import os

print("\033[1;96m" + "="*50)
print("\033[1;3;35m        Dummy Admin Login Checker")
print("="*50 + "\033[0m")
print()
def check_login(user,pwd):
    if user == "admin" and pwd == "toor123":
        return "[✓]Access granted welcome Admin[✓]"
    else:
        return "[×] Access Denied![×]"
result_1 = check_login("admin","toor123")
print(f"\033[1;3;32m>>>{result_1}\033[0m")
time.sleep(1)
