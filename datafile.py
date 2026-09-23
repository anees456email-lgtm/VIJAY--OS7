import time
count = 1
while count <= 5:
    if count == 3:
        print (f"\033[1;32m {count} Checkpoint\033[0m")
    else:
        print (f"\033[1;91m {count} Round\033[0m")
    count += 1
    time.sleep(1)
print ("\033[1;93m Program Finished\033[0m")

