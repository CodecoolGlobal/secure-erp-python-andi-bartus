import sys, os
from view import terminal as view
from controller import crm_controller, sales_controller, hr_controller
from colorama import*

def load_module(option):
    if option == 1:
        crm_controller.menu()
    elif option == 2:
        sales_controller.menu()
    elif option == 3:
        hr_controller.menu()
    elif option == 0:
        return 0
    else:
        raise KeyError()


def display_menu():
    os.system('clear')
    
    options = ["(0) Exit program",
               "(1) Customer Relationship Management (CRM)",
               "(2) Sales",
               "(3) Human Resources"]
    print(Fore.BLUE +ascii_art)
    view.print_menu("Main menu", options, Fore.LIGHTCYAN_EX)

# TODO different module, separate txt
ascii_art ='''
 __    __   _______     ___   ____    ____  _______ .__   __.     _______ .______      .______   
|  |  |  | |   ____|   /   \  \   \  /   / |   ____||  \ |  |    |   ____||   _  \     |   _  \  
|  |__|  | |  |__     /  ^  \  \   \/   /  |  |__   |   \|  |    |  |__   |  |_)  |    |  |_)  | 
|   __   | |   __|   /  /_\  \  \      /   |   __|  |  . `  |    |   __|  |      /     |   ___/  
|  |  |  | |  |____ /  _____  \  \    /    |  |____ |  |\   |    |  |____ |  |\  \----.|  |      
|__|  |__| |_______/__/     \__\  \__/     |_______||__| \__|    |_______|| _| `._____|| _|      
'''

def menu():
    
    option = None
    while option != '0':
        display_menu()
        try:
            option = view.get_input("Select module > ")
            load_module(int(option))
        except KeyError:
            view.print_error_message("There is no such option!")
        except ValueError:
            view.print_error_message("Please enter a number!")
    view.print_message("Good-bye!")
