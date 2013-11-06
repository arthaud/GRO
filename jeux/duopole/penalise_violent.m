% Stratégie qui "pénalise" de plus en plus l'adversaire s'il n'est pas
% coopératif.
function x = strategie(numpart,tx,ty,gx,gy)
nbr_penal_y = 0;
nbr_penal_x = 0;

for i = 2:numpart-1
  if (ty(i) > 0.75)
    nbr_penal_y = nbr_penal_y + 1;
  end;
end;

while numpart-nbr_penal_x-1>0 && (tx(numpart-nbr_penal_x-1) > 0.75),
  nbr_penal_x = nbr_penal_x + 1;
end;

if (nbr_penal_x < nbr_penal_y)
  x = 1.1255*2*(3-ty(numpart-1))/3;
else
  x = 0.75;
end;
