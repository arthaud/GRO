% Stratégie joue de plus en plus tant que l'autre coopère et qui coopère sinon.
function x = strategie(numpart,tx,ty,gx,gy)
if (numpart <= 2)
    x = 0.75;
else
    ty_mean = mean(ty(numpart-2:numpart-1));

    if (ty_mean < 0.8)
        x = tanh(numpart/10)*1.5;
    else
        x = 0.75;
    end;
end;

