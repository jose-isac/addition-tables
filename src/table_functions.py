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
            while True:
                print(tables[0])
                go_back = input()
                if go_back == 'y':
                    os.system(clear)
                    break
                else:
                    os.system(clear)
                    continue

        case '2':
            os.system(clear)
            while True:
                print(tables[1])
                go_back = input()
                if go_back == 'y':
                    os.system(clear)
                    break
                else:
                    os.system(clear)
                    continue

        case '3':
            print("\nSee you later!\n")
            exit()

        case _:
            os.system(clear)
            print('Please select one avaliable table')


def show_info():
    # This function show useful info
    
    message = """
    ======================================================
    #                                                    #
    #   Hello! Which table do you want to study today?   #
    #                                                    #
    #   1. Table One                                     #
    #   2. Table Two                                     #
    #                                                    #
    #   3. Exit                                          #
    #                                                    #
    #   !Enter a number between 1 and 3                  #
    #                                                    #
    ======================================================

    """
    print(message)
