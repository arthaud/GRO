function x = strategie(numpart,tx,ty,gx,gy)
if(numpart == 1)
    x = 0.75;
else
    x = min(max(ty(numpart - 1), 0.75), 1.5);

    % si la stratégie n'évolue pas sur plusieurs tours, et qu'il est
    % méchant : j'essaie de communiquer en étant gentil
    mid_start = floor(numpart / 2);
    end_start = floor(5 * numpart / 6);
    if(sum(ty(mid_start : numpart - 1)) / (numpart - mid_start) >= sum(ty(end_start : numpart - 1)) / (numpart - end_start))
        if(log2(numpart) - floor(log2(numpart)) < 0.1) 
            x = 0.75;
        end;
    end;

    % si on est tous les deux gentils, j'essaie de l'attaquer gentiment
    % si il réagit, je ferme ma gueule et je coopère.
    if(numpart > 4 && sum(ty(mid_start : numpart - 1)) / (numpart - mid_start) == 0.75)
        x = min(tx(numpart - 1) + 0.05, 1.125);
    end;
end;
