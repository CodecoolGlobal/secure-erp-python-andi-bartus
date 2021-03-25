import sys, os
sys.path.append(os.getcwd())
from model.sales import sales
from view import terminal as view
from colorama import*
init()

def list_transactions():
    table = sales.list_transactions()
    headers = sales.HEADERS
    view.print_table(table, headers)
    


def add_transaction():
    view.print_error_message("Not implemented yet.")


def update_transaction():
    view.print_error_message("Not implemented yet.")


def delete_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["(0) Back to main menu",
               "(1) List transactions",
               "(2) Add new transaction",
               "(3) Update transaction",
               "(4) Remove transaction",
               "(5) Get the transaction that made the biggest revenue",
               "(6) Get the product that made the biggest revenue altogether",
               "(7) Count number of transactions between",
               "(8) Sum the price of transactions between"]
    view.print_menu("Sales", options, Fore.LIGHTCYAN_EX)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation > ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)


menu()