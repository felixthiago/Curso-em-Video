

from colorama import * 
init()

from datetime import *
now = datetime.now()
dateTime = now.strftime("%H:%M:%S")


strTime = f"{Fore.LIGHTMAGENTA_EX}[{Fore.MAGENTA}*{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} {dateTime} ~ "
cer = f'{Fore.LIGHTGREEN_EX}[{Fore.GREEN}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} ~ '
err = f'{Fore.LIGHTRED_EX}[{Fore.RED}-{Fore.LIGHTRED_EX}] ~ {Fore.RESET}'
choice = f'[{Fore.YELLOW}.{Fore.RESET}] {dateTime} {Fore.YELLOW}P{Fore.BLUE}y{Fore.YELLOW}t{Fore.BLUE}h{Fore.YELLOW}o{Fore.BLUE}n{Fore.YELLOW}:{Fore.RESET} '



import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')