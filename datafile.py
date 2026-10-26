# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print()
print("\033[1;3;35m      ​   ====== Path Discovery ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def check_path(path_name):
    "admin_panel"
    if path_name == "admin_panel":
        return True
    else:
        return False
wordlist = ["login","user","admin","dashbord","admin_panel"]
for path in wordlist:
    print("\033[1;93m>>> Trying path_name\033[0m")
    time.sleep(1)
    print()
    if check_path(path):
        print(f"\033[1;92m[✓] Success! path found {path}\033[0m")
        time.sleep(1)
    else:
        print("\033[1;91m[×] Wrong path_name [×]\033[0m")
        time.sleep(1)
