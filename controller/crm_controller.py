import sys, os
sys.path.append(os.getcwd())
from model.crm import crm
from view import terminal as view
from colorama import*
init()


def list_customers():
    os.system('clear')
    view.print_message('------------------')
    view.print_message('    Customers ')
    view.print_message('------------------\n')
    table = crm.list_customers()
    headers = crm.HEADERS
    view.print_table(table, headers)
    view.get_input('\nBack to menu press Enter')
    os.system('clear')
    


# list_customers()


def add_customer():
    os.system('clear')
    view.print_message('------------------')
    view.print_message(' Add new customer')
    view.print_message('------------------\n')
    labels = crm.HEADERS[1:]   
    new_data = view.get_inputs(labels)
    crm.add_customer_data(new_data)
    view.get_input('\nBack to menu press Enter')
    os.system('clear')
    



def update_customer():
    os.system('clear')
    view.print_message('------------------')
    view.print_message(' Update customer')
    view.print_message('------------------\n')
    table = crm.list_customers()    
    i_d = view.get_input("Please provide an ID or exit > ")
    if i_d == 'exit':
        os.system('clear')
           
    else: 
        while True:
            for lst in table:
                if lst[0] == i_d:
                    update_data = view.get_input("\nWhat do you want to update? 1: name | 2: e-mail | 3: subscribe status | 0: Exit  >  ")
                    if update_data == "1":
                        name = view.get_input("\nNew name >  ")
                        lst[1] = name
                    if update_data == "2":
                        e_mail = view.get_input("\nNew e_mail >  ")
                        lst[2] = e_mail
                    if update_data == "3":
                        sub_status = view.get_input("\nNew sunscribe status >  ")
                        lst[3] = sub_status
                    if update_data == '0':
                        display_menu()
                            
            crm.update_costumer(table)
            again = view.get_input("\nAnything else to update? Y/N >  ").lower()
            if again =='y':
                True
            else:
                break
   
    

def delete_customer():
    os.system('clear')
    view.print_message('------------------')
    view.print_message(' Delete customer')
    view.print_message('------------------\n')        
    table = crm.list_customers()
    i_d = view.get_input("Provide and ID or exit > ")
    for lst in table:
        if lst[0] == i_d:
            table.remove(lst)
        if i_d == 'exit':
            os.system('clear')
            display_menu()
    crm.update_costumer(table)
    view.get_input('\nBack to menu press Enter')
    os.system('clear')
    

    


def get_subscribed_emails():
    os.system('clear')
    table = crm.list_customers()
    subscribed_list = [lst[-2] for lst in table if lst[-1] == '1']
    view.print_menu('Subscribed e-mails', subscribed_list, Fore.LIGHTCYAN_EX)
    view.get_input('\nBack to menu press Enter')
    os.system('clear')
               


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    os.system('clear')
    options = ["(0) Back to main menu",
               "(1) List customers",
               "(2) Add new customer",
               "(3) Update customer",
               "(4) Remove customer",
               "(5) Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options, Fore.LIGHTCYAN_EX)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation > ")
            
            run_operation(int(operation))
            
        except KeyError as err:
            view.print_error_message(err)


