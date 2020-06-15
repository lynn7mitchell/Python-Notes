#OOP
#Classes

class PlayerCharacter:
    # __init__ is a magic method or a constructor
    # this means you have to give the argument for name
    #'self' is similar to 'this' in js 
    def __init__(self, name, age):
        self.name = name
        self.age = age

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