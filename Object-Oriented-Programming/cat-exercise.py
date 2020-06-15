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