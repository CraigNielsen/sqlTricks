
from time import time
from sqlalchemy.orm import sessionmaker
import sys
from myCMDapp import db
from helper_methods import *
# 1 need to add records into a table defined by the filename
# (ie: the User would be equal to filename (name of table))
# 2 the number of records will be defined by the names in
# the first row of the input csv
# 3 the first line should not be read
# 4 the db should only drop the table that it is working on,
# then create that one again. defined by filenam
# 5 - account for first column required as primary key
# at moment, it is assumed first column is auto created.. :/




def load_file(folder, table_name):
    table = get_table_scope(folder, table_name)
    # db.drop_all()
    # db.create_all()
    # Create the session
    # need an init function for each table (or a loop here, i prefer init)
    session = sessionmaker()
    session.configure(bind=db.engine)
    s = session()
    try:
        data = Load_Data(folder+"/config/"+table_name+".csv", ',')
        data.pop(0)  # rid of table names
        print data
        for row in data:
            record = table(*row[0:])
            s.add(record)
        s.commit()      # Attempt to commit all the records
        print "committed " + table_name + " successfully"
    except Exception as inst:
        s.rollback()    # Rollback the changes on error
        print inst
    finally:
        s.close()       # Close the connection


def load_model_config(folder_name):
    print "loading data from: " + folder_name + "/__init__.py\n"
    imports = Load_Data(folder_name + "/__init__.py", " ")
    tables = [x[1] for x in imports]
    for table_name in tables:
        load_file(folder_name, table_name)

if __name__ == "__main__":
    '''uses the __init__.py as an index for the databases
        in the models folder. The config folder will be used
        to load configuration for the tables defined in __init__py'''
    t = time()
    user_input = raw_input("This will destroy the current database config: \n\
        are you sure you want to continue? Y or N?")
    if user_input.upper() != "Y":
        print "stopping operation"
        sys.exit()
    db.drop_all()
    db.create_all()
    folder_name = sys.argv[1]
    load_model_config(folder_name)
    print "Time elapsed: " + str(time() - t) + " s."  # 0.091s
