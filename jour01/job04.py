#create the class : 
class Personne :
    def __init__(self, nom, prenom) :  #create the constructor
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self) :  #Create the method
        return print(f"Je suis {self.nom} {self.prenom}")
    
#Instanciate the class and cal the methods :
personne1 = Personne('John', 'Doe')
personne1.SePresenter()
personne2 = Personne('Jean', 'Dupond')
personne2.SePresenter()

