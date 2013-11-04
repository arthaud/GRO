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
nbr_penal_y = 0;
nbr_penal_x = 0;

for i = 1:numpart-1
  if (ty(i) > 0.75)
    nbr_penal_y = nbr_penal_y + 1;
  end;
end;

while numpart-nbr_penal_x-1>0 && (tx(numpart-nbr_penal_x-1) > 0.75),
  nbr_penal_x = nbr_penal_x + 1;
end;

if (nbr_penal_x < nbr_penal_y)
  x = 2*(3-ty(numpart-1))/3;
else
  x = 0.75;
end;
