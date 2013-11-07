% Stratégie qui joue telle que:
%   f(0)    = 1.125   (on est pas trop brutal)
%   f(0.75) = 0.75    (on coopère avec qqn qui coopère)
%   f(1.5)  = 0.75    (on essaye de coopérer avec qqn qui ne coopère pas, des
%                      fois qu'il changerait d'avis)
% en fonction de mean(ty(2:numpart-1)).
function x = strategie(numpart,tx,ty,gx,gy)
if (numpart <= 2)
    x= 0.75;
else
    x= 1/3*mean(ty(2:numpart-1))^2-3/4*mean(ty(2:numpart-1))+1.125;
end;

