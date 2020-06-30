import sys
import random

num1 = sys.argv[1]
num2 = sys.argv[2]
guess = sys.argv[3]

print(num1, num2, guess)


answer = random.randint(num1, num2)

if guess == answer:
    print("You are right!")
elif guess != answer:
      print("You are wrong")
    


# solution
# from random import randint
# # you will need to run this on your machine and not this website for the sys.argv to work!
# import sys

# answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# while True:
#     try:
#         guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
#         if  0 < guess < 11:
#             if guess == answer:
#                 print('you are a genius!')
#                 break
#         else:
#             print('hey bozo, I said 1~10')
#     except ValueError:
#         print('please enter a number')
#         continue