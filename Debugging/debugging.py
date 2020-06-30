#debugging
import pdb

def add(num1, num2):
    # this will stop the code at whatever line it's on and let you ask what different parameters and variables are
    # you can type help in pdb to see all the commands
    # c command to close and not ctrl+c
    pdb.set_trace()
    return num1 + num2
add(4, 'asdfasdf')