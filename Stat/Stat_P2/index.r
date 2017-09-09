cat("\014") ## Clear Console 
 
###############################
## 1) Sampe 50 points from X~Ber(p0=0.2)
###############################
sample = rbinom(50, 1, 0.2);
##
# Result: 
# [1] 1 0 0 0 0 0 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
##


###############################
## 2) Calculate the sample proportion p^* of "1"s shown in the above sampe you obtained
###############################
p_hat_star = sum(sample)/length(sample);
##
# Result: 
# [1] 0.22
##

###############################
## 3) Do you think it's reasonably good enough? Explain why.
###############################
# Yes, this sample proportion is reasonably close to the original proportion. 
## 
# Because n > 30, X_avg = p^* = p_hat_star ~ N(p0, pq/n).
# P(|p_hat_star - p0| >= 0.22-p0) = 2*P(p_hat_star-p0 >= 0.22-p0) = 2*P([p_hat_star - p0]/[sqrt(pq/n)] >= [0.22-p0]/[sqrt(pq/n)])
# = 2*P(Z >= 0.02/0.05657) = 2*P(Z >= 0.353544) = 2*normalcdf(0.353544, 9^9, 0, 1) = 2*0.36184 = 72.36%
# Thus the probability of a deviation in sample proportion being equal to or greater than 0.02 is 72.36%, which is rather large.
# This furthur confirms our assumption that this is reasonably good enough.


################################
## 4) Pretend that you forgot the probability of success p0 you used to generate the above sample of size 50. Your guess now is 0.4. And you want to figure out whether it is 0.4. Here are two ways for your choice, and which one do you think is more reasonable?
################################

########################
## a) Compare the sample proportion you got in above part 2 with your guess 0.4. If they are reasonably close, you will adopt your guess 0.4. Think about how you could judge the closeness.
########################
# The sample proportion and the guess are not very close, and this guess will not be adopted.
##
# Because n > 30, X_avg = p̂* = p_hat_star ~ N(p0, pq/n).
# P(|p_hat_star - 0.4| >= |0.22-0.4|) = 2*P(p_hat_star-0.4 >= |0.22-0.4|) = 2*P([p_hat_star - 0.4]/[sqrt(0.4*0.6/50)] >= [0.22-0.4]/[sqrt(pq/n)])
# = 2*P(Z >= 0.18/0.0693) = 2*P(Z >= 2.5974) = 2*normalcdf(2.5974, 9^9, 0, 1) = 2*0.00469 = 0.939%
# Thus the probability of the sample proportion deviating by 0.18 or more is less than 1%. This is quite low.
# This suggests that a guess of 0.4 is not very close to the truth.

########################
## b) Generate 10,000 p̂ values for n = 50 given that p0 = 0.4. Plot the histogram of p̂_k k = [1, 10000]. Calculate the probability that p̂ < p̂∗ through the frequency of {p̂_k  < p̂*, k = [1,10000]}. This probability is actually related with the important concept in Statistics, p value!
########################
N = 10000;
n = 50;
result = apply(matrix(1:N, ncol = 1), 1, function(x) rbinom(50, 1, 0.4))
hist(colSums(result)/n, xlab = expression(bar(X)[n]), main = "", prob = TRUE)
## See Rplot
p_hat_k = colSums(result)/n;
p_hat_k = as.integer(p_hat_k < p_hat_star);
prob = sum(p_hat_k)/N
##
# Result:
# [1] 0.003
##
# This value, 0.3%, too confirms that the guess of 0.4 is a poor choice for the given sample average. 0.22,  p^*, is in a very extreem region of this distribution. 


################################
# 5) Calculate the exact probability of P(p^_50 < p^*) given that X ~ Bern(p0 = 0.4)
################################
# For an exact calculation, P(p^_50 < p^*) = binomcdf(50, 0.4, p^*50) = 0.005687 = 0.578%. 


################################
# 6) Calculate the CTL aproximated probability of P(p^_50 < p^*) given that X ~ Bern(p0 = 0.4), n > 30, 
################################
# p^_50 ~ N(0.4, 0.4*0.6/50),
# P(p^_50 <= p^*) = normalcdf(-9^9, p^*, 0.4, sqrt(0.4*0.6/50)) = 0.004687 = 0.4687%.

################################
# 7) Compare p values obtained in the above 3 ways. Also, calculate the corrected CLT probability.
#################################
########################
# a) Compare p values obtained in the above 3 ways
########################
# The CTL of the p value is very similar to the exact probability, more similar than the simulation estimate, and does not vary like the simulated estimation does every time it is computed. 

########################
# b) Calculate the corrected CLT probability.
########################
#  P(p^_50 <= p^*) =  P(p^_50*50 <= (p^*)*50 + 0.5) = normalcdf(-9^9, (0.22)*50 + 0.5, 0.4*50, sqrt(50*0.4*0.6)) = 0.00707 = 0.707%