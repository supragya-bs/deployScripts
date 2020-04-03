from tabulate import tabulate
from colorama import Fore, Back, Style
import time
import os

def green(str):
    return Fore.GREEN + str + Style.RESET_ALL
def red(str):
    return '\033[91m' + str + '\033[0m'
def yellow(str):
    return Fore.YELLOW + str + Style.RESET_ALL
def bold(str):
    return Style.BRIGHT + str + Style.RESET_ALL
def heraline():
    rows, columns = os.popen('stty size', 'r').read().split()
    heraline = "HERA v. 0.1.0b - Added mactest"
    app = "Mac Rigorous Tests"
    print(Fore.WHITE + Back.BLUE + Style.BRIGHT 
            + heraline 
            + " "*(int(columns) - len(heraline) - len(app)) 
            + Back.WHITE + Fore.BLACK
            + app
            + Style.RESET_ALL)

table = [
    [bold("Pingable"), bold("CHKMAC"), bold("CHKVER"), bold("Redis working?")],
    [green("Yes, latency = 32ms"), green("All working"), red("Missing - 1192, 1188"), yellow("Not all - redis not working")],
    [],
    [bold("Reachable"), bold("Logs shown?"), bold("Visible on prod?"), bold("instance_id")],
    [red("Not reachable"), green("Logs available"), red("Missing - 1192, 1188"), green("available")]
]
os.system("clear")
heraline()
print("Mac address: " + bold("192.168.0.1"))
print(tabulate(table))
print()
print("Mac address: " + bold("192.168.0.1"))
print(tabulate(table))

time.sleep(3)
table[1][1] = red("Cannot reach")
os.system("clear")
heraline()
print("Mac address: " + bold("192.168.0.1"))
print(tabulate(table))
print()
print("Mac address: " + bold("192.168.0.1"))
print(tabulate(table))