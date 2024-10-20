from colorama import Fore

def menu():
    
    ascii_path = 'ascii.txt'
    with open(ascii_path, 'r') as ascii:
            ascii_content = ascii.read()
            print(Fore.MAGENTA, ascii_content)
    print("\n")
    print(f"{Fore.CYAN}[0] - {Fore.WHITE}Panic   {Fore.MAGENTA}[1] - {Fore.WHITE}Start   {Fore.CYAN}[2] - {Fore.WHITE}Proxies    {Fore.MAGENTA}[3] - {Fore.WHITE}Ping")
    print(f"{Fore.WHITE}[4] - {Fore.CYAN}WhoIs?   {Fore.WHITE}[5] - {Fore.MAGENTA}Layer   {Fore.WHITE}[6] - {Fore.CYAN}Unsafe Mode    {Fore.WHITE}[8] - {Fore.MAGENTA}Credits")
    print("\n")