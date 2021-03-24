import sys, os
sys.path.append(os.getcwd())
from model.hr import hr
from view import terminal as view
from colorama import*


def list_employees():
    os.system('clear')
    table = hr.list_employees()
    headers = hr.HEADERS
    view.print_table(table, headers)
    view.get_input('\nBack to menu press Enter')
    
    


#list_employees()

def add_employee():

    view.print_error_message("Not implemented yet.")


def update_employee():
    view.print_error_message("Not implemented yet.")


def delete_employee():
    view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["(0) Back to main menu",
               "(1) List employees",
               "(2) Add new employee",
               "(3) Update employee",
               "(4) Remove employee",
               "(5) Oldest and youngest employees",
               "(6) Employees average age",
               "(7) Employees with birthdays in the next two weeks",
               "(8) Employees with clearance level",
               "(9) Employee numbers by department"]
    view.print_menu("Human resources", options, Fore.LIGHTCYAN_EX)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
menu()