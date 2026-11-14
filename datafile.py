# this script does not target any real systems and was created solely for educational purposes.
import time
import os
#os.system("clear")
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[1;96m" + "-"*50)
time.sleep(1)
print()
print("\033[1;3;36m      ===== ​Node Health Scanner.py  ======  ")
time.sleep(1)
print("\033[0m")
print("\033[1;96m" + "-"*50)
time.sleep(1)
print("\033[1;96m" + "="*50)
time.sleep(1)
print("\033[0m")
print()
status_codes = [200,200,404,500,200,700,244,552,777,875,542]
def node_scanner(*nodes):
    print("\033[1;3;35m Server Receiver Scanner Starting...\033[0m\n")
    time.sleep(1)
    print(f"\033[1;3;34m Total Nodes: {len(nodes)}\033[0m")
    time.sleep(1)
    for node in nodes:
        if node == 404:
            print(f"\033[1;3;31m>> Node {node}: Not Found!\033[0m")
            time.sleep(1)
        elif node == 500:
            print(f"\033[1;3;33m--> Node {node}: WARNING! Internal Server Error\033[0m")
            time.sleep(1)
        elif node == 777:
            print(f"\033[1;3;32m[✓] Success Node {node}: is Active\033[0m")
            time.sleep(1)
            break
        else:
            print(f"\033[1;3;36m[/] Normal Node: {node}\033[0m")
            time.sleep(1)
node_scanner(*status_codes)
