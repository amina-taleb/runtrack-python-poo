def change_part(self, part_name, new_material) :
    if part_name in self.__part :
        self.__part[part_name] = new_material
        print(f"La nouvelle piece est en {new_material}")
    else :
        print(f"La pièce n'existe pas")

#