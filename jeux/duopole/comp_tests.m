NBJ=input('Nombre de parties: ');

stra={'cooperatif', 'noncooperatif', 'killer', 'penalise', 'stackelberg', 'mmmttk', 'penalise_violent', 'evolutif', 'gklmjbse'};
[_, N] = size(stra);
results = zeros(N, N);

for i=1:N
    for j=1:N
        [tx, ty, gx, gy] = jeu(NBJ,stra{i},stra{j});
        results(j, i) = sum(gx);
    end;
end;

results = [min(results); mean(results); max(results)];
disp('Min/Mean/Max');
for i=1:N
    fprintf('%5.2f  %5.2f  %5.2f %s\n', results(1,i), results(2,i), results(3,i), stra{i})
end;

