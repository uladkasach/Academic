%% Plot N(threshold) -vs- (threshold)

thresholds = [0.1, 0.05, 0.01, 0.005, 0.001]
n_depth = [8, 14, 68, 134, 667]%% Found by series_equals_ln2.m
%% 1.3431
loglog(thresholds, n_depth, '-s')
grid on
title('Accuracy Level vs Cutoff N - Three Dimensional')
ylabel('N');
xlabel('Accuracy');