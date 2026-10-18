# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
print()
print("\033[1;3;35m  ​====== Dummy Botnet Army Simulator ======  ")
print("\033[0m")
print("\033[1;96m" + "="*50)
print("\033[0m")
print()
total_bots = 0
def add_bot():
    global total_bots
    total_bots = total_bots + 1
    target = "unknwon_ip"
    print(f"\033[1;91m>>> target infected local system syatem name: {target} ")
    time.sleep(1)
for i in range(3):
    add_bot()
#add_bot()
#add_bot()
#add_bot()
print("\033[1;93m total bots in my army:", total_bots)
