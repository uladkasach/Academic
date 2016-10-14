function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta




%%%%%%%%%%%%%%%%%%%%%%%
%% Calculate general data
%%%%%%%%%%%%%%%%%%%%%%%
initial_theta = theta; %% for ease of use in debuging in console
z = (X * initial_theta);
hypothesis = sigmoid(z);
delta = hypothesis - y; 

%% In regularization we do not want theta_0 to be regularized. 
%% Setting theta_0 (theta(1)) equal to 0 eliminates the regularization contribution of theta_0 in both gradient and cost
regularization_theta = initial_theta; 
regularization_theta(1) = 0;

%%%%%%%%%%%%%%%%%%%%%%%%%
%% Calculate Cost
%%%%%%%%%%%%%%%%%%%%%%%%%
logistic_cost_vector = (-y).*log(hypothesis) - (1-y).*log(1-hypothesis);
logistic_cost = sum(logistic_cost_vector)/length(logistic_cost_vector);
regularization_cost = lambda/2/m*sum(regularization_theta.^2);
J =  logistic_cost + regularization_cost;

%%%%%%%%%%%%%%%%%%%%%%%%%
%% Calculate Gradient
%%%%%%%%%%%%%%%%%%%%%%%%%
grad = (X' * delta)./m + lambda/m*regularization_theta;




% =============================================================

end
