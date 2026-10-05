# this script does not target any real systems and was created solely for educational purposes.
import time
print("--------------------------------------")
print("======================================")
print("\033[1;3;35m Dummy  Safe Port Scanner\033[0m")
print("======================================")
print("--------------------------------------")
print()
def safe_port():
    ports = [21,22,80,443]
    while True:
        pwd = input("Enter Target ip: (exit to 0: ")
        if pwd == "0":
            print("\033[1;93m Scanner stopped!\033[0m")
            time.sleep(1)
            break
        elif pwd == "127,0,0,1":
            print(f"\033[1;92m>> Scan Allow\033[0m")
            time.sleep(1)
        else:
            print("\033[1;91m[WARNING] External Ips are blocked\033[0m")
            continue
        for i in ports:
            print(f"\033[1;3;4;36m  Scanning port>>> {i} close\033[0m")
            time.sleep(1)

        print(f"\033[1;94m >>> {pwd} secure <<<\033[0m")
safe_port()
