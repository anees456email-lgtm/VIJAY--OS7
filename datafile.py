# this script does not target any real systems and was created solely for educational purposes.
import time
import os
print("\033[1;96m")
os.system("figlet -f slant 'Dummy Tool'")
print("\033[0m")
print("=" *60)
def safe(ip,target_port):
    for port in target_port:
        print(f"\033[1;92m>>> {ip}: port >>>  {port} \033[0m")
        time.sleep(1)
safe("127.0.0.1",[22,80,21,443,8080])
safe("8.8.8.8",[80,443,22,8080,21])
