# This simple script will calculate what the length of the fence around a flower bed and how many flowers do you need


import math
import sys


# DRY
def exit(code: int):
    input('\nPress ENTER to exit... ')
    sys.exit(code)


# Mode
answer = input('Is your flower bed round? (y/[n])\n>>> ').lower()

# Little check
if not answer in ['y', 'n', '']:
    print('Type only [y] or [n] or [<NOTHING>]')

    exit(-1)

is_round = True if answer == 'y' else False


# Collecting data
try:
    density = int(input('Enter how many flowers per square meter do you want?\n>>> '))
except ValueError as e:
    print('\n\nError message: %s\n' % str(e))

    print('Please, type only digits. (e.g. the input "four" is invalid, while "4" is valid)')

    exit(-1)

try:
    if not is_round:
        length = float(input('Enter the length in meters of your flower bed\n>>> ').replace(',', '.'))
        width  = float(input('Enter the width in meters of your flower bed\n>>> ').replace(',', '.'))
    else:
        diameter = float(input('Enter the diameter in meters of your flower bed\n>>> '.replace(',', '.')))
except ValueError as e:
    print('\n\nError message: %s\n' % str(e))

    print('Please, type only digits. (e.g. the input "fifty-nine point four" is invalid, while "59.4" or "59,4" is valid)')

    exit(-1)


# Calculation
if not is_round:
    perimiter = 2 * (length + width)
    square = length * width
else:
    perimiter = math.pi * diameter
    square = math.pi * (diameter * 0.5) ** 2

flowers_amount = math.floor(square * density)


# Printing out the info and exiting
print('The needed length of the fence is %s meters' % str(round(perimiter, 2)))
print('And, you need %d flowers' % flowers_amount)

exit(0)
