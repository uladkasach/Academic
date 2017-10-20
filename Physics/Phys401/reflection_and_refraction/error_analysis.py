


delta_s = ;
delta_t = ;
delta_theta1 = 1;


def calculate_imprecision(s, t, theta1, n2)
    delta_s_over_t = delta_s / t - s / t**2 * delta_t;
    part1 = np.cos(theta1) / np.sin(theta1) * delta_theta1;
    part2 = (delta_s_over_t * (1 - np.sin(theta1)) - s/t*np.cos(theta1) * delta_theta1) / ((s/t)**2 - 2 * s / 5 * np.sin(theta1));
    part3 = (np.cos(theta1) * delta_theta1 - delta_s_over_t) / (np.sin(theta1) - s/t)
    delta_n2 = n2 * (part1 + part2 + part3);
