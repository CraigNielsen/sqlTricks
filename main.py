from myCMDapp import db
from myCMDapp.models import *
from helper_methods import *
from loadDBConfig import *

if __name__ == '__main__':
    t = time()
    user_input = raw_input("This will destroy the current database config: \n\
        are you sure you want to continue? Y or N?")
    if user_input.upper() != "Y":
        print "stopping operation"
        sys.exit()
    db.drop_all()
    db.create_all()
    folder_name = "myCMDapp/models"
    load_model_config(folder_name)
    print "Time elapsed: " + str(time() - t) + " s."  # 0.091s