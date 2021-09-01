import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.GREEN + '''Options Menu
    [1] - Upper case
    [2] - Lower case
    [3] - Title case
    [4] - Captalize case
    [5] - Invert case
    [0] - Finish Program
    ''')

def upper(phrase):
    phrase = phrase.upper()
    yield phrase
def lower(phrase):
    phrase = phrase.lower()
    yield phrase
def title(phrase):
    phrase = phrase.title()
    yield phrase
def capitalize(phrase):
    phrase = phrase.capitalize()
    yield phrase
def invert(phrase):
    phrase = phrase.swapcase()
    yield phrase

while True:
    option = input(Fore.YELLOW +'Option Choiced: ')
    try:
        if option.isdigit():
            option = int(option)
            if option == 0:
                os.system('cls')
                break
            elif option != 1 or 2 or 3 or 4 or 5:
                print('Digite uma opcao valida')

            phrase = input('Type or paste your content here:\n'+ Fore.BLUE + '-> ')
            print()

            if option == 1:
                print(Fore.RED + 'A Resultado eh: ' + Fore.BLUE + next(upper(phrase)) )
            elif option == 2:
                print(Fore.RED + 'A Resultado eh: ' + Fore.MAGENTA + next(lower(phrase)))
            elif option == 3:
                print(Fore.RED + 'A Resultado eh: ' + Fore.CYAN + next(title(phrase)))
            elif option == 4:
                print(Fore.RED + 'A Resultado eh: ' + Fore.YELLOW + next(capitalize(phrase)))
            elif option == 5:
                print(Fore.RED + 'A Resultado eh: ' + Fore.GREEN + next(invert(phrase)))
                
    except:
        print(Fore.RED +'Reenicie o programa e tente novamente!')
        break