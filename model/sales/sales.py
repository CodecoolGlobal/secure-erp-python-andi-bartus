""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""
import sys, os
sys.path.append(os.getcwd())
from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def list_transactions():
    table = data_manager.read_table_from_file(DATAFILE)
    return table


def add_transactions(new_data):
    table = data_manager.read_table_from_file(DATAFILE, separator=';')
    i_d = util.generate_id()
    new_data.insert(0, i_d)
    new_table = table + [new_data]
    data_manager.write_table_to_file(DATAFILE, new_table)
    return new_table


def update_transactions(table):
    data_manager.write_table_to_file(DATAFILE, table)


def find_dates_between(table, new_data):
    first_year = new_data[0]
    second_year = new_data[1]
    first_year = int(first_year.replace("-", ""))
    second_year = int(second_year.replace("-", ""))
    dates = [int(date[-1].replace("-", "")) for date in table]
    result = [date for date in dates if first_year <= date and second_year >= date]
    return result