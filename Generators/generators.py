#Generators

# Generators don't take up space in memory
# Generators are iterable

# Range is a generator
# list(range(100))

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list = make_list(100)
# print(my_list)

def generator_function(num):
    for i in range(num):
        # yield pauses the function and comes back to it when you do something to it
        yield i

for item in generator_function(1000):
    print(item)