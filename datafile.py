# Only education purpose
# Python while loop challenge: Skip even numbers with continue, print only odd numbers > 5, ensure counter increases every round. Debugged indentation bug causing infinite loop on Termux.
count = 1
while count <= 5:
    num = int(input("Enter num:"))
    if num % 2 == 0:
        print (f"\033[1;3;32m {num}\033[0m")
        count += 1
        continue
    if num > 5:
        print (f"\033[1;3;31m {num}\033[0m")
    count += 1
