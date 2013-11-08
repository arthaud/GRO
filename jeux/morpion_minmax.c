#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Définition des types */
typedef enum {VIDE, CROIX, ROND} Case;
typedef Case* Morpion;

typedef struct {
    unsigned int x;
    unsigned int y;
} Position;

/* Manipulation des Morpions */
Morpion new_morpion(unsigned int n)
{
    Morpion morpion;
    int x, y;
    
    morpion = (Morpion)malloc(n * n * sizeof(Case));

    if(morpion == NULL)
        return NULL;

    for(x=0; x<n; x++)
    {
        for(y=0; y<n; y++)
        {
            morpion[x+n*y] = VIDE;
        }
    }

    return morpion;
}

void free_morpion(Morpion morpion)
{
    free(morpion);
}

Morpion copy_morpion(Morpion morpion, unsigned int n)
{
    Morpion copy = (Morpion)malloc(n * n * sizeof(Case));

    if(copy == NULL)
        return NULL;

    memcpy(copy, morpion, n * n * sizeof(Case));

    return copy;
}

void print_case(Case c)
{
    switch(c)
    {
        case CROIX:
            printf("X");
            break;
        case ROND:
            printf("O");
            break;
        default:
            printf(" ");
    }
}

void print_morpion(Morpion morpion, unsigned int n)
{
    int i, x, y;

    printf("+");
    for(i=0; i<n; i++)
        printf("---+");
    printf("\n");

    for(x=0; x<n; x++)
    {
        printf("|");
        for(y=0; y<n; y++)
        {
            printf(" ");
            print_case(morpion[x+n*y]);
            printf(" |");
        }
        printf("\n");

        printf("+");
        for(i=0; i<n; i++)
            printf("---+");
        printf("\n");
    }
}

Case adversaire(Case c)
{
    if(c == CROIX)
        return ROND;
    else
        return CROIX;
}

/* Fonction parcours_morpion
 *
 * Permet de parcourir toutes les lignes, toutes les colonnes et les 2 diagonales.
 *
 * 1 <= i <= 2*n + 2
 * i indique le numéro de la "ligne" :
 *   entre 1 et n : ligne i
 *   entre n+1 et 2*n : colonne i-n
 *   2*n+1 : première diagonale
 *   2*n+2 : deuxième diagonale
 *
 * 1 <= j <= n
 * j indique l'indice dans cette ligne
 */
int parcours_morpion(unsigned int n, int i, int j)
{
    if(1 <= i && i <= n)
    {
        return (i-1) + n*(j-1);
    }
    else if(n+1 <= i && i <= 2*n)
    {
        return (j-1) + n*(i-n-1);
    }
    else if(i == 2*n + 1)
    {
        return (j-1) + n*(j-1);
    }
    else // i == 2*n + 2
    {
        return (n-j) + n*(j-1);
    }
}

int Infini = 1000000;

int evaluation(Morpion morpion, unsigned int n, Case joueur)
{
    int score = 0;
    int i, j;
    int count_joueur, count_adversaire;

    for(i=1; i <= 2*n+2; i++) /* pour chaque lignes, colonnes et diagonales */
    {
        count_joueur = 0;
        count_adversaire = 0;

        for(j=1; j <= n; j++)
        {
            if(morpion[parcours_morpion(n, i, j)] == joueur)
                count_joueur++;

            if(morpion[parcours_morpion(n, i, j)] == adversaire(joueur))
                count_adversaire++;
        }

        if(count_joueur == n)
            return Infini;
        if(count_adversaire == n)
            return -Infini;

        if(count_adversaire == 0)
            score += count_joueur;
        if(count_joueur == 0)
            score -= count_adversaire;
    }

    return score;
}

/* Fonction minmax
 * 
 * joueur indique notre joueur (CROIX, ROND)
 * elagage vaut 1 si on doit appliquer l'élagage alpha beta, sinon 0
 * coup contiendra le coup à jouer
 * noeud_joueur vaut 1 si on doit prendre le max, sinon on doit prendre le min (défaut: 1)
 * first_call vaut 1 si c'est le premier appel récursif, sinon 0 (défaut: 1)
 * alpha_beta vaut alpha ou beta, en fonction de noeud_joueur (défaut: 0)
 */
int minmax(Morpion morpion, unsigned int n, Case joueur, unsigned int profondeur_max, int elagage, Position* coup, int noeud_joueur, int first_call, int alpha_beta)
{
    Morpion fils;
    int eval, eval_optimale, first_eval = 1;
    int x, y;

    eval = evaluation(morpion, n, joueur);
    if(profondeur_max == 0 || eval == Infini || eval == -Infini)
        return eval;

    for(x=0; x<n; x++)
    {
        for(y=0; y<n; y++)
        {
            if(morpion[x + n*y] == VIDE)
            {
                fils = copy_morpion(morpion, n);

                if(noeud_joueur)
                    fils[x + n*y] = joueur;
                else
                    fils[x + n*y] = adversaire(joueur);

                eval = minmax(fils, n, joueur, profondeur_max-1, elagage, NULL, !noeud_joueur, first_eval, eval_optimale);
                free_morpion(fils);

                if(first_eval
                    || (noeud_joueur && eval > eval_optimale)
                    || (!noeud_joueur && eval < eval_optimale))
                {
                    first_eval = 0;
                    eval_optimale = eval;

                    if(coup != NULL) /* on veut le coup */
                    {
                        coup->x = x;
                        coup->y = y;
                    }
                }

                if(elagage && !first_call
                    && ((noeud_joueur && eval_optimale >= alpha_beta)
                        || (!noeud_joueur && eval_optimale <= alpha_beta)))
                {
                    return eval_optimale;
                }
            }
        }
    } 

    if(first_eval) /* jeu complet */
        return eval;

    return eval_optimale;
}

#define MINMAX(morpion, n, joueur, prof, elagage, coup) minmax((morpion), (n), (joueur), (prof), (elagage), (coup), 1, 1, 0)

int main()
{
    Morpion m;
    Position p;
    int eval;

    m = new_morpion(3);

    m[1 + 3*1] = CROIX;
    m[0] = CROIX;

    eval = MINMAX(m, 3, CROIX, 4, 1, &p);

    printf("eval = %d, coup = (%d, %d)\n", eval, p.x, p.y);

    free_morpion(m);
    return 1;
}
