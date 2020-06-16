from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} s')
        return result
    return wrapper

#Higher Order Function
# a function that encapsulates or returns another function
def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func


#Decorators


# func is hello 
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*******")
        func(*args, **kwargs)
        print("*******")        
    return wrap_func

@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)


hello('hello', ':)')


@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()