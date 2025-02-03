import numpy as np
class Cercle :
    def __init__(self, rayon) :
        self.rayon = rayon

    def changerRayon(self, new_r) :
        self.rayon = new_r
        print(f"Le nouvrau rayon est : {self.rayon}")

    def circonférence(self) :
        return 2 * np.pi * self.rayon
    
    def diametre(self) :
        return 2 * self.rayon

    def aire(self) :
        return np.pi * self.rayon**2
    
    def afficherInfo(self) :
        print(f"La forme géométrique est : cercle")
        print(f"Le rayon r = {self.rayon} cm")
        print(f"Le diamètre du cercle est D = {2 * self.rayon} cm")
        print(f"La circonférence du cercle est P = {2 * np.pi * self.rayon} cm")
        print(f"L'aire du cercle est A = {np.pi * self.rayon**2} cm²")

#Instanciation : Creation of the objects
print(f"\nPour le premier cercle :")
cercle1 = Cercle(4)      
cercle1.afficherInfo()
cercle1.diametre()
cercle1.circonférence()
print(f"\nPour le deuxième cercle :")
cercle2 = Cercle(7)      
cercle2.afficherInfo()
cercle2.diametre()
cercle2.circonférence()
cercle2.aire()