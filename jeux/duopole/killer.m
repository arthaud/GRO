function x = strategie(numpart,tx,ty,gx,gy)

if (numpart <= 5)
    x = 1.5;
else
   y_mean = mean(ty(numpart-5:numpart-1));

   if (y_mean > 0.75)
       x = 1.5;
   else
       x = 1.5-y_mean;
   end;
end;
