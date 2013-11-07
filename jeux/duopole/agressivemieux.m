% Stratégie développée par un autre groupe donnée pour les tests.
function x = strategie(numpart,tx,ty,gx,gy)
if (numpart>10 && mean(ty(numpart-9:numpart-1)) == 0.75 && mean(tx(numpart-6:numpart-1)) == 0.75)
    x=1.5;
elseif(numpart > 2  && ty(numpart-1) == 0.75)
    x=0.75;
elseif(numpart<=5)
	x= 0.75;
else
    moy = mean(ty(numpart-4:numpart-1));
    if(moy > 0.75)
        x=1.5; %valeur à optimiser
    else
        x = 1.5 - moy;
    end
end;
