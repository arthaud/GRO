function x = strategie(numpart,tx,ty,gx,gy)

x = min(max(ty(numpart - 1), 0.75), 1.5);
    
mid_start = floor(numpart / 2);
end_start = floor(5 * numpart / 6);
    
% anti plongeon dans le négatif
if(numpart > 5 && mean(ty(numpart - 5 : numpart - 1)) > 2)
    x = 1;
end;

% si la stratégie n'évolue pas sur plusieurs tours, et qu'il est
% méchant : j'essaie de communiquer en étant gentil
if(mean(ty(mid_start : numpart - 1)) >= mean(ty(end_start : numpart - 1)))
    if(log2(numpart / 10) - floor(log2(numpart / 10)) < 0.1) 
        x = 0.75;
    end;
end;

% si on est tous les deux gentils, j'essaie de l'attaquer gentiment
% si il réagit, je ferme ma gueule et je coopère.
if(numpart > 4 && mean(ty(mid_start : numpart - 1)) == 0.75)
    x = min(tx(numpart - 1) + 0.05, 1.125);
end;