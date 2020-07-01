# read write append

# this way you don't have to close the file
# mode means it can only be read write or append. r = read w = write 
#  you can do r + w for read and write
try:
    with open('File IO/test.txt', mode='r+') as my_file:
        text = my_file.write('hey its me')
        print(my_file)
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO Error')
    raise err