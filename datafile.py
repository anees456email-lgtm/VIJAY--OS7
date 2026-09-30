# this script does not target any real systems and was created solely for educational purposes.

print ("======================================")
print ("\033[1;3;36m while loop and for loop\033[0m")
print ("======================================")
print()
count = 1
while count <= 2:
    for i in range(3):
        print (f"\033[1;92m count {count} i {i} \033[0m")
    count += 1
print ("\033[1;95m[*]Finished[*]\033[0m")
