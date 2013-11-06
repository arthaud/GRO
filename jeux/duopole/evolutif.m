function x = strategie(numpart,tx,ty,gx,gy)

if (numpart == 1)
        x = 0.75;
elseif (numpart == 2)
        x = 0.85;
else 
        step = 1.3;

        if ((gx(numpart-1)>gx(numpart-2)) && (tx(numpart-1)>gx(numpart-2))) 
                x = tx(numpart-1) * step;
        elseif (gx(numpart-1)<gx(numpart-2) && (tx(numpart-1)>gx(numpart-2)))
                x = tx(numpart-1) / step;
        elseif  (gx(numpart-1)>gx(numpart-2) && (tx(numpart-1)<gx(numpart-2)))
                x = tx(numpart-1) / step;
        else
                x = tx(numpart-1) * step;
        end
end
