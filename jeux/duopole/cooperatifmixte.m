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

%cooperation donc on joue d/4, ici d=3 donc x = 0.75
if(numpart<=8) %on essaye de cooperer pendant 5 tour
	x= 0.75;
else
    moy = mean(ty(numpart-4:numpart-1));
    if (moy > 0.80 && ty(numpart-1) == 0.75)
        x = 0.75;
    elseif (moy < 0.70)
        x = 1.5 - moy;
    elseif (moy > 0.80) %on accepte une marge pour rester cooperatif
        x=1.5; 
    else
        x = 0.75;
    end
end;
