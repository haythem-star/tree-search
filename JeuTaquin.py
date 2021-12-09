import numpy as np
from Noeud import Noeud

class JeuTraquin:
    ouverts = []
    fermés = []
    logFile = open('logFile.txt', 'w')

    def __init__(self,n,etatInitial):
        self.taille_taquin = n
        self.logFile.write('état Initial : \n')
        writeEtat(self.logFile,etatInitial,self.taille_taquin)
        self.logFile.write('#############################################\n')
        self.ouverts.append(Noeud(etatInitial,0,n))


    def RechercheEnLargerDabord(self):
        self.logFile.write('Recherche En Larger D abord\n .........\n')
        if(len(self.ouverts) == 0):
            afficheTrace(self.logFile,False,self.taille_taquin,self.ouverts,self.fermés)
            self.logFile.close()
            return False
        node = self.ouverts.pop(0)
        if (TestEtatFinal(self.taille_taquin,node.etat)):
            afficheTrace(self.logFile, True,self.taille_taquin,self.ouverts,self.fermés, node)
            self.logFile.close()
            return node
        self.fermés.append(node.etat)
        if('haut' in node.movesPosssiples):
            EtatHaut = DeplaceHaut(node.etat)
            if (not TestEtatRepeter(EtatHaut,self.fermés)):
                self.ouverts.append(Noeud(EtatHaut,node.cout+1,self.taille_taquin,node))
        if ('bas' in node.movesPosssiples):
            EtatBas = DeplaceBas(node.etat)
            if (not TestEtatRepeter(EtatBas, self.fermés)):
                self.ouverts.append(Noeud(EtatBas, node.cout + 1, self.taille_taquin,node))
        if ('gauche' in node.movesPosssiples):
            EtatGauche = DeplaceGauche(node.etat)
            if (not TestEtatRepeter(EtatGauche, self.fermés)):
                self.ouverts.append(Noeud(EtatGauche, node.cout + 1, self.taille_taquin,node))
        if ('droite' in node.movesPosssiples):
            EtatDroite = DeplaceDroite(node.etat)
            if (not TestEtatRepeter(EtatDroite, self.fermés)):
                self.ouverts.append(Noeud(EtatDroite, node.cout + 1, self.taille_taquin,node))
        print(len(self.ouverts))
        return self.RechercheEnLargerDabord()

    def RechercheEnProfondeurDabord(self):
        self.logFile.write('Recherche En Profondeur D abord\n .........\n')
        if(len(self.ouverts) == 0):
            afficheTrace(self.logFile, False,self.taille_taquin,self.ouverts,self.fermés)
            self.logFile.close()
            return False
        node = self.ouverts.pop(0)
        if (TestEtatFinal(self.taille_taquin,node.etat)):
            afficheTrace(self.logFile,True,self.taille_taquin,self.ouverts,self.fermés,node)
            self.logFile.close()
            return node
        self.fermés.append(node.etat)
        if('haut' in node.movesPosssiples):
            EtatHaut = DeplaceHaut(node.etat)
            if (not TestEtatRepeter(EtatHaut,self.fermés)):
                self.ouverts.insert(0,Noeud(EtatHaut,node.cout+1,self.taille_taquin,node))
        if ('bas' in node.movesPosssiples):
            EtatBas = DeplaceBas(node.etat)
            if (not TestEtatRepeter(EtatBas, self.fermés)):
                self.ouverts.insert(0,Noeud(EtatBas, node.cout + 1, self.taille_taquin,node))
        if ('gauche' in node.movesPosssiples):
            EtatGauche = DeplaceGauche(node.etat)
            if (not TestEtatRepeter(EtatGauche, self.fermés)):
                self.ouverts.insert(0,Noeud(EtatGauche, node.cout + 1, self.taille_taquin,node))
        if ('droite' in node.movesPosssiples):
            EtatDroite = DeplaceDroite(node.etat)
            if (not TestEtatRepeter(EtatDroite, self.fermés)):
                self.ouverts.insert(0,Noeud(EtatDroite, node.cout + 1, self.taille_taquin,node))
        print(len(self.ouverts))
        return self.RechercheEnProfondeurDabord()




def DeplaceHaut(etat):
    res =np.where(etat == 0)
    newEtat = np.copy(etat)
    row_trou = res[0][0]
    column_trou = res[1][0]
    row_tuile = res[0][0] - 1
    column_tuile = res[1][0]
    newEtat[row_trou][column_trou] = newEtat[row_tuile][column_tuile]
    newEtat[row_tuile][column_tuile] = 0
    return newEtat

def DeplaceBas(etat):
    res =np.where(etat == 0)
    newEtat = np.copy(etat)
    row_trou = res[0][0]
    column_trou = res[1][0]
    row_tuile = res[0][0] + 1
    column_tuile = res[1][0]
    newEtat[row_trou][column_trou] = newEtat[row_tuile][column_tuile]
    newEtat[row_tuile][column_tuile] = 0
    return newEtat

def DeplaceGauche(etat):
    res =np.where(etat == 0)
    newEtat = np.copy(etat)
    row_trou = res[0][0]
    column_trou = res[1][0]
    row_tuile = res[0][0]
    column_tuile = res[1][0] - 1
    newEtat[row_trou][column_trou] = newEtat[row_tuile][column_tuile]
    newEtat[row_tuile][column_tuile] = 0
    return newEtat

def DeplaceDroite(etat):
    res =np.where(etat == 0)
    newEtat = np.copy(etat)
    row_trou = res[0][0]
    column_trou = res[1][0]
    row_tuile = res[0][0]
    column_tuile = res[1][0] + 1
    newEtat[row_trou][column_trou] = newEtat[row_tuile][column_tuile]
    newEtat[row_tuile][column_tuile] = 0
    return newEtat

def TestEtatRepeter(etat,fermes):
    for i in fermes:
        if(np.array_equal(etat,i)):
            return True
    return False

def TestEtatFinal(n, etat):
    for i in range(n):
        for j in range(n):
            if(j == n-1):
                if(i < n-1):
                    if(etat[i+1][0] != 0):
                        if(etat[i][j] > etat[i+1][0]):
                            return False
                    else:
                        if(etat[i][j] > etat[i+1][1]):
                            return False
            else:
                if(etat[i][j+1] != 0):
                    if(etat[i][j] > etat[i][j+1]):
                        return False
                else:
                    if(j+1 == n-1):
                        if(i < n-1):
                            if (etat[i][j] > etat[i + 1][0]):
                                return False
                    else:
                        if(etat[i][j] > etat[i][j+2]):
                            return False
    return True

def afficheTrace(file,bool,n,ov,fer,node=None):
    file.write('resultat : ')
    if (bool):
        file.write('attend\n')
        print('parcourt\n')
        loopNode = node.lastNode
        while (loopNode is not None):
            writeEtat(file,loopNode.etat,n)
            loopNode=loopNode.lastNode
        file.write('\ncout de recherche = {}'.format(node.cout))
        file.write('\nnoeud sauvegardé en mémoire = {} '.format(len(ov) + len(fer) + 1))
    else:
        file.write('echec')

def writeEtat(file,etat,n):
    file.write('\n{ ')
    for i in range(n):
        for j in range(n):
            file.write(str(etat[i][j]))
            if(j != n-1):
                file.write(',')
        if (i != n-1):
            file.write('\n')
        else:
            file.write(' }\n')

# arr = np.array([[1,0,2],[4,5,8],[6,3,7]])
# print(arr)
# print(TestEtatFinal(3,arr))
# arr2 = np.array([[4,1,2],[6,0,5],[3,7,8]])
# print(arr)
# print(DeplaceHaut(arr2))
# print(np.array_equal(arr,DeplaceHaut(arr2)))
# print('origin')
# print(arr)
# print('deplace trou bas')
# print(DeplaceBas(arr))
# print('deplace trou Haut')
# print(DeplaceHaut(arr))
# print('deplace trou droite')
# print(DeplaceDroite(arr))
# print('deplace trou gauche')
# print(DeplaceGauche(arr))


