% Stratégie qui "pénalise" l'adversaire s'il n'est pas coopératif.
function x = strategie(numpart,tx,ty,gx,gy)
nbr_penal_y = 0;
nbr_penal_x = 0;

for i = 1:numpart-1
  if (ty(i) > 0.75)
    nbr_penal_y = nbr_penal_y + 1;
  end;
  if (tx(i) > 0.75)
    nbr_penal_x = nbr_penal_x + 1;
  end;
end;

if (nbr_penal_x <= nbr_penal_y)
  ty_mean = ty(2);
  if numpart > 2
    ty_mean = mean(ty(2:numpart-1));
  end;

  x = (3-ty_mean)/2;
else
  x = 0.75;
end;
