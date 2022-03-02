import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class ConvertCase:


    def __init__(self):
        pass

    def upper(self, phrase):
        self.phrase = phrase.upper()
        yield self.phrase
    def lower(self,phrase):
        self.phrase = phrase.lower()
        yield self.phrase
    def title(self,phrase):
        self.phrase = phrase.title()
        yield self.phrase
    def capitalize(self,phrase):
        self.phrase = phrase.capitalize()
        yield self.phrase
    def invert(self,phrase):
        self.phrase = phrase.swapcase()
        yield self.phrase



cc = ConvertCase()

print(Fore.GREEN + '''Options Menu
    [1] - Upper case
    [2] - Lower case
    [3] - Title case
    [4] - Captalize case
    [5] - Invert case
    [0] - Finish Program
    ''')


option = input(Fore.YELLOW +'Option Choiced: ')
try:
    if option.isdigit():
        option = int(option)

        if option == 0:
            print(Fore.GREEN + 'Bye...')

        else:
            phrase = input('Type or paste your content here:\n'+ Fore.BLUE + '-> ')
            print()

            if option == 1:
                print(Fore.BLUE + next(cc.upper(phrase)) )
            elif option == 2:
                print(Fore.MAGENTA + next(cc.lower(phrase)))
            elif option == 3:
                print(Fore.CYAN + next(cc.title(phrase)))
            elif option == 4:
                print(Fore.YELLOW + next(cc.capitalize(phrase)))
            elif option == 5:
                print(Fore.GREEN + next(cc.invert(phrase)))
            else:
                print('Enter a Valid option')
            
except:
    print(Fore.RED +'Rebooting program.')
