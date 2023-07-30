# -*- coding: utf-8 -*-
# There is three functions: one to print the tables, one to prompt the user
# and one to clear the terminal screen

# Only for clear the terminal screen and add compatibility for windows
import os 


def clear():
    # This function clear the terminal screen depending of the operating system

    opr_system = os.name

    if opr_system == 'nt': #windows
        os.system('cls')
    else:                  #linux or macos
        os.system('clear')

def select_tables(tables: list):
    # This functions let the user choose which table he wants to see
    
    choose = input()
    match choose:
        case '1':
            clear()
            while True:
                print(tables[0])
                go_back = input()
                if go_back == 'r':
                    clear()
                    break
                else:
                    clear()
                    continue

        case '2':
            clear()
            while True:
                print(tables[1])
                go_back = input()
                if go_back == 'r':
                    clear()
                    break
                else:
                    clear()
                    continue

        case '3':
            print("\nSee you later!\n")
            exit()

        case _:
            clear()
            print('Please select one avaliable table')


def show_info():
    # This function show useful info
    clear()
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
