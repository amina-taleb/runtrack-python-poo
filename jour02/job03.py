from job02 import Livre  #import the class Livvre

#In order to modificate the class in this file, I will use the concept of 'Héritage'
#I will create a new class (sous-class)
class NouveauLivre(Livre):
    def __init__(self, titre, auteur, nombre_page, disponible):  #create the constructor of the sous-classe
        super().__init__(titre, auteur, nombre_page)  #call the constructor of the main class
        self.__disponible = disponible #create a private attribute
    # we add or modificate the attribute in the sous-class

    def vérification(self) :
        if self.__disponible == True :
            return True
        else : 
            return False
        
    def emprunter(self) :  
        if self.__disponible == True :  #if the book is
            self.__disponible = False  #the book is not disponible
        return self.__disponible
       #### A refaire, tester sans utiliser l'attribut disponible

    def A_rendre(self) :
        if self.emprunter() :  #I call the method emprunter
            self.__disponible = False
            print(f"Il faut rendre ce livre")
        else :
            self.__disponible = True
            print(f"Le livre est disponible")
            

livre1 = NouveauLivre('Maths', 'Amina', 100, False)
print(livre1.vérification())
print(livre1.emprunter())
print(livre1.A_rendre())