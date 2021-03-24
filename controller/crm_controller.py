import sys, os
sys.path.append(os.getcwd())
from model.crm import crm
from view import terminal as view


def list_customers():
    table = crm.list_customers()
    headers = crm.HEADERS
    view.print_table(table, headers)
    #view.print_error_message("Not implemented yet.")
    


# list_customers()


def add_customer():
    labels = crm.HEADERS[1:]   
    new_data = view.get_inputs(labels)
    crm.add_customer_data(new_data)
    
# add_customer()


def update_customer():
    table = crm.list_customers()    
    i_d = view.get_input("Please provide an ID > ")
    while True:
        for lst in table:
            if lst[0] == i_d:
                update_data = view.get_input("What do you want to update? 1: name | 2: e-mail | 3: subscribe status | 0: Exit  >  ")
                if update_data == "1":
                    name = view.get_input("New name >  ")
                    lst[1] = name
                if update_data == "2":
                    e_mail = view.get_input("New e_mail >  ")
                    lst[2] = e_mail
                if update_data == "3":
                    sub_status = view.get_input("New sunscribe status >  ")
                    lst[3] = sub_status
                if update_data == '0':
                    display_menu()
        crm.update_costumer(table)
        again = view.get_input("Anything else to update? Y/N >  ").lower()
        if again =='y':
            True
        else:
            break
    #display_menu()
    
#update_customer()     




def delete_customer():
    table = crm.list_customers()
    i_d = view.get_input("ID > ")
    for lst in table:
        if lst[0] == i_d:
            table.remove(lst)
    crm.update_costumer(table)
    

    
#delete_customer()

def get_subscribed_emails():
    table = crm.list_customers()
    subscribed_list = [lst[-2] for lst in table if lst[-1] == '1']
    print('Emails: ' + ", ".join(subscribed_list))
               
#get_subscribed_emails()

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
    options = ["0 Back to main menu",
               "1 List customers",
               "2 Add new customer",
               "3 Update customer",
               "4 Remove customer",
               "5 Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


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