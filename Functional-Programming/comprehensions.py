#list comprehension

#list, set, dictionary

my_list = [char for char in 'hello']

my_list2 = [num for num in range(0,100)]

my_list3 = [num*2 for num in range(0,100)]
# loop through 0 - 100 and make it to the power of 2 and then if it an odd don't keep it
my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]
# for char in 'hello':
#     my_list.append(char)

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)


#set comprehension

my_set = {char for char in 'hello'}

print(my_set)


#dictionary comprehension
simple_dict = {
    'a': 1,
    'b': 2
}
# what you want to do with it key:value**2

my_dict = {key:value**2 for key, value in simple_dict.items() if value % 2 ==0}

print(my_dict)