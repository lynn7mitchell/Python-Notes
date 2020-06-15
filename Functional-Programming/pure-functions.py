# A pure function does not have side effects

# functools is a toolbelt that can be used for functional tools that comes with python
from functools import reduce


my_list = [1,2,3]
your_list = [10,20,30]

def multiply_by2(li):
    # new_list = []
    # for item in li:
    #     new_list.append(item*2)
    # return new_list
    return li*2

# print(multiply_by2(my_list))


# map
# map(action, data we want the action to take place on)
# map will loop through the list and then use the function multiply_by2 as the action
# list() turns it into a new list
print(list(map(multiply_by2, my_list)))


# FILTER
# filter(action, data we want the action to take place on)
def only_odd(item):
    # true or false
    return item % 2 != 0

# filter checks if the item is true or false, by using the action, and then adds the true to a new list
print(list(filter(only_odd, my_list)))


# ZIP
# zip takes to lists and puts them together in a tuple.
# [(mylist[0], your_list[0]), (mylist[1], your_list[1])], (mylist[2], your_list[2]) 

#IT CAN BE MORE THAN 2
print(list(zip(your_list, my_list)))


# REDUCE
def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 10))


print('The Original My List', my_list)
print('The Original Your List', your_list)

