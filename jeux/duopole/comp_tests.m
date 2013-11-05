NBJ=input('Nombre de parties: ');

N = 5; % nb de stratégies, ne pas oublier d'ajouter les nouvelles
stra=cell(N, 1);
stra{1} = 'cooperatif';
stra{2} = 'noncooperatif';
stra{3} = 'killer';
stra{4} = 'penalise';
stra{5} = 'stackelberg';

results = zeros(N, N);

for i=1:size(stra)
    for j=1:size(stra)
        [tx, ty, gx, gy] = jeu(NBJ,stra{i},stra{j});
        results(i, j) = sum(gx);
    end;
end;

results = [min(results); mean(results); max(results)];
disp('Min     Max     Mean'), disp(results')

