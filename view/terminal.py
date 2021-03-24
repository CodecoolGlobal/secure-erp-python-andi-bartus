from colorama import*
init()

def print_menu(title, list_options, color):
    print(color +'\n----------------------------------')
    print('\n' + title + '\n')
    print('----------------------------------')
    for element in list_options:
        print(element + '\n')
    # for index in range(len(list_options))):
    #     print(f'({index + 1}), {list_options[index]}')   
    # print("(0) Exit program")


    """Prints options in standard menu format like this:
    print
    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    


def print_message(message):
    print(message)
 

def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def line_separator(row):
    line = "|"
    for i in range(len(row)):
        line += "------------------------------|"
    return line


def header(HEADERS):
    headers = HEADERS
    line = "|"
    for name in headers:
        line += f"  {name:<28}|"
    print(" /" + "-"*len(headers)*30 + " \\")
    print(line)
    print(line_separator(headers))


def get_printable_line(row):
    line = "|"
    for cell in row:
        line += f"  {cell:<28}|"
    return line


def print_table(table, HEADERS):
    header(HEADERS)
    for index in range(len(table)):
        print(get_printable_line(table[index]))
        if index == len(table)-1:
            print(" \\" + "------------------------------"*len(table[index]) + " /")
        else:
            print(line_separator(table[index]))


def get_input(label):
    option = input(label)
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return option


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    new_data = []
    for label in labels:
        get_label = input(label + ': ')
        new_data.append(get_label)
    return new_data


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    pass
