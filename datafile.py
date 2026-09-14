# Day 9 - Even / Odd Filter with Continue
# Challenge: 5 inputs, print only odd > 5, skip even with continue

count = 1
while count <= 5:
    num = int(input("Enter num: "))

    if num % 2 == 0:
        print (f"\033[1;3;32m {num} \033[0m")
        count += 1
        continue

    if num > 5:
        print(f"\033[1;3;31m odd {num}\033[0m")
    count += 1
