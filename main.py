import colorama

from colorama import Fore, Back, Style

print(Fore.RED + 'texto vermelho\n')

print(Back.GREEN + 'fundo verde\n')

print(Style.BRIGHT + 'enfatizar o texto\n')

print(Style.RESET_ALL)
print('Voltando ao normal...')

"""

As constantes de formatação disponíveis são:
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
  
Style.RESET_ALL 
redefine o primeiro plano, o plano de fundo e o brilho. 
O Colorama realizará essa reinicialização automaticamente na saída do programa.

"""
