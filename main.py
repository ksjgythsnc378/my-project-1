from colorama import init, Fore, Back, Style
init()
print(f"{Fore.RED}{Back.YELLOW}Hello World!{Style.RESET_ALL}")
print(f"{Fore.GREEN}Hello World in green!{Style.RESET_ALL}")
print(f"{Fore.BLUE}{Style.BRIGHT}Hello World in bright blue!{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}{Back.CYAN}{Style.BRIGHT}Hello world in bright magenta text and cyan background!{Style.RESET_ALL}")