# Strong random password generator
# By @shadowoff09
# Totally random generator if you have questions you can check my github repository github.com/shadowoff09



import random
from string import digits, punctuation, ascii_letters


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

length = int(input("\nHow many digits should your password be?: "))
symbols = ascii_letters + digits
secure_random = random.SystemRandom()
password = "".join(secure_random.choice(symbols)
    for i in range(length))



print(f'\n\nHere is your password: {textcolors.WARNING}{password}{textcolors.ENDC}\n\n')



print(f'Totally {textcolors.FAIL}random{textcolors.ENDC} generator if you have questions you can check my github repository {textcolors.OKBLUE}https://github.com/shadowoff09{textcolors.ENDC}\n\n')

12
