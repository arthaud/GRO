disp('Duopole de Cournot');
disp('Stratégies possibles : optimal/noncooperatif/stackelberg');
NBJ=input('Nombre de parties: ');
strax=input('Stratégie du 1er joueur: ','s');
stray=input('Stratégie du second joueur: ','s');
[tx, ty, gx, gy] = jeu(NBJ,strax,stray);
fig = afficher(tx,ty,gx,gy,strax,stray);
