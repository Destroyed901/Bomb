from colorama import Fore
from colorama import Fore, Back, Style
from termcolor import colored
import requests, time, webbrowser, os

Logo = colored("""


    ____  ____  __  _______ 
   / __ )/ __ \/  |/  / __ )
  / __  / / / / /|_/ / __  |
 / /_/ / /_/ / /  / / /_/ / 
/_____/\____/_/  /_/_____/  
         channel: https://t.me/eniac_tg

1 - Mail Bomber
2 - Phone Bomber    
""", "red")
print(Logo)
while True:
    shell = input('choose from this:')
    if shell == '1':
        webbrowser.open_new_tab('Mail.html')
    elif shell == '2':
        os.system('python Destroyer.py')
