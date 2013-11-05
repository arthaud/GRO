function x = strategie(numpart,tx,ty,gx,gy)
if (numpart == 1)
	x= 0;
else
	ty_mean = mean(ty(1:numpart-1));
	x = 2*(3-ty_mean)/3;
end;
