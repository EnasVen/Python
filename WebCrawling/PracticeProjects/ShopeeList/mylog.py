import colorama

def cyan(text):
    print(f'{colorama.Fore.CYAN}{text}{colorama.Style.RESET_ALL}')

def yellow(text):
    print(f'{colorama.Fore.YELLOW}{text}{colorama.Style.RESET_ALL}')

def red(text):
    print(f'{colorama.Fore.RED}{text}{colorama.Style.RESET_ALL}')

def green(text):
    print(f'{colorama.Fore.GREEN}{text}{colorama.Style.RESET_ALL}')

