% Stratégie développée par un autre groupe donnée pour les tests.
function x = strategie(numpart,tx,ty,gx,gy)
persistent compteur;
persistent seuil
if ( isempty(compteur))
    compteur = 0
    seuil = 10 + floor(20*rand());
end;

if (numpart <= 2)
	x= 0.75;
else
    if ty(numpart-1) == 0.75
        x=0.75;
    else
        lambda = 2*ty(numpart-1) / (3-tx(numpart-2));
        if lambda >= 1.9
            x = 0.75;
        else
            x = (lambda + 0.1)*(3-ty(numpart-1))/2;
        end;
    end;
end;
if ( x == 0.75 )
    compteur = compteur + 1;
else
    compteur = 0;
end;
if compteur > seuil
    x = (3-ty(numpart-1))/2;
    seuil = 10 + floor(rand()*20);
    compteur = 31;
end;
    
