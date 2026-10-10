# this script does not target any real systems and was created solely for educational purposes.
import time
import os
print("\033[1;96m" + "="*50)
print("\033[1;3;36m             MATH'S FUNCTION")
print("="*50 + "\033[0m")
print()
def check_number(a,b):
    return a + b
number = check_number(100,100)
print(f"\033[1;92m>>> {number}\033[0m")
time.sleep(1)
def room_1(a,c):
    return a **c
a = room_1(2,16)
print(f"\033[1;3;31m>>> {a}\033[0m")
time.sleep(1)
def room_2(a,d):
    return a /d
b = room_2(7,7)
print(f"\033[1;3;4;33m>>> {b}\033[0m")
time.sleep(1)
def room_3(y,z):
    return y % z
c = room_3(7,70)
print(f"\033[1;94m>>> {c}\033[0m")
time.sleep(1)
def room_4(y,b):
    return y - b
d = room_4(14,7)
print(f"\033[1;3;35m>>> {d}\033[0m")
time.sleep(1)
def room_5(s,b):
    return s > b
e = room_5(7,5)
print(f"\033[1;96m>>> {e}\033[0m")
time.sleep(1)
def room_6(f,z):
    return f < z
f = room_6(10,7)
print(f"\033[1;97m>>> {f}\033[0m")
time.sleep(1)
