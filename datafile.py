# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
print()
print("\033[1;3;35m  ​====== DUMMY Triple-Strike_Payload ======  ")
print("\033[0m")
print("\033[1;96m" + "="*50)
print("\033[0m")
print()
attempt = 0
def crack_password():
    global attempt
    attempt += 1
    secret_key = "cyber123"
    if attempt == 3:
        return f"\033[1;92m>>> {secret_key}\033[0m"
    else:
        return "\033[1;91m × Access Denied!\033[0m"
for i in range(3):
    result = crack_password()
    print(result)
    time.sleep(1)
