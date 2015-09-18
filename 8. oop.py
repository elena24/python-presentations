class Animal:
    
    __color = "Blue"
    
    def __init__(self, age):
        self.age = age
    
    def printDescription(self, name):
        
        return "This is an animal " + name + " age: ", self.age
    
    def getColor(self):
        return self.__color
    
    def setColor(self, newColor):
        self.__color = newColor
        
        
class Dog(Animal):
    
    def __init__(self, age):
        self.age = age
    
    def printDescription(self, name):
        return "This is a " + name + " age: " + str(self.age)

myAnimal = Animal(4)
print(myAnimal.age)
print(myAnimal.printDescription("Animal"))

myAnimal.age = 3
print(myAnimal.age)

print(myAnimal.getColor())
myAnimal.setColor("red")
print(myAnimal.getColor())

dog = Dog(3)
print(dog.printDescription("dog"))