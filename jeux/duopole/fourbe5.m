% Stratégie développée par un autre groupe donnée pour les tests.
function x = strategie(numpart,tx,ty,gx,gy)
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
