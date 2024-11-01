class Cat: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    def sound(self): 
        return f"{self.name} says meow!" 
my_cat = Cat("black", 7)
print(my_cat.name)
print(my_cat.age)
print(my_cat.sound())