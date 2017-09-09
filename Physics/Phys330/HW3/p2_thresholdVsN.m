%% Plot N(threshold) -vs- (threshold)

thresholds = [0.1, 0.05, 0.01, 0.005, 0.001]
n_depth = [10, 19, 92, 183, 912]%% Found by series_equals_ln2.m

loglog(thresholds, n_depth, '-s')
grid on
title('Accuracy Level vs Cutoff N - Two Dimensional')
ylabel('N');
xlabel('Accuracy');