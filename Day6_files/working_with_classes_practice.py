 # a class allows you to define a data structure and methods   
class dog:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

# instantiate the class and provide it some variables
my_dog = dog('corgi', 'rogue', 3)

# it looks similar to accessing an object in powershell  object.subobject property
print(my_dog.breed)
print(my_dog.name)
print(my_dog.age)

#------------------------------------------

# lets try our dog class with a method to show if its been walked and if its been fed

class cooler_dog:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
    
    def walked(self):
        print("Hoomman! I " + self.name +  " the wonderful " + self.breed + " have been walked")

    def fed(self):
        print("Hooman! I " + self.name +  " the wonderful " + self.breed + " have been fed! feed me more")

# intantiate the class and provide it some variables
my_dog = cooler_dog('corgi', 'rogue', 3)

# tryout the internal method for walked on the object
my_dog.walked()

# try out the internal method for fed on the object
my_dog.fed()       

