function x = strategie(numpart,tx,ty,gx,gy)

if (numpart == 1)
        x = 0.75;
elseif (numpart == 2)
        x = 0.85;
else 
        if ((gx(numpart-1)-gx(numpart-2)) > 0 && (tx(numpart-1)-gx(numpart-2)>0)) 
                x = tx(numpart-1) + 0.1;
        elseif (gx(numpart-1)-gx(numpart-2) < 0 && (tx(numpart-1)-gx(numpart-2)>0))
                x = tx(numpart-1) - 0.1;
        elseif  (gx(numpart-1)-gx(numpart-2) > 0 && (tx(numpart-1)-gx(numpart-2)<0))
                x = tx(numpart-1) - 0.1;
        else
                x = tx(numpart-1) + 0.1;
        end
end
