from partie01 import Part
class Ship(Part):
    def __init__(self, nom, parts = {}):
        self.nom = nom
        self.__parts = parts

    def get_dict(self) :
        return self.__parts
    
    def set_dict(self) :
        
        
