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
  %x = 2*(3-ty(numpart-1))/3;
  x = 1.5;
else
  x = 0.75;
end;
