#créer la classe :
class Vehicule :
    def __init__(self, marque, modèle,année, prix):
        self.marque = marque 
        self.modèle = modèle
        self.année = année
        self.prix = prix
    
    def informationVehicule(self) :
        return f"Marque = {self.marque}\nModèle = {self.modèle}\nAnnées = {self.année}\nPrix = {self.prix}"
    

#créer  la sous classe :
class Voiture(Vehicule) :
    def __init__(self, marque, modèle, année, prix, portes = 4):
        super().__init__(marque, modèle, année, prix)
        self.portes = portes

    def informationVehicule(self) :
        return f"Marque = {self.marque} \nModèle = {self.modèle}\nAnnées = {self.année}\nPrix = {self.prix}\nNombre de porte = {self.portes}"
    
#instancier les objets :
voiture = Voiture('Mercedes', 'Classe A', 2020, 18500)
print(voiture.informationVehicule())