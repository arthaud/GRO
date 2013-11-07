function x = strategie(numpart,tx,ty,gx,gy)
if (numpart <= 2)
    x = 0.75;
else
    ty_mean = mean(ty(numpart-2:numpart-1));

    if (ty_mean < 0.8)
        x = tanh(numpart/10)*1.5;
    elseif (ty_mean > 1.3)
        x = 0.75;
    else
        x = 1.5;
    end;
end;

