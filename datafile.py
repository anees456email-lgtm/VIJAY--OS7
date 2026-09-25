# This is merely a fake packet scanner; this script does not target any real systems and was created solely for educational purposes.
import time
print ("======================================")
print ("\033[1;3;36m Fake packet_sender\033[0m")
print ("======================================")
print()
packet = 0
while packet < 10:
    packet += 1
    if packet == 4 or packet == 7:
        print (f"\033[1;91m[!]packet {packet}: corrupted skipping...\033[0m")
        continue
    else:
        print (f"\033[1;3;4;32m[+]packet {packet}: sent successfully[+]\033[0m")
        time.sleep(1)
print()
print ("\033[1;93m[✓]All data transfer complete[✓]\033[0m")
