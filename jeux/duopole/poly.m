function x = strategie(numpart,tx,ty,gx,gy)
if (numpart == 2)
	x= 0.75;
else
    x= 1/3*ty(numpart-1)^2-3/4*ty(numpart-1)+1.125;
end;

