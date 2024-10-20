import os
import requests
import urllib
import sys
import platform
import colorama
from func import menu
from colorama import  Fore

def clear():
    if(platform.system == 'Windows'):
            os.system("cls")
    else:
        os.system("clear")

link = ""
file = "proxy.txt"
times = 0
ip = "127.0.0.1"
inpstring = (f"{Fore.CYAN}Cern{Fore.WHITE}@{Fore.MAGENTA}User-{Fore.CYAN}[{Fore.WHITE}${Fore.CYAN}]{Fore.WHITE}#")

def main():
    while(1):
        clear()
        menu()
        choice = int(input(inpstring))
        if choice == 1:
            input()
        if choice == 2:
            input()
        if choice == 3:
            os.system(f"ping {ip}")
        if choice == 0:
            clear()
            open('proxy.txt', 'w').close()
            exit()
        else:
            print("Cern@admin-[$]> Invalid Choice")

main()




