class Point :
    def __init__(self, x, y): #x and y are the horizontal and vertical coordinates
        self.x = x
        self.y = y

    def afficherLesPoints(self) :
        return print(f"Les coordonnée de ce point sont ({self.x}; {self.y}) ")
    
    def afficherX(self) :
        return print(f"L'abcisse de ce point est : x = {self.x}")
    
    def afficherY(self) :
        return print(f"L'ordonnée de ce point est : y = {self.y}")
    
    def changerX(self, New_x) :
        self.x = New_x
        return print(f"La nouvelle valeur de x est : x_new = {self.x}")

    def changerY(self, New_y) :
        self.y = New_y
        return print(f"La nouvelle valeur de y est : y_new = {self.y}")

#instanciate the class :
pointA = Point(2, 3)
pointA.afficherLesPoints()
pointA.afficherX()
pointA.afficherY()     #
pointA.changerX(4)
pointA.changerY(6)