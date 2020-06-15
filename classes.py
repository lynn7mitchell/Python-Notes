# OOP
# Classes

class PlayerCharacter:
    # Class Object Attribute
    membership = True

    # __init__ is a magic method or a constructor
    # this means you have to give the argument for name
    # 'self' is similar to 'this' in js
    def __init__(self, name='anonymous', age=0):
        if(PlayerCharacter.membership):
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')
        return 'done shouting'

    def run(self):
        print('run')
        return 'done running'


player1 = PlayerCharacter('Ace', 23)
player2 = PlayerCharacter('Ash', 24)

# added attack attribute to player2 only
player2.attack = 50

print(player1.run())
print(player1.name, player1.age)
print(player2.name, player2.age)


print(player2.attack)

print(player1.shout())



#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
kaliki = Cat('Kaliki', 3)
toby = Cat('Toby', 5)
kraz = Cat('Kraz', 4)


# 2 Create a function that finds the oldest cat
def oldestCat(*cats):
    highestAge = 0
    for cat in cats:
        if(cat.age > highestAge):
            highestAge = cat.age
    return highestAge
        
# Solution
# def get_oldest_cat(*args):
#     return max(args)
    
oldestCat(kaliki, toby, kraz)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldestCat(kaliki, toby, kraz)} years old.")