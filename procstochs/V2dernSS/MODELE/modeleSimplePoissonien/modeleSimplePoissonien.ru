 NB INIT    I    �Nodes names
end

States of nodes
x[1:4]=0;
print -T'5'  -F'resultats_f' x
end

States of mutable directed arcs
end

States of mutable undirected arcs
end

Constants
lambda = 0.6
mu = 0.4
end
 E-N N0 x[1] =random()<lambda
 E-N N1 x[2] = x[2]+d12-d42
 E-N N2 x[3] = x[3] + d23 
 E-N N3 x[4] =random()<mu
 DO-FL  ARC ( N2 --- N3 ) double d23  = x[2]*d42 
 DO-FL  ARC ( N4 --- N2 ) double d42  = x[4] >0
 DO-FL  ARC ( N1 --- N2 ) double d12=x[1] 
