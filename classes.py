# OOP
# Classes

# Classes are camelcase
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
    
    # you have to add cls when you create a class method (not used often)
    @classmethod
    def adding_things(cls, num1, num2):
        # cls() instantiates the class PlayerCharacter with the name of Smitche and the age of the sum of num1 + num2
         return cls('Smitche', num1 + num2)

    # staticmethod is the same thing as classmethod except you don't have the cls parameter
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

   


player1 = PlayerCharacter('Ace', 23)
player2 = PlayerCharacter('Ash', 24)
player3 = PlayerCharacter.adding_things(2,10)
# added attack attribute to player2 only
player2.attack = 50

print(player1.run())
print(player1.name, player1.age)
print(player2.name, player2.age)
print(player3.name, player3.age)


print(player2.attack)

print(player1.shout())




