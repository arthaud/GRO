function x = strategie(numpart,tx,ty,gx,gy)
% strategie -- Strategie d'un joueur 
%
%  Usage
%    x = strategie(numpart,tx,ty,gx,gy)
%
%  Inputs
%    tx     tableau des strategies jouees par le joueur x
%    ty     tableau des strategies jouees par le joueur y (l'adversaire)
%    gx     tableau des gains du joueur x
%    gy     tableau des gains du joueur y (l'adversaire)
%
%  Outputs
%    x      strategie elaboree par le joueur x
%
%  Description
%    Elaboration d'une strategie dans le cadre de jeux iteres
%    avec information complete. L'ensemble des strategies est
%
%  See also
%    jeu
%
if (numpart == 2)
	x=0.75;
else
    if (tx(numpart-1)-0.3<ty(numpart-1)<tx(numpart-1)+0.3)&&(numpart<80)
        x=ty(numpart-1);
    else
            x = 2*ty(numpart-1);
    end
    if (numpart>4)
        if (ty(numpart-1)/(tx(numpart-2)-3)==ty(numpart-2)/(tx(numpart-3)-3))
            if (tx(numpart-2)~=tx(numpart-3))
                b = (ty(numpart-2)-ty(numpart-1))/(tx(numpart-2)-tx(numpart-3));
                x = (3-ty(numpart-1))/(2-b);
            end
        end
        if (tx(numpart-2)==2.99)||(tx(numpart-1)==2.99)
            x=0.1;
        end
    end
    if (x<0)
        x=0;
    end
    if (x>3)
        x=2.99;
    end
end;