import os
import subprocess
import requests
import urllib
import sys
import platform
import colorama
from func import menu
from colorama import  Fore
from spammer import dos

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
            dos()
        if choice == 2:
            input()
        if choice == 3:

            subprocess.Popen(["open", 'ping.py'])
        if choice == 4:
            domain = input(f"{inpstring}> Enter domain url :")
            api_url = 'https://api.api-ninjas.com/v1/whois?domain={}'.format(domain)
            whois_api = input(f"{inpstring}> Enter your WhoIs? api key :")
            response = requests.get(api_url, headers={'X-Api-Key': whois_api})
            if response.status_code == requests.codes.ok:
                print(response.text)
            else:
                print("Error:", response.status_code, response.text)
        if choice == 0:
            clear()
            open('proxy.txt', 'w').close()
            exit()
        else:
            print("Cern@admin-[$]> Invalid Choice")

main()




