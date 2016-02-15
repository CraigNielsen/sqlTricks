from myCMDapp import db
from myCMDapp.models.Customer import Customer
from myCMDapp.models.Product import Product
from myCMDapp.models.Basket import Basket
from helper_methods import *
from loadDBConfig import *

if __name__ == '__main__':
    user = Customer.query.first()
    
#     product = BasketHasProduct.query(BasketHasProduct.basket_basketID == '1')
    print user.basket[0].tags
    