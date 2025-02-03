#jobs 1, 2 and 3
#create the class :
class Operation :
    def __init__(self, nombre1, nombre2): #create the constructor
        self.nombre1 = nombre1   #initialize the attributes 
        self.nombre2 = nombre2

    def addition(self) :
        return self.nombre1 + self.nombre2

#Create the objects
operation1 =Operation(1, 2) 
print(operation1)   #print the object
#it will print the object : <__main__.Operation object at 0x000001C83E597AD0>, that means :
# __main__ : the module where the class is defined
#Operation : the name of the class
#0x000001C83E597AD0 : the memory adress