# when you import a file in python it runs the code in the file it's importing so they're in memory
import utility
from shopping import shopping_cart
from utility import *

import built_in_modules


print(shopping_cart.buy('apple'))
print(multiply(10,20))
print(divide(4,2))

# __main__ is given to the file that you run
# print(__name__)

if __name__ == '__main__':
    print('please run this')