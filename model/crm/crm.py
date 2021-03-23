""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""
import sys, os
sys.path.append(os.getcwd()) 
from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

def add_customer(table):
    data_manager.write_table_to_file(DATAFILE, table, separator=';')


def list_customers():
    table = data_manager.read_table_from_file(DATAFILE)
    return table

print(list_customers())
