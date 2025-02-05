class Rectangle :
    def __init__(self, longueur, largeur):  #create the constructor 
        self.__longueur = longueur
        self.__largeur = largeur  #make both attributes as private

    def get_largeur(self) :
        return self.__largeur    #create a getter for both attributes
   
    def get_longueur(self) :
        return self.__longueur 
    
    def set_largeur(self, new_largeur) :
        if new_largeur >= 0 :
            self.__largeur = new_largeur
        return self.__largeur
    
    def set_longueur(self, new_longueur) :
        if new_longueur >= 0 :
            self.__largeur = new_longueur
        return self.__longueur
    
rect = Rectangle(10, 5)
print(f"La longueur de ce rectangl est L = {rect.get_longueur()}")   #Have acces to the attribute values
print(f"La largeur de ce rectangle est l = {rect.get_largeur()}")
rect.set_longueur(6)    #modificate the attribute values
rect.set_largeur(2)
print(f"La nouvelle longueur de ce rectangl est L = {rect.get_longueur()}")   #Have acces to the new attribute values
print(f"La nouvelle largeur de ce rectangle est l = {rect.get_largeur()}")
