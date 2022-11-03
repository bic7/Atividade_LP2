import colorama

from colorama import Fore, Back, Style

print(Fore.RED + 'texto vermelho\n')

print(Back.GREEN + 'fundo verde\n')

print(Style.BRIGHT + 'enfatizar o texto\n')

print(Style.RESET_ALL)
print('Voltando ao normal...')