# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print()
print("\033[1;3;35m      ====== DUMMY Payload Obfuscation ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
def encode_payload(num):
    return (num * 3) + 7
def check_access(encoded_num):
    if encoded_num == 307:
        return True
    else:
        return False
for i in range(50,150):
    if check_access(encode_payload(i)):
        print(f"\033[1;92m>>> Firewall! Correct Raw {i}\033[0m")
        time.sleep(1)
        break
    else:
        print(f"\033[1;91m>> Falied PIN {i}\033[0m")
        time.sleep(0.05)


