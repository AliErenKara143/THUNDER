import os

import requests
import argparse
import colorama
import sys

import threading

import getpass

def print_usage():
    usage = """
    ########################################
    usage : python3 Thunder.py -t {target}
    ########################################
    """

    print(usage)
    sys.exit(1)

wordlists = open(f'/home/{getpass.getuser()}/Masaüstü/THUNDER/wordlist.txt').readlines()
found = []

def banner():
    os.system("clear")
    os.system("figlet THUNDER -f big")

def generateError(err="Error!"):
    print(f"{colorama.Fore.BLUE}[{colorama.Fore.RED}-{colorama.Fore.BLUE}] {colorama.Fore.RESET}{err}")
    sys.exit(1)
def get_target():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t" , "--target" , dest="target" , help="Specify target's address")
    args = parser.parse_args()

    if args.target:
        return args.target

    else:
        print_usage()

def scan(links):
    for link in links:
        link = "http://" + get_target() + "/" + link

        r = requests.get(link)
        http = r.status_code

        if http == 200 and "not found" not in str(r.content):
            print(f"{colorama.Fore.BLUE}[+] Possible Admin Panel Found : {colorama.Fore.YELLOW}{link}")
            found.append(link)

        else:
            print(f"{colorama.Fore.RED}[-] Not Found : {link}")


def thread():
    path1 = wordlists[:100]
    path2 = wordlists[101:200]
    path3 = wordlists[201:300]
    path4 = wordlists[301:400]


    def part1():
                link = path1
                scan(link)

    def part2():
        link = path2
        scan(link)

    def part3():
        link = path3
        scan(link)

    def part4():
        link = path4
        scan(link)

    t1 = threading.Thread(target=part1)
    t2 = threading.Thread(target=part2)
    t3 = threading.Thread(target=part3)
    t4 = threading.Thread(target=part4)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

def print_founds():
  if len(found) == 0:
      print(f"{colorama.Fore.RED}[-] No Admin Panels Found")
  else:
    print("")
    print("-" * 40)
    print(f"{colorama.Fore.YELLOW}Founded admin-panel count {len(found)}\n")
    print(f"\nFounded admin panels : ")
    for i in found:
        print(i)
    print("-" * 40)
    print("")


if __name__ == '__main__':
    get_target()
    banner()
    thread()
    print_founds()



