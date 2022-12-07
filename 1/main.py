import math
import sys


# Collecting data
try:
    length = float(input('Enter the length in meters of a flower bed: ').replace(',', '.'))
    width  = float(input('Enter the width in meters of the flower bed: ').replace(',', '.'))
except ValueError as e:
    print('\n\nError message: %s\n' % str(e))
    print('Please, type only digits. (e.g. the input "one" is invalid, while "59.4" or "59,4" is valid)')
    input('\nPress ENTER to exit... ')
    sys.exit(-1)


# Calculation
perimiter = 2 * (length + width)
square = length * width

flowers_amount = math.floor(square * 4)


# Printing out the info and exiting
print('The needed length of the fence is %s meters' % str(round(perimiter, 2)))
print('Also, you need %d flowers' % flowers_amount)

input('\nPress ENTER to exit... ')
sys.exit(0)
