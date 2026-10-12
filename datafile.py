# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
print("\033[1;3;35m               Dummy ​access_control.py ")
print("\033[1;94m" + "="*50)
print("\033[0m")
print()
def my_function(username,password):
    if username == "admin123":
        print(f"\033[1;92m>>>  {username}: correct username\033[0m")
        if password == "2212":
            return "correct password Access granted"
        else:
            return  "wrong password Access decline"
    else:
        return "wrong username"
result_1 = my_function("admin123","2212")
result_2 = my_function("admim","2122")
print(f"\033[1;92m>>> {result_1}\033[0m")
time.sleep(1)
