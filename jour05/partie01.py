class Part :
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material) :
        self.material = new_material
        return self.material
    
    def __str__(self):
        return f"Nom_pièce = {self.name}\nMateriau = {self.material}"
    
