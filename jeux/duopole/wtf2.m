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

if (numpart <= 2)
    x=0.75;
else
    b = ty(numpart-1)/(3-tx(numpart-2));
    x = (3-ty(numpart-1))/(2-b);
end;
