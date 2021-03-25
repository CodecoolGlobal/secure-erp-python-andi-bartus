import sys, os
sys.path.append(os.getcwd())
from model.sales import sales
from view import terminal as view
from colorama import*
init()

def list_transactions():
    os.system('clear')
    view.print_message('------------------')
    view.print_message('  Transactions ')
    view.print_message('------------------\n')
    table = sales.list_transactions()
    headers = sales.HEADERS
    view.print_table(table, headers)
    view.get_input('\nBack to menu press Enter')
    os.system('clear')


def add_transaction():
    os.system('clear')
    view.print_message('-----------------')
    view.print_message(' Add transaction')
    view.print_message('-----------------\n')
    labels = sales.HEADERS[1:]   
    new_data = view.get_inputs(labels)
    sales.add_transactions(new_data)
    view.get_input('\nBack to menu press Enter')
    os.system('clear') 


def update_transaction():
    os.system('clear')
    view.print_message('--------------------')
    view.print_message(' Update transaction')
    view.print_message('--------------------\n')
    table = sales.list_transactions()    
    i_d = view.get_input("Please provide an ID or exit > ")
    if i_d == 'exit':
        os.system('clear')
           
    else: 
        while True:
            for lst in table:
                if lst[0] == i_d:
                    update_data = view.get_input("\nWhat do you want to update? 1: customer | 2: product | 3: price | 4: date | 0: Exit  >  ")
                    if update_data == "1":
                        name = view.get_input("\nNew customer >  ")
                        lst[1] = name
                    if update_data == "2":
                        e_mail = view.get_input("\nNew product >  ")
                        lst[2] = e_mail
                    if update_data == "3":
                        sub_status = view.get_input("\nNew price >  ")
                        lst[3] = sub_status
                    if update_data == "4":
                        date= view.get_input("\nNew date >  ")
                        lst[4] = date
                    if update_data == '0':
                        display_menu()
                            
            sales.update_transactions(table)
            again = view.get_input("\nAnything else to update? Y/N >  ").lower()
            if again =='y':
                True
            else:
                break


def delete_transaction():
    os.system('clear')
    view.print_message('--------------------')
    view.print_message(' Delete transaction')
    view.print_message('--------------------\n')        
    table = sales.list_transactions()
    i_d = view.get_input("Provide and ID or exit > ")
    for lst in table:
        if lst[0] == i_d:
            table.remove(lst)
        if i_d == 'exit':
            os.system('clear')
            display_menu()
    sales.update_transactions(table)
    view.get_input('\nBack to menu press Enter')
    os.system('clear')


def get_third(item):
    return float(item[3])


def get_biggest_revenue_transaction():
    os.system('clear')
    view.print_message('-----------------------------')
    view.print_message(' Biggest revenue transaction')
    view.print_message('-----------------------------\n') 
    table = sales.list_transactions()
    sorted_table = sorted(table, key=get_third)
    headers = sales.HEADERS
    #print(sorted_table[-1])
    st = [sorted_table[-1]]
    view.print_table(st, headers)
    view.get_input('\nBack to menu press Enter')
    os.system('clear')
    
    
    
   


def get_biggest_revenue_product():
    os.system('clear')
    view.print_message('---------------------------')
    view.print_message(' Biggest revenue product ')
    view.print_message('---------------------------\n') 
    table = sales.list_transactions()
    
    product= {}
    for lst in table:
        if lst[2]  not in product.keys():
            product[lst[2]] = 0
        if lst[2] in product.keys():
            product[lst[2]] += float(lst[3])
    
        
    max_price = max(product.values())
    for key, value in product.items():
        if value == max_price:
            view.print_message(f'\nBiggest revenue product is: {key}')
    view.get_input('\nBack to menu press Enter')
    os.system('clear')

   


def count_transactions_between():
    os.system('clear')
    view.print_message('-----------------------------------')
    view.print_message(' Count transactions between 2 dates ')
    view.print_message('-----------------------------------\n') 
    table = sales.list_transactions()
    labels = ['First date (yyyy-mm-dd)', 'Second date (yyyy-mm-dd)']
    new_data = view.get_inputs(labels)
    view.print_message(len(sales.find_dates_between(table, new_data)))
    view.get_input('\nBack to menu press Enter')
    os.system('clear')


def sum_transactions_between():
    os.system('clear')
    view.print_message('-----------------------------')
    view.print_message(' Sum prices between 2 dates')
    view.print_message('-----------------------------\n') 
    table = sales.list_transactions()
    labels = ['First date (yyyy-mm-dd)', 'Second date (yyyy-mm-dd)']
    new_data = view.get_inputs(labels)
    dates_between = sales.find_dates_between(table, new_data)
    view.print_message(sum([float(lst[3]) for lst in table if int(lst[-1].replace("-", "")) in dates_between]))
    view.get_input('\nBack to menu press Enter')
    os.system('clear')


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
    os.system('clear')
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



