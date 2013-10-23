#!/usr/bin/python

from __future__ import division
import collections
import operator

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
    pass


class SRandom():
    def resultat(self, resultat):
        pass

    def predire(self):
        return {PAPIER: 1/3, CAILLOU: 1/3, CISEAU: 1/3}


class SPapier(SRandom):
    def predire(self, resultat):
        return {PAPIER: 1}


class SCaillou(SPapier):
    def predire(self, resultat):
        return {CAILLOU: 1}


class SCiseau(SPapier):
    def predire(self, resultat):
        return {CISEAU: 1}


class SMarkov(Strategie):
    def __init__(self, n=1):
        self.previous = []
        self.d = collections.defaultdict(lambda: collections.defaultdict(int))
        self.n = n

    def resultat(self, resultat):
        self.d[tuple(self.previous[-self.n:])][resultat] += 1
        self.previous.append(resultat)

    def predire(self):
        count = sum(self.d[tuple(self.previous[-self.n:])].values())
        if not count:
            return {}
        return {k: v / count for k, v in self.d[tuple(self.previous[-self.n:])].items()}


class Joueur():
    def __init__(self):
        self.strategies = {
            #SPapier(): 1,
            #SCaillou(): 1,
            #SCiseau(): 1,
            SRandom(): 1e-10,
            #SMarkov(): 1,
            SMarkov(2): 1,
            #SMarkov(3): 1,
        }

    def jouer(self):
        scores = collections.defaultdict(float)
        for s, coef in self.strategies.items():
            for prediction, coef2 in s.predire().items():
                scores[prediction] += coef * coef2

        prediction = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)[0][0]
        
        return ANTAGONISTE[prediction]

    def resultat(self, resultat):
        for s in self.strategies:
            s.resultat(resultat)


class JoueurHumain():
    def jouer(self):
        i = None
        while i not in range(3):
            try:
                i = int(input("0->Papier, 1->Caillou, 2->Ciseau : "))
            except:
                pass
        return i
    
    def resultat(self, resultat):
        print("L'ennemi a fait : %s" % resultat)


class Arbitre():
    def __init__(self, joueur1, joueur2):
        self.joueur1, self.joueur2 = joueur1, joueur2

    def jouer(self, n=100):
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

