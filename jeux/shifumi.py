#!/usr/bin/python

from __future__ import division
import collections
import operator
import random

PAPIER, CAILLOU, CISEAU = range(3)

RESULTATS = {
    (PAPIER, PAPIER): (0, 0),
    (CAILLOU, CAILLOU): (0, 0),
    (CISEAU, CISEAU): (0, 0),
    (PAPIER, CAILLOU): (1, 0),
    (PAPIER, CISEAU): (0, 1),
    (CAILLOU, PAPIER): (0, 1),
    (CAILLOU, CISEAU): (1, 0),
    (CISEAU, PAPIER): (1, 0),
    (CISEAU, CAILLOU): (0, 1),
}
ANTAGONISTE = {
    PAPIER: CISEAU,
    CAILLOU: PAPIER,
    CISEAU: CAILLOU,
}


class Strategie():
    def __repr__(self):
        return self.__class__.__name__ + '()'


class SRandom(Strategie):
    def resultat(self, resultat):
        pass

    def predire(self):
        return random.choice((PAPIER, CAILLOU, CISEAU))


class SPapier(SRandom):
    def predire(self):
        return PAPIER


class SCaillou(SPapier):
    def predire(self):
        return CAILLOU


class SCiseau(SPapier):
    def predire(self):
        return CISEAU


class SMarkov(Strategie):
    def __init__(self, n=1):
        self.previous = []
        self.d = collections.defaultdict(lambda: collections.defaultdict(int))
        self.n = n

    def resultat(self, resultat):
        self.d[tuple(self.previous[-self.n:])][resultat] += 1
        self.previous.append(resultat)

    def predire(self):
        try:
            return sorted(self.d[tuple(self.previous[-self.n:])].items(), key=operator.itemgetter(1), reverse=True)[0][0]
        except IndexError:
            return None


class Joueur():
    def __init__(self):
        self.strategies = {
            SPapier(): 0,
            SCaillou(): 0,
            SCiseau(): 0,
            #SRandom(): 1,
            #SMarkov(): 0.6,
            SMarkov(2): 0.2,
            #SMarkov(3): 0,
            #SMarkov(4): 0,
        }
        self.tau = 50

        self.last_prediction = {}

    def jouer(self):
        scores = collections.defaultdict(float)
        for s, coef in self.strategies.items():
            prediction = s.predire()

            self.last_prediction[s] = prediction

            if prediction is None:
                continue

            scores[prediction] += coef

        prediction = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)[0][0]
        
        return ANTAGONISTE[prediction]

    def resultat(self, resultat):
        for s in self.strategies:
            s.resultat(resultat)

            goal = 1 if self.last_prediction[s] == resultat else 0
            self.strategies[s] = (self.strategies[s]*(self.tau-1) + goal) / self.tau
        
        #print(self.strategies)


class JoueurHumain():
    def jouer(self):
        i = None
        while i not in range(3):
            try:
                i = int(input("0->Papier, 1->Caillou, 2->Ciseau : "))
            except ValueError:
                pass
        return i
    
    def resultat(self, resultat):
        print("L'ennemi a fait : %s" % resultat)


class Arbitre():
    def __init__(self, joueur1, joueur2):
        self.joueur1, self.joueur2 = joueur1, joueur2

    def jouer(self, n=1000):
        s1 = 0
        s2 = 0
        for i in range(n):
            p1 = self.joueur1.jouer()
            p2 = self.joueur2.jouer()
            r = RESULTATS[p1, p2]
            s1 += r[0]
            s2 += r[1]
        
            self.joueur1.resultat(p2)
            self.joueur2.resultat(p1)

            print("[J1] Score %s : %s" % (self.joueur1, s1))
            print("[J2] Score %s : %s" % (self.joueur2, s2))
            print()


if __name__ == '__main__':
    Arbitre(Joueur(), JoueurHumain()).jouer()

