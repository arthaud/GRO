#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy

def sacados(objets, masse_max):
    """
    Résoud le problème du sac à dos avec de la programmation dynamique.
    Fonctionne seulement avec des valeurs entières.
    On pourrait optimiser l'algorithme en ne retenant que la ligne pour (i-1), et pas toute les lignes.

    >>> objets = ((2,3),(3,4),(4,5),(5,6))
    >>> sacados(objets, 5)
    7
    """
    assert isinstance(masse_max, int) and all(isinstance(x[0], int) for x in objets)

    matrice = numpy.zeros(shape=(len(objets)+1, masse_max+1), dtype='int64')

    for i in range(1,len(objets)+1):
        masse_objet, prix = objets[i-1]
        for masse in range(masse_max + 1):
            if masse_objet <= masse:
                matrice[i,masse] = max(matrice[i-1,masse], matrice[i-1,masse-masse_objet] + prix)
            else:
                matrice[i,masse] = matrice[i-1,masse]

    return matrice[len(objets)-1,masse_max]

def read_testfile(path):
    """
        Lit un fichier généré par le générateur trouvé ici:
            http://www.diku.dk/~pisinger/codes.html
        Retourne une liste de couples (masse, valeur) considérée comme bon
        exemple.
    """
    with open(path, 'r') as f:
        objects = []
        line = f.readline()
        nb_objs = int(line)
        for i in range(0, nb_objs):
            line = f.readline()
            dummy, a, b = map(int, line.split())
            objects.append((b, a))
        return objects

if __name__ == '__main__':
    import doctest
    doctest.testmod()

