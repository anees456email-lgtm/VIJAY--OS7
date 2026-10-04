# this script does not target any real systems and was created solely for educational purposes.
import time
print ("--------------------------------------")
print ("======================================")
print ("\033[1;3;34m Dummy  Auto Network Scanner\033[0m")
print ("======================================")
print ("--------------------------------------")
print()
def auto_scan():
    targets = ["192.187.22.2","10.0.0.1","8.8.8.8"]
    print(f"\033[1;93m starting {targets}\033[0m")
    for target in targets:
        print(f"\033[1;92m[*]Hacking ip >>> {target}[*]\033[0m")
        time.sleep(1)
auto_scan()
