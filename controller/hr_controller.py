import sys, os
sys.path.append(os.getcwd())
from model.hr import hr
from view import terminal as view
from colorama import*


def list_employees():
    os.system('clear')
    view.print_message('------------------')
    view.print_message('    Employees ')
    view.print_message('------------------\n')
    table = hr.list_employees()
    headers = hr.HEADERS
    view.print_table(table, headers)
    view.get_input('\nBack to menu press Enter')
    
    


#list_employees()

def add_employee():
    os.system('clear')
    view.print_message('------------------')
    view.print_message(' Add new employee')
    view.print_message('------------------\n')
    labels = hr.HEADERS[1:]   
    new_data = view.get_inputs(labels)
    hr.add_employee_data(new_data)
    view.get_input('\nBack to menu press Enter')
    os.system('clear') 
    
  
def update_employee():
    os.system('clear')
    view.print_message('------------------')
    view.print_message(' Update employee')
    view.print_message('------------------\n')
    table = hr.list_employees()    
    i_d = view.get_input(" ID or exit > ")
    if i_d == 'exit':
        os.system('clear')
           
    else: 
        while True:
            for lst in table:
                if lst[0] == i_d:
                    update_data = view.get_input("\nWhat do you want to update? 1: name | 2: date of birth | 3: department | 4: clearance | 0: Exit  >  ")
                    if update_data == "1":
                        name = view.get_input("\nNew name >  ")
                        lst[1] = name
                    if update_data == "2":
                        e_mail = view.get_input("\nNew date of birth > ")
                        lst[2] = e_mail
                    if update_data == "3":
                        sub_status = view.get_input("\nNew department >  ")
                        lst[3] = sub_status
                    if update_data == "4":
                        clear = view.get_input("\nNew clearance >  ")
                        lst[4] = clear
                    if update_data == '0':
                        display_menu()
                            
            hr.update_employee(table)
            again = view.get_input("\nAnything else to update? Y/N >  ").lower()
            if again =='y':
                True
            else:
                break




def delete_employee():
    os.system('clear')
    view.print_message('------------------')
    view.print_message(' Delete employee')
    view.print_message('------------------\n')        
    table = hr.list_employees()
    i_d = view.get_input("Provide and ID or exit > ")
    for lst in table:
        if lst[0] == i_d:
            table.remove(lst)
        if i_d == 'exit':
            os.system('clear')
            display_menu()
    hr.update_employee(table)
    view.get_input('\nBack to menu press Enter')
    os.system('clear')

def get_second(item):
    return item[2]


def get_oldest_and_youngest():
    os.system('clear')
    table = hr.list_employees()
    sorted_table = sorted(table, key=get_second)
    old_young = [sorted_table[0][1], sorted_table[-1][1]]
    os.system('clear')
    view.print_message('-----------------------')
    view.print_message('Youngest:       Oldest:')    
    print(f"{old_young[0]}             {old_young[1]}")
    view.get_input('\nBack to menu press Enter')
    os.system('clear')
    


def get_average_age():
    os.system('clear')
    view.print_message('--------------------------')
    view.print_message(' Average age of employees')
    view.print_message('--------------------------\n')  
    import datetime
    now = datetime.datetime.now().year
    table = hr.list_employees()
    dates = [int(date[2][0:4]) for date in table]
    average_ages = sum(dates)//len(dates)
    average_age = now - average_ages
    print(average_age)
    view.get_input('\nBack to menu press Enter')
    os.system('clear')
    



def next_birthdays():
    os.system('clear')
    view.print_message('--------------------------------')
    view.print_message(' Next Birthdays within 14 days')
    view.print_message('--------------------------------\n')  
    table = hr.list_employees()
    given_date = view.get_input('\nDate: YYYY-MM-DD  >  ')
    os.system('clear')
    view.print_message('--------------------------------')
    view.print_message(' Next Birthdays within 14 days')
    view.print_message('--------------------------------\n') 
    view.print_message(f'Given date : {given_date}\n')
    birthday_in_two_weeks = hr.birthday_in_two_weeks(given_date, table)
    # print(date)
    if len(birthday_in_two_weeks) == 0:
        view.print_message(" There's no birthdays in two weeks to date!")
    else:
        view.print_message(f'{", ".join(birthday_in_two_weeks)}')
    view.get_input('\nBack to menu press Enter')
    os.system('clear')
    
 


def count_employees_with_clearance():
    os.system('clear')
    view.print_message('----------------------------------------')
    view.print_message(' Employees with at least clearance level')
    view.print_message('----------------------------------------\n')  
    clearence_input = view.get_input("Clearence level > ")
    table = hr.list_employees()
    number_of_employees = hr.clearence_and_above(table, clearence_input)
    view.print_message(number_of_employees)
    view.get_input('\nBack to menu press Enter')
    os.system('clear')




def count_employees_per_department():
    os.system('clear')
    view.print_message('---------------')
    view.print_message(' Departments')
    view.print_message('---------------\n')  
    table = hr.list_employees()
    print(hr.employees_by_department(table))
    view.get_input('\nBack to menu press Enter')
    os.system('clear')
    


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
    os.system('clear')
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
            operation = view.get_input("Select an operation > ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)


