NBJ=input('Nombre de parties: ');

N = 9; % nb de stratégies, ne pas oublier d'ajouter les nouvelles
stra=cell(N, 1);
stra{1} = 'cooperatif';
stra{9} = 'gklmjbse';
stra{2} = 'noncooperatif';
stra{3} = 'killer';
stra{4} = 'penalise';
stra{5} = 'stackelberg';
stra{6} = 'stackelberg_mean';
stra{7} = 'penalise_violent';
stra{8} = 'evolutif';

results = zeros(N, N);

for i=1:size(stra)
    for j=1:size(stra)
        [tx, ty, gx, gy] = jeu(NBJ,stra{i},stra{j});
        results(j, i) = sum(gx);
    end;
end;

results = [min(results); mean(results); max(results)];
disp('Min/Mean/Max')

for i=1:N
    fprintf('%5.2f  %5.2f  %5.2f %s\n', results(1,i), results(2,i), results(3,i), stra{i})
end;

