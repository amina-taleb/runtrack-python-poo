class Livre :
    def __init__(self, titre, auteur, nombre_page):   #make the constructor
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_page = nombre_page

    def get_titre(self) :
        return self.__titre     #make the getters
    
    def get_auteur(self) :
        return self.__auteur
    
    def get_nb_page(self) :
        return self.__nombre_page
    
    def set_titre(self, new_titre) :   #make the setters
        self.__titre = new_titre
        return self.__titre
    
    def set_auteur(self, new_auteur) :
        self.__auteur = new_auteur
        return self.__auteur
    
    def set_nb_page(self, new_nb_page) :
        if new_nb_page > 0 :
            self.__nombre_page = new_nb_page
        return self.__nombre_page
    
livre = Livre('Maths', 'Amina', 100)
print(f"Le titre de ce livre est : {livre.get_titre()}")
print(f"L'auteur de ce livre est : {livre.get_auteur()}")
print(f"Le nombre de pages de ce livre est : {livre.get_nb_page()}")
livre.set_titre('Physique')
livre.set_auteur('Yannis')
livre.set_nb_page(80)
print(f"Le nouveau titre de ce livre est : {livre.get_titre()}")
print(f"Le nouvel auteur de ce livre est : {livre.get_auteur()}")
print(f"Le nouveau nombre de pages de ce livre est : {livre.get_nb_page()}")