

from helper_methods import *
# need to create a function that takes in
# a filename for a destination config table
# a folder name is given.
# uncomment the column name rows to be used in the loadCsv config
import csv
import sys





def dumpfile(folder, table_name):
    ''' takes in a path to table
        SQLalchemy class must have same name as the .py
        (to import the object from the file)
        config directory required in model'''
    table = get_table_scope(folder, table_name)
    try:
        outfile = open(folder+"/config"+"/"+table_name+".csv", 'w')
    except IOError:
        print "please make a config directory inside the given models folder"
        return
    outcsv = csv.writer(outfile)
    records = table.query.all()
    outcsv.writerow([column.name for column in table.__mapper__.columns])
    # can extend this function to check for 'id' name
    [outcsv.writerow([getattr(record, column.name) for column in
                      table.__mapper__.columns]) for record in records]
    outfile.close()


def dump_folder(folder):
    '''uses the __init__.py as an index for the databases to save
     in the models folder'''

    print "saving data from: " + folder + "/__init__.py\n"
    imports = Load_Data(folder + "/__init__.py", " ")
    tables = [x[1] for x in imports]
    for table_name in tables:
        dumpfile(folder, table_name)
    return


if __name__ == '__main__':
    try:
        dump_folder(sys.argv[1])
    except IndexError:
        print "please pass in the name of the model folder as an argument.\
         eg: appfolder/models"
    finally:
        print "\nsuccess\n"
