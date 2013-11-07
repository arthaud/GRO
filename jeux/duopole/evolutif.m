function x = strategie(numpart,tx,ty,gx,gy)
persistent step;
if (numpart <= 2)
        x = 0.75;
        step = 1.3;
elseif (numpart == 3)
        x = 0.85;
else 

        if ((gx(numpart-1)>gx(numpart-2)) && (tx(numpart-1)>tx(numpart-2))) 
                x = tx(numpart-1) + step;
                step = step * 1.2;
        elseif (gx(numpart-1)<gx(numpart-2) && (tx(numpart-1)>tx(numpart-2)))
                x = tx(numpart-1) - step;
                step = step / 1.2;
        elseif  (gx(numpart-1)>gx(numpart-2) && (tx(numpart-1)<tx(numpart-2)))
                x = tx(numpart-1) - step;
                step = step * 1.2;
        else
                x = tx(numpart-1) + step;
                step = step / 1.2;
        end

        x = max(0.75, min(1.5, x));
end
