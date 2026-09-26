# this script does not target any real systems and was created solely for educational purposes.
import time
print ("======================================")
print ("\033[1;3;34m Mini DirBuster Simulator\033[0m")
print ("======================================")
print()
target_url = "[www.target.com](https://www.target.com)"
worldlist = ["/contact","/images","/robots.txt","/adminl_panel","/congig.php"]
for path in worldlist:
    print (f"\033[1;93m[*] Scanning: {target_url} {path}\033[0m")
    if path == "/adminl_panel":
        print (f"\033[1;3;4;32m[✓]BOOM! hidden {path}: found\033[0m")
        break
    else:
        print ("\033[1;91m[!]404 not found[!]\033[0m")
        time.sleep(1)
