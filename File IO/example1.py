my_file = open('File IO/test.txt')

print(my_file.read())
# print will only run once. The file goes through like a cursor until it ends
# the cursor stays at the end
print(my_file.read())
# this moves the cursor back to the index of 0
my_file.seek(0)
# this will run again because the cursor is at the start of the file
print(my_file.read())

my_file.seek(0)

# reads whatever line the cursor is on
print(my_file.readline())

my_file.seek(0)

# creates a list of lines
print(my_file.readlines())

# you have to close the file to use it elsewhere
my_file.close()