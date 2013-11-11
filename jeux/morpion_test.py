#!/usr/bin/python2
# -*- coding: utf-8 -*-

import morpion_strategies
import morpion
import sys
import numpy

def get_strategies():
    """
    Retourne toutes les stratégies disponibles, à l'exception de la stratégie humaine
    """
    return map(lambda f : getattr(morpion_strategies, f),filter(lambda f : f.startswith('strat') and f != 'strat_humain', dir(morpion_strategies)))

if __name__ == '__main__':
    strats = get_strategies()
    output = open(sys.argv[1], 'w')
    tailles = [3, 4, 5, ]#10, 50]
    temps = [[] for i in range(len(strats))] # temps des différentes stratégies pour jouer un coup

    for i, strat in enumerate(strats):
        for j, opponent in enumerate(strats[i:]):
            print('Opposing %s and %s...' % (strat.__name__,opponent.__name__))
            output.write('Opposing %s and %s...\n' % (strat.__name__,opponent.__name__))
            score = [0,0]
            matchs_nuls = 0
            for taille in tailles:
                print('    Taille %s' % taille)
                output.write('    Size %s:\n' %taille)
                gagnant, temps_match = morpion.match(taille, (strat, opponent), display=False)
                temps[i] += temps_match[0]
                temps[j] += temps_match[1]
                if gagnant is None:
                    matchs_nuls += 1
                    output.write('        Match nul')
                else:
                    score[gagnant] += 1
                    output.write('        Gagnant: %s\n' % strat.__name__ if not gagnant else opponent.__name__)
                    
            output.write('    Total:\n')
            output.write('        %s: %s/%s (%s%%)\n' % (
                strat.__name__,
                score[0],
                len(tailles),
                100*score[0]/float(len(tailles))))
            output.write('        %s: %s/%s (%s%%)\n' % (
                opponent.__name__,
                score[1],
                len(tailles),
                100*score[1]/float(len(tailles))))
            output.write('        Matchs nuls: %s/%s (%s%%)\n' % (
                matchs_nuls,
                len(tailles),
                100*matchs_nuls/float(len(tailles))))

    output.write('\n')
    for i, strat in enumerate(strats):
        output.write('Stratégie %s:\n'% strat.__name__)
        output.write('    Temps moyen pour un coup: %ss\n' % numpy.mean(temps[i]))
        output.write('    Ecart-type: %s\n' % numpy.std(temps[i]))
    output.close()

