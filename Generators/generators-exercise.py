def fib(num):
    num1 = 0
    num2 = 1

    for i in range(num):
        yield i
        temp = num1
        num1 = num2
        num2 = temp + num2

for x in fib(100):
    print(x)


def fib2(number):
    num1 = 0
    num2 = 1
    result = []
    for i in range(number):
        result.append(num1)
        temp = num1
        num1 = num2
        num2 = temp + num1
    return result

print(fib2(100))