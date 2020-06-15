#use def to define a function
def say_hello():
  print('hello')

say_hello()

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show_tree():
  for li in picture:
    for item in li:
      # if item == 1
      # 1 is truthy
      if(item):
        print('*', end="") #end with an empty string
      else:
        print(' ', end="")
    print('') #this adds a new line for every row
  



show_tree()
show_tree()

#paramaters

# default paramaters
def say_this_stuff(stuff="Kermit", things="Shikamaru"):
  # f means you can use the variables in the string
  print(f'{stuff} and {things}')

# positional arguments
say_this_stuff('whatnot', 'objects')

# keyword arguments
say_this_stuff(things='objects', stuff='whatnot')

# default paramaters example
say_this_stuff()

# a function should do one thing really well and should return something

def sum(num1, num2):
  # docstring
  '''
  Info: this function returns the sum of num1 and num2
  '''
    # without return it will give you 'None'

  return num1 + num2

total = sum(10,5)
print(sum(10, total))

# gets info about a function
help(sum)



# *args **kwargs

def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1,2,3,4))

# **kwargs is the same except its keyword arguments




# TESLA EXERCISE

def checkDriverAge(age):
  # age = input("What is your age?: ")

  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(36)

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.



#FUNCTIONS EXERCISE

# my solution
def highest_even(li):
    answer = 0
    for num in li:
      if num > answer and num % 2 == 0:
        answer = num
    return answer

print (highest_even([10,2,3,4,8,11,5,6,16]))


# teacher solution
def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_even([10,1,2,3,4,8]))