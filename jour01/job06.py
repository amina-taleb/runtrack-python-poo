class Animal :
    def __init__(self, age = 0, prenom = ''):  
        self.age = age #initialise the values
        self.prenom = prenom

    def vieillir(self) :
        self.age += 1

    def nommer(self, nom) :
        print(f"L'animal se nomme {nom}")
    
animal1 = Animal(0)  #we can associalte only one attribute
print(f"L'age de l'animal {animal1.age} ans")
animal1.vieillir()  #we call the method "vieillir"
print(f"L'age de l'animal {animal1.age} ans")
animal1.nommer('Luna')

#Note : when we initialise the attributes at 0 or an empty chain, when we instanciate the class, we can cal only one attribute for the object.