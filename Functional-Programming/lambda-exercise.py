
# lambda expressions
# a lambda experssion is a function that is only going to be used once
# lambda param: action(param)

# square
my_list = [5,4,3]

print(list(map(lambda item: item**2, my_list )))

# sort by the second item
a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key= lambda x: x[1])
print(a)