function x = strategie(numpart,tx,ty,gx,gy)
% strategie -- Strategie d'un joueur 
%
%  Usage
%    x = strategie(nx,ny,ng,tx,ty,gx,gy)
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

if (numpart>10 && mean(ty(numpart-9:numpart-1)) == 0.75 && mean(tx(numpart-6:numpart-1)) == 0.75)
    x=1.5;
elseif(numpart > 2  && ty(numpart-1) == 0.75)
    x=0.75;
elseif(numpart<=5)
	x= 0.75;
else
    moy = mean(ty(numpart-4:numpart-1));
    if(moy > 0.75)
        x=1.5; %valeur à optimiser
    else
        x = 1.5 - moy;
    end
end;
