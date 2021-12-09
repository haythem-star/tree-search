import numpy as np
from JeuTaquin import JeuTraquin
from Noeud import Noeud


arr = np.array([[7,2,4],[5,0,6],[8,1,3]])
arr2 = np.array([[2,3],[1,0]])
# noeud = Noeud(arr,0,3)
# print(arr)
# print(noeud.movesPosssiples)


jeu = JeuTraquin(2,arr2)

result = jeu.RechercheEnProfondeurDabord()


if(not result):
    print('etat final ne peut pas etre attend')
else:
    print('Etat final trouvé')
    print(result.etat)
    print('cout de recherche = {}'.format(result.cout))
    print('noeud sauvegardé en mémoire = {} '.format(len(jeu.ouverts)+ len(jeu.fermés)+1))


# arr3=None
# print(arr is not None)



# arr = np.array([[1,2,3,4],[9,8,7,6],[0,1,4,7]])
#
# arr2 = ['a','b','c','d']
#
# res = np.where(arr == 4)
#
# print(arr2.index('f'))
#
# if(len(arr2) == 0):
#     print('arr2 is empty')
