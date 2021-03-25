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