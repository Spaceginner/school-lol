# This script will show how do you need to label your notebook. yea, it is not in english this time, srry :Э
# (yes, centering the text is a part of the hometask)


import os
import sys


# DRY
def exit(code: int):
    input('\nНажміть ENTER для виходу... ')
    sys.exit(code)


# Setting up some vars
terminal_width = os.get_terminal_size()[0]


# Collecting data
answer = input("Ви чоловік? (y/n)\n>>> ").lower()

if answer in ['y', 'n']:
    is_male = True if answer == "y" else False
else:
    print("\n\nПотрібно відповісти на запитання латинською літерою [y] (Так) або [n] (Ні).\n")

    exit(-1)

    

name = input("Ваше ім'я (у родовому відмінку)\n>>> ")
surname = input("Ваше прізвище (у родовому відмінку)\n>>> ")
school = input("Назва вашої школи (у родовому відмінку)\n>>> ")
grade = input("Ваш клас\n>>> ")
subject = input("Шкільний предмет у родовому відмінку)\n>>> ")

# Outputing how the user should label his notebook
print('\n\n')
print(f"Зошит".center(terminal_width, ' '))
print(f"з {subject}".center(terminal_width, ' '))
print(f'{"учня" if is_male else "учениці"} {grade} класу'.center(terminal_width, ' '))
print(f"{school}".center(terminal_width, ' '))
print(f"{surname} {name}".center(terminal_width, ' '))
print('\n\n')

exit(0)
