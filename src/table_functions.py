# -*- coding: utf-8 -*-
# There is two functions: one to print the tables and one to prompt the user

import os # Only for clear the terminal screen and add compatibility for windows

def select_tables(tables: list):
    # This functions let the user choose which table he wants to see
    
    opr_system = os.name
    clear = 'clear' if opr_system == 'posix' else 'cls'

    choose = input()
    match choose:
        case '1':
            os.system(clear)
            print(tables[0])

        case '2':
            os.system(clear)
            print(tables[1])

        case _:
            os.system(clear)
            print('Please select one avaliable table')

