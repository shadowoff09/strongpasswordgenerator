# Strong random password generator
# By @shadowoff09
# Totally random generator if you have questions you can check my github repository https://github.com/shadowoff09/PasswordGenerator


import random
import time
import clipboard
import os
from string import digits, ascii_letters


class textcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
os.system('cls' if os.name == 'nt' else 'clear')

length = int(input("\nHow many digits should your password be?: "))
symbols = ascii_letters + digits
secure_random = random.SystemRandom()
password = "".join(secure_random.choice(symbols)
    for i in range(length))

print(f'\n\nGenerating your password with {length} characters...')

time.sleep(1)

print(f'\n\nHere is your password: {password}\n\n')



print(f'Totally random generator if you have questions you can check my github repository https://github.com/shadowoff09/PasswordGenerator\n\n')


