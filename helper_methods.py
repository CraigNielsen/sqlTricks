import importlib
import csv


def Load_Data(file_name, delimitr):
    datafile = open(file_name, 'r')
    datareader = csv.reader(datafile, delimiter=delimitr)
    data = []
    for row in datareader:
        data.append(row)
    # print data
    return data


def get_table_scope(folder, table_name):
    table_scope = importlib.import_module(
        ".".join(folder.split("/"))+"."+table_name)
    ref = getattr(table_scope, table_name)
    return ref
