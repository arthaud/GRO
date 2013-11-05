#!/usr/bin/python2
# -*- coding: utf-8 -*-

def carre_magique(n):
    '''
    Retourne un carré magique d'ordre n
    '''
    assert n >= 3
    if n % 2 == 0:
        return carre_magique_pair(n)
    else:
        return carre_magique_impair(n)

def carre_magique_impair(n):
    '''
    http://fr.wikipedia.org/wiki/Carr%C3%A9_magique_%28math%C3%A9matiques%29#Ordre_impair
    '''
    assert n % 2 == 1
    m = n // 2
    matrice = [[None] * n for _ in range(n)]

    i = 1
    for x in range(n-1, -1, -1):
        y = n - x - 1
        for j in range(n):
            if x+j < n // 2:
                matrice[x+j+n-m][y+j-m] = i
            elif x+j >= n + n // 2:
                matrice[x+j-n-m][y+j-m] = i
            elif y+j < n // 2:
                matrice[x+j-m][y+j+n-m] = i
            elif y+j >= n + n // 2:
                matrice[x+j-m][y+j-n-m] = i
            else:
                matrice[x+j-m][y+j-m] = i

            i += 1

    return matrice

def carre_magique_pair(n):
    assert n % 2 == 0
    if n % 4 == 0:
        return carre_magique_pairement_pair(n)
    else:
        return carre_magique_pairement_impair(n)

def carre_magique_pairement_pair(n):
    '''
    http://fr.wikipedia.org/wiki/Carr%C3%A9_magique_%28math%C3%A9matiques%29#M.C3.A9thode_des_permutations_autour_des_diagonales
    '''
    assert n % 4 == 0
    matrice = [[None] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            rel_x, rel_y = x % 4, y % 4 # Position relative dans le carré 4*4
            if (rel_x, rel_y) in ((1,0), (2,0), (0,1), (0,2), (3,1), (3,2), (1,3), (2,3)):
                matrice[x][y] = n*n + 1 - (x + n*y + 1)
            else:
                matrice[x][y] = x + n*y + 1

    return matrice

def carre_magique_pairement_impair(n):
    '''
    http://fr.wikipedia.org/wiki/M%C3%A9thode_LUX_de_Conway_pour_les_carr%C3%A9s_magiques
    '''
    assert n % 4 == 2
    m = (n - 2) // 4

    lux = [['L'] * (2*m + 1) for _ in range(m+1)]
    lux.append(['U'] * (2*m + 1))
    lux += [['X'] * (2*m + 1) for _ in range(m-1)]

    # Echange L et U
    lux[m][m] = 'U'
    lux[m+1][m] = 'L'

    matrice = [[None] * n for _ in range(n)]

    x, y = m, 0
    i = 1
    while True:
        # Marquage
        real_x, real_y = x * 2, y * 2

        if lux[y][x] == 'L':
            matrice[real_y][real_x+1] = i
            i += 1
            matrice[real_y+1][real_x] = i
            i += 1
            matrice[real_y+1][real_x+1] = i
            i += 1
            matrice[real_y][real_x] = i
            i += 1
        elif lux[y][x] == 'U':
            matrice[real_y][real_x] = i
            i += 1
            matrice[real_y+1][real_x] = i
            i += 1
            matrice[real_y+1][real_x+1] = i
            i += 1
            matrice[real_y][real_x+1] = i
            i += 1
        else: # == 'X'
            matrice[real_y][real_x] = i
            i += 1
            matrice[real_y+1][real_x+1] = i
            i += 1
            matrice[real_y+1][real_x] = i
            i += 1
            matrice[real_y][real_x+1] = i
            i += 1

        # Méthode de Siam
        old_x, old_y = x, y
        x, y = x+1, y-1

        if x >= 2*m + 1:
            x = 0
        if y < 0:
            y = 2*m

        if matrice[y*2][x*2] is not None:
            x = old_x
            y = old_y + 1

        if y >= 2*m + 1 or matrice[y*2][x*2] is not None:
            break

    return matrice
