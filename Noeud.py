import numpy as np
class Noeud:
    movesPosssiples = []
    def __init__(self,etat,c,n,lastNode=None):
        self.lastNode = lastNode
        self.movesPosssiples = []
        self.etat = etat
        self.cout = c
        self.taille_taquin = n
        res = np.where(etat == 0)
        if (res[0][0] != 0):
            self.movesPosssiples.append('haut')
        if (res[0][0] != n - 1):
            self.movesPosssiples.append('bas')
        if (res[1][0] != 0):
            self.movesPosssiples.append('gauche')
        if (res[1][0] != n - 1):
            self.movesPosssiples.append('droite')