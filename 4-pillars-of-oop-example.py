# 4 pillars of OOP
#encapsulation sign_in is encapsulated in the user class
#abstraction use the data and don't try to understand it
#inheritance line 10
#polymorphism line 42

class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

# Wizard inherited the User class' data i.e. the sign_in function
class Wizard(User):
    def __init__(self, name, power, email):
        # grabs the user function for email
        User.__init__(self, email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows, email):
        # grabs the user function for email using super() which does not require self
        super().__init__(email)        
        self.name = name
        self.arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: {self.arrows} arrows left ')

# multiple inheritance
class HybridBorg(Wizard, Archer):
    pass

wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('Robin', 100, 'archer@gmail.com')
hb1 = HybridBorg('Boris', 37, 'borgie@gmail.com')

wizard1.attack()
archer1.attack()
hb1.attack()
# print(wizard1.sign_in())

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
# top level class is called object in python
print(isinstance(wizard1, object))


# polymorphism
#the same method is used but the output is changed due to the object it is used on
def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()


print(wizard1.email)


#introspection
# print(dir(wizard1))