#import numpy as np   
# #I import this library in order to be able to create a matrix (to do later)

class Personnage :
    def __init__(self, x, y):  #the player is represented by (x, y) = (i, j) index coordinates
        self.x = x
        self.y = y  #This function returns the initial position of each player
    
    def gauche(self, dx) :  #plateau is a matrix 3 x 3
        self.x = self.x - dx   #dx is the displacement over x   (x is decreasing)
       #we choose the displacement and then we update the position over x axis
    def droite(self, dx) :
        self.x = self.x + dx   #x os increasing 

    def bas(self, dy) :
        self.y = self.y + dy

    def haut(self, dy) :
        self.y = self.y - dy

    def position(self) :
        print(f"La position actuelle du joeur est :{(self.x, self.y)}")

    #I want to add an other method, to find the player's position over a surface defined as :
    def plateau_jeu(self, plateau) :
        print(f"La position du joeur sur le plateau est :{plateau[self.x] [self.y]}")   #When we want to print a position from a matrix, we call matrix[i][j]

#instaciation :
#The initial position of the player is :
personnage1 = Personnage(0, 0) 
#For example, I want he go to the left by one step
personnage1.gauche(1)
personnage1.position()
plateau = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        
personnage1.plateau_jeu(plateau)