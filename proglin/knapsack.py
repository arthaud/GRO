#!/usr/bin/python
# -*- coding: UTF-8 -*-

def knapsack(objects, max_mass):
    """
    Résout le problème du sac à dos avec de la programmation dynamique.
    Fonctionne seulement avec des valeurs entières.

    objects est une liste de couples (masse, prix) représentant les objets.
    """
    assert isinstance(max_mass, int) and all(isinstance(x[0], int) for x in objects)

    current_line = [0 for i in range(max_mass+1)]
    prev_line = current_line[:]

    for i in range(0,len(objects)):
        object_mass, price = objects[i]
        for masse in range(max_mass + 1):
            if object_mass <= masse:
                current_line[masse] = max(prev_line[masse], prev_line[masse-object_mass] + price)
            else:
                current_line[masse] = prev_line[masse]

        prev_line = current_line[:]

    return current_line[max_mass]

def best_ratio(x): return x[1]/x[0]
def worst_mass(x):  return -x[0]
def best_price(x): return x[1]

def greedy(objects, max_mass, key):
    """
        Algorithme approché du glouton.
        Nécessite de trier les objets selon un critère `key'.
        Par exemple
            greedy(obj, max_mass, worst_mass)
        choisit les objets en commençant par les moins lourds.
    """
    cost, mass = 0, 0
    objects = sorted(objects, key=key, reverse=True)

    for o in objects:
        if o[0] + mass <= max_mass:
            mass += o[0]
            cost += o[1]

            if mass == max_mass:
                break

    return cost

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

