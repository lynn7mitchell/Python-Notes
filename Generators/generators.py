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


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_for([1,2,3])

# from time import time
# def performance(fn):
#     def wrapper(*args, **kawrgs):
#         t1 = time()
#         result = fn(*args, **kawrgs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper

# @performance
# def long_time():
#     # this is faster since it isn't looping over a list. 
#     #  even if it is not even a second of difference think about it at a larger scale like Google
#     print('1')
#     for i in range(10000000):
#         i*5
# @performance
# def long_time2():
#     print('2')
#     for i in list(range(10000000)):
#         i*5


# long_time()
# long_time2()