% Stratégie développée par un autre groupe donnée pour les tests.
function x = strategie(numpart,tx,ty,gx,gy)

%cooperation donc on joue d/4, ici d=3 donc x = 0.75
if(numpart<=8) %on essaye de cooperer pendant 5 tour
	x= 0.75;
else
    moy = mean(ty(numpart-4:numpart-1));
    if (moy > 0.80 && ty(numpart-1) == 0.75)
        x = 0.75;
    elseif (moy < 0.70)
        x = 1.5 - moy;
    elseif (moy > 0.80) %on accepte une marge pour rester cooperatif
        x=1.5; 
    else
        x = 0.75;
    end
end;
