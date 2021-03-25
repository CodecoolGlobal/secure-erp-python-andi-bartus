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



def days_calculator(date):
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[-2:])
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]
    leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]
    if is_leap_year(year) is True:
        days = sum(leap_months[0:month-1]) + day
    else:
        days = sum(months[0:month -1]) + day       
    return days

def next_birthday(given_date, table):
    given_year = int(given_date[0:4])
    given_date_days = days_calculator(given_date)
    birthdays = [item[2] for item in table]
    result1 = []
    result2 = []
    for date in birthdays:             
        birth_days = days_calculator(date)
        diff =  birth_days - given_date_days
        
        if birth_days <= 13:
            given_date_days = given_date_days + birth_days   
            if given_date_days - given_year <= 14:
                result1.append(date)
                result = result1
            
        else:
            if diff <= 14 and diff >= 0:
                result2.append(date)
                result = result2
    return result

 
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
       