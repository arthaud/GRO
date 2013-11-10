
function nothing = comp_tests(round_nb, print_latex)

stra={
    'cooperatif',
    'noncooperatif',
    'stackelberg',
    'palkeo',
    'penalise',
    'penalise_violent',
    'mmmttk',
    'mmmttkv2',
    'gklmjbse',
    'poly',
    'killer',
    'cooperatifmixte',
    'agressivemieux',
    'best_strategie',
%   'fourbe5', % stratégie tellement mauvaise qu'elle fausse les résultats
}';

[bla, N] = size(stra);
results = zeros(N, N);

for i=1:N
    for j=1:N
        [tx, ty, gx, gy] = jeu(round_nb,stra{i},stra{j});
        results(j, i) = sum(gx);
    end;
end;

results = [min(results); mean(results); max(results)];
disp('Min/Mean/Max');

if print_latex
    for i=1:N
        fprintf('%20s & $%6.2f$ & $%6.2f$ & $%6.2f$ \\\\\\hline\n', \
                stra{i}, results(1,i), results(2,i), results(3,i))
    end;
else
    for i=1:N
        fprintf('6.2f  %6.2f  %6.2f %s\n', \
                results(1,i), results(2,i), results(3,i), stra{i})
    end;
end;

