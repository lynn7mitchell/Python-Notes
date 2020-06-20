#Data Types

# int
print(type(2*4))

  # to the power of 3
print(2 ** 3)
  
  #rounded down to integer
print(2 // 3)
print (5 // 4)

  #modulo gets remainder
print(6 % 4)






# float
print(type(2*4.1))




#math functions
print(round(3.1))

#returns absolute value (no negative)
print(abs(-20))

#complex data type
print(bin(5))

#take binary number and make it an integer. the binary is base 2. 0b is just how python says it's binary. binary of 5 is 101
print(int('0b101', 2))





# bool
is_logged_in = True





# str
string = 'this is a string'

long_string = '''

asdfjasdf

this is a long string

'''

print(string)
print(long_string)

#str is .toString
print(str(100))
print(type(str(100)))

#escape sequences
print("stuff and 'things' ")
print("It\'s \"weird\"")
print("\t tabed over")
print("new\nline")

# formatted strings

name = 'Name Namerson'
age = 76

# putting f before the string formats it
print(f'Sup {name} you are {age} and look like a rubber glove got caught in a lawn mower')

# python2 version
print('Sup {} you are {} and look like a rubber glove got caught in a lawn mower'.format(name, age))

# string index includes spaces
selfish = 'me me me'
          #01234567
print(selfish[0])
#[start : stop : stepover(by how many spaces)]
print(selfish[0:8:2])
print(selfish[-1])
#reverse order
print(selfish [::-1])

# you can reassign an entire string but not just part of iter

# selfish = 100 (will work)
# selfish[2] = '8' (will not work)

# len starts at 1 instead of 0
print(len(selfish))

quote = 'stuff and other things'
print(quote.upper())
print(quote.capitalize())
print(quote.find('and'))
print(quote.replace('and', 'but'))



# list (array)
li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = ['a', 1, False]

print(li3[0])

# list slicing
#same as slicing strings
print(li3[0::2])

li[0] = 4

print(li)
# len is length that starts at 1
print(len(li))

li.append(9)

print(f'appened li {li}')


# inserts 7 at index of 4
li.insert(2, 7)
print(f'7 added at index 4 in li {li}')

#li.extend is like push (adds at end)

#remove using .pop() (delete at the end or pass index as an argument)

# .pop() returns the number is removes

# .remove() takes value that you want remove (find value and delete)

# .remove() returns None

# .clear() removes everything from  a list

# .index() takes a value start and stop. finds the index of the value you are looking for. you can make it look between 2 indexes with the start and stop parameters

#the 'in' keyword
#the print below is basically asking is 5 in li_in and returns true or false
li_in = [1,2,3,4,5,6,7,8,2]
print(5 in li_in)

# .count() searches for the parameter given to see how many times it occurs in whatever the method is called open

print(li_in.count(2))

li_sort = [2,5,1,4,8,3]
# .sort sorts a list
print(li_sort.sort())

# sort() creates a new list
print(sorted(li_sort))

# .copy will copy a li

# .reverse will reverse the array as is (not sort then reverse)

# copy new li
li4 = li3[:]

# starts at 1
print(list(range(1, 100)))

# starts at 0
print(list(range(100)))

li_join = ['hello', 'person']

# joins but adds spaces
new_li = ' '.join(li_join)

print(new_li)

# list unpacking

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other)
print(d)




# Matrix
matrix2d = [
  [1,2,3],
  [4,5,6]
]

print(matrix2d[0][2])

matrix3d = [
  [1,[7,8,9],2,3],
  [4,5,6]
]

print(matrix3d[0][1][2])





# None is a value






#dict

# Dictonary (object)
# dictionaries are unordered in memory.
#dictionary keys need to be immutable (cannot be changed)
test = {
  'a': 1,
  'stuff': 'things',
  'x': True,
  'w': [1,2,3]
}
print(test['stuff'])

# age does not exist but wont give an error because of .get() this will return none
print(test.get('age'))

#you can set a default value in .get()
print(test.get('age', 34))

#this way is never used
user = dict(name = 'person')

print(user)


print('x' in test) #true

print('x' in user.keys()) #true

print('x' in user.values()) #false

print(test.items()) #creates a list

# change
test['w'] = [3,5,4]
# add
test['z'] = 'added'


#test.clear() clears the dictionary
#test.copy will copy the dictionary
#test.pop('x')
#test.popitem() randomly returns a key and value
test.popitem()

#.update
test.update({'x' : False})
print(test)


# tuple
# a tuple is an immutable list
my_tuple = (1,2,3,4,5)



# set
# unordered collection of UNIQUE objects
# no duplicate values
my_set = {1,2,3,4,5}
my_set.add(100)
my_set.add(2)
print(my_set)

my_list = [1,2,3,4,5,5,2]
# set() changes to a set
print(set(my_list))

#sets cannot be indexed you have to grab specific values like a dictionary

new_set = {1,2,3,4,5,6}
other_set = {4,5,3,1,58,25,6,7}

#discard
print(new_set.difference(other_set))

print(my_set.discard(5))



