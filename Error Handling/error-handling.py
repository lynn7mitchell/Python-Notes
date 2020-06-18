while True: 
    try:
        age = int(input('what is your age?'))
        10/age
        raise ValueError('hey...stop it')
    except ZeroDivisionError:
        print('please enter a number higher than 0')
        break
    else:
        print('thank you') 
        break
    # finally will print no matter what
    finally: 
        print('Mmmk, I am finally done')



def sum(num1, num2):
    try: 
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print('You done messed up' + err)

print(sum(1,'2'))

