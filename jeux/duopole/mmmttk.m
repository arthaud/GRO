% Stackelberg en moyenne, sauf si l'adversaire est coopératif.
function x = strategie(numpart,tx,ty,gx,gy)
if (numpart == 2)
	x= 0.75;
else
    ty_near_mean = mean(ty(max(numpart-5, 2):numpart-1));

    if (ty_near_mean < 0.76)
        x = 0.75;
    else
        ty_mean = mean(ty(2:numpart-1));
        x = 2*(3-ty_mean)/3;
    end;
end;

