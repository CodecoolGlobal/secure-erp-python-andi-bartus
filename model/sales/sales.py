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
