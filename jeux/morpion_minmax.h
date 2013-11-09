#ifndef HEADER_MORPION_MINMAX
#define HEADER_MORPION_MINMAX

#include "Python.h"

/* Définition des types */
typedef enum {VIDE, CROIX, ROND} Case;
typedef Case* Morpion;

typedef struct {
    unsigned int x;
    unsigned int y;
} Position;

/* Manipulation des Morpions */
Morpion new_morpion(unsigned int n);
void free_morpion(Morpion morpion);
Morpion copy_morpion(Morpion morpion, unsigned int n);
void print_case(Case c);
void print_morpion(Morpion morpion, unsigned int n);
Case adversaire(Case c);

/* Algorithme de Minmax */
int Infini = 1000000;
int parcours_morpion(unsigned int n, int i, int j);
int evaluation(Morpion morpion, unsigned int n, Case joueur);
int minmax(Morpion morpion, unsigned int n, Case joueur, unsigned int profondeur_max, int elagage, Position *coup, int noeud_joueur, int first_call, int alpha_beta);
#define MINMAX(morpion, n, joueur, prof, elagage, coup) minmax((morpion), (n), (joueur), (prof), (elagage), (coup), 1, 1, 0)

/* Module Python */
static PyObject * py_morpion_minmax(PyObject *self, PyObject *args);

static PyMethodDef MorpionMinmaxMethods[] = {
    {"minmax",  py_morpion_minmax, METH_VARARGS, "Fonction identique à morpion_strategies.minmax, mais en C."},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initmorpion_minmax(void);

#endif /* !HEADER_MORPION_MINMAX */
