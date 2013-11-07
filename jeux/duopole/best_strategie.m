function x = strategie(numpart,tx,ty,gx,gy)
% strategie -- Strategie d'un joueur 
%
%  Usage
%    x = strategie(numpart,tx,ty,gx,gy)
%
%  Inputs
%    tx     tableau des strategies jouees par le joueur x
%    ty     tableau des strategies jouees par le joueur y (l'adversaire)
%    gx     tableau des gains du joueur x
%    gy     tableau des gains du joueur y (l'adversaire)
%
%  Outputs
%    x      strategie elaboree par le joueur x
%
%  Description
%    Elaboration d'une strategie dans le cadre de jeux iteres
%    avec information complete. L'ensemble des strategies est
%
%  See also
%    jeu
%
%  References
%    "L'altruisme perfectionne", J.P. Delahaye, P. Mathieu,
%    Pour la science No 187, Mai 1993
%

persistent compteur;
persistent seuil
if ( isempty(compteur))
    compteur = 0
    seuil = 10 + floor(20*rand());
end;

if (numpart <= 2)
	x= 0.75;
else
    if ty(numpart-1) == 0.75
        x=0.75;
    else
        lambda = 2*ty(numpart-1) / (3-tx(numpart-2));
        if lambda >= 1.9
            x = 0.75;
        else
            x = (lambda + 0.1)*(3-ty(numpart-1))/2;
        end;
    end;
end;
if ( x == 0.75 )
    compteur = compteur + 1;
else
    compteur = 0;
end;
if compteur > seuil
    x = (3-ty(numpart-1))/2;
    seuil = 10 + floor(rand()*20);
    compteur = 31;
end;
    