%% Plot N(threshold) -vs- (threshold)


%% point (0.1, 0.5)
thresholds = [0.1, 0.05, 0.01, 0.005, 0.001]
n_depth = [3, 3, 5, 5, 5]

semilogx(thresholds, n_depth, '-s')
hold on



%% point (0.5, 0.5)
thresholds = [0.1, 0.05, 0.01, 0.005, 0.001]
n_depth = [3, 5, 5, 7, 9]

semilogx(thresholds, n_depth, '-s')
hold on


%% point (0.9, 0.5)
thresholds = [0.1, 0.05, 0.01, 0.005, 0.001]
n_depth = [7, 9, 15, 19, 27]


semilogx(thresholds, n_depth, '-s')



grid on
title('Accuracy Level vs Cutoff N - Problem 4')
ylabel('N');
xlabel('Accuracy');