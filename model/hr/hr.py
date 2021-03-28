""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""
import sys, os
sys.path.append(os.getcwd())
from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def list_employees():
    table = data_manager.read_table_from_file(DATAFILE)
    return table


def add_employee_data(new_data):
    table = data_manager.read_table_from_file(DATAFILE, separator=';')
    i_d = util.generate_id()
    new_data.insert(0, i_d)
    new_table = table + [new_data]
    data_manager.write_table_to_file(DATAFILE, new_table)
    return new_table


def update_employee(table):
    data_manager.write_table_to_file(DATAFILE, table)

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def days_counter_to_date_year(given_date):
    date_year = int(given_date[0:4])
    reference_year = 1900
    days_counter = 0
    for year in range(reference_year, date_year):
        if is_leap_year(year) is True:
            days_counter += 366
        else:
            days_counter += 365
    return days_counter


def date_year_days(given_date):
    year = int(given_date[0:4])
    month = int(given_date[5:7])
    day = int(given_date[-2:])
    simple_year_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]
    leap_year_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]
    date_year_day = 0
    if is_leap_year(year) is True:
        if month == 1:
            date_year_day = day
        if month == 2:
            date_year_day = leap_year_months[0] + day
        if month > 2:
            date_year_day = sum(leap_year_months[0: month-1]) + day
    else:
        if month == 1:
            date_year_day = day
        if month == 2:
            date_year_day = simple_year_months[0] + day
        if month > 2:
            date_year_day = sum(simple_year_months[0: month-1]) + day
    return date_year_day


def all_days(date):
    all_day = days_counter_to_date_year(date) + date_year_days(date)
    return all_day


def present_year_birthday(birth_date, given_date):
    present_birthday = f"{given_date[0:4]}-{birth_date[5:]}"
    return present_birthday


def birthday_in_two_weeks(given_date, table):
    names_list = []
    if is_leap_year(int(given_date[0:4])) is True:
        year = 366
    else:
        year = 365
    for lst in table:
        birth_date = lst[2]
        if 0 <= (all_days(present_year_birthday(birth_date, given_date)) - all_days(given_date)) % year <= 14:
            names_list.append(lst[1])
    return names_list

 
def clearence_and_above(table, label):
    number_of_employees = 0
    
    for lst in table:
        if lst[-1] >= label:
            number_of_employees += 1
    return number_of_employees
        
        
def employees_by_department(table):
    employees = {}
    for lst in table:
        if lst[-2] in employees.keys():
            employees[lst[-2]] += 1
        else:
            employees[lst[-2]] = 1
    return employees
       