import numpy as np
import csv # to load data



path = raw_input("Please define the path of the input CSV file. (Note - program assumes last column of data is a label.)\n -> ");
if(path == "x" and False):
    path = 'magic04.csv';


print("Loading data...");
#########################################
# Step 1: Load data
#########################################
#'magic04.csv'
with open(path, 'r') as f:
  reader = csv.reader(f)
  data = list(reader)
##print(words)
#print ("Rows: ", len(data), '\n');
#print ("Dimensions: ", len(data[0]), '\n');
np_data = np.array(np.array(data)[:, 0:-1], dtype=float); # strip label from data
#print np_data;



print("Centering data...");
##########################################
# Step 2: Center Data
##########################################
def center_data(data):
    mean = np.mean(data, axis=0); #column wise mean
    #print(mean);
    return data - mean;
#np_data = np.array([[40, 10], [50, 11]])
centered_data = center_data(np_data);
#print centered_data;
#center_data(centered_data);


print "\n";
print("--- Question 1... ---");
##########################################
# Question 1: 
##########################################
# Write a function to Compute the sample covariance matrix as inner products between the
# columns of the centered data matrix (see equation 2.31). Show that the result from your function
# matches the one using numpy.cov function.
'''
def compute_sample_covariance_innerProductMethod(matrix):
    row_size_n = len(matrix);
    covar = np.dot(matrix.transpose(1,0), matrix) / row_size_n;
    #print (covar);
    #print (" n x d : " , len(covar), "x" , len(covar[0]));
    return covar;
'''
def compute_sample_covariance_outerProductMethod(matrix):
    row_size_n = len(matrix);
    col_size_d = len(matrix[0]);
    #covar = np.dot(matrix.transpose(1,0), matrix) / row_size_n;
    
    matrix_t = matrix.transpose(1,0);
    the_sum = None;
    for i in range(0, row_size_n):
        z_i = matrix[i, :].reshape(1, col_size_d); #row vector
        #print(z_i.shape);
        z_i_t = matrix_t[:, i].reshape(col_size_d, 1); #col vector
        #print(z_i_t.shape);
        #print(i)
        #print(z_i)
        #print(z_i_t);
        product_i = np.multiply(z_i,  z_i_t);
        #print(product_i)
        #print(product_i.shape);
        #exit();
        if(the_sum is None):
            the_sum = product_i;
        else:
            the_sum = the_sum + product_i; 
    covar = the_sum / row_size_n;
    
    #print (covar);
    #print (" n x d : " , len(covar), "x" , len(covar[0]));
    return covar;

Sigma = compute_sample_covariance_outerProductMethod(centered_data);
#print('\n');
#print(Sigma);
#print(Sigma.shape);
Sigma_2 = np.cov(centered_data, bias=True, rowvar=False);
#print('\n');
#print(Sigma_2);
#print(Sigma_2.shape );
#print "np.sum(difference) of function result - numpy.cov result ~= 0 :"; 
#print(np.sum(Sigma - Sigma_2));
print("np.allclose(implemented outerProduct covar, numpy.cov) = " + str( np.allclose(Sigma, Sigma_2) ));




print "\n";
print("--- Question 2... ---");
##########################################
# Question 2: 
##########################################
# Use linalg.eig to find the first two dominant eigenvectors, and compute the projection of
# data points on the subspace spanned by these two eigenvectors. Now, compute the variance of the
# datapoints in the projected subspace using the subroutine that you wrote for Question 1 (Do not
# print the projected datapoints on stdout, only print the value of the variance)
eig_vals, eig_vecs = np.linalg.eig(Sigma);
#print(eig_vals, eig_vecs);
eig_vals = np.array(eig_vals);
eig_vecs = np.array(eig_vecs);


def find_largest_not_in(values, exluded_index_array):
    largest_value = None;
    largest_index = None;
    for i in range(0, len(values)):
        to_be_excluded = i in exluded_index_array
        if(to_be_excluded):
            continue; # this value is already in array, skip it
        this_value = values[i];
        this_index = i;
        if(largest_value is None or largest_value < this_value):
            largest_value = this_value;
            largest_index = this_index;
    return largest_index, largest_value;
            
def order_eig(eigen_vals, eigen_vecs):
    ordered_indicies = [];
    for i in range(0, len(eigen_vals)):
        largest_index, largest_value = find_largest_not_in(eigen_vals, ordered_indicies);
        #print(largest_index, largest_value);
        ordered_indicies.append(largest_index);
        #print(ordered_indicies);
        
    ordered_eigen_values = [];
    ordered_eigen_vectors = np.array(eigen_vecs) * 0;
    for i in range(0, len(ordered_indicies)):
        this_index = ordered_indicies[i];
        this_val = eigen_vals[this_index];
        this_vec = eigen_vecs[:, this_index];
        #print("--");
        #print(this_vec);
        ordered_eigen_values.append(this_val);
        ordered_eigen_vectors[:, i] = this_vec;
        #print("--");
        #print(ordered_eigen_vectors[:, 0]);
    return ordered_eigen_values, ordered_eigen_vectors;

eig_vals, eig_vecs = order_eig(eig_vals, eig_vecs);
# print(eig_vals, eig_vecs);
# print("\n");
# print (eig_vecs[:,1]);
# print("\n");
# print (eig_vecs_2[:,1]);
# print(eig_vecs.shape);

top_two_eig_vecs = eig_vecs[:, 0:2];
# print(top_two_eig_vecs);
# exit();
# two_dimensional_data = np.matmul(top_two_eig_vecs.transpose(1,0), centered_data.transpose(1,0) ).transpose(1,0);
#two_dimensional_data = np.matmul(centered_data, top_two_eig_vecs);
two_dimensional_data = centered_data.dot(top_two_eig_vecs);
# print(two_dimensional_data);

# print("\n");
print("Covariance Matrix:");
# print(eig_vals);
# print("\n");
covar = compute_sample_covariance_outerProductMethod(two_dimensional_data);
print(covar);
print("\nVariance Captured :");
print(covar.trace());
print("\nPercentage of Total Variance Captured :");
print(covar.trace() / Sigma.trace());
#print(covar.trace() / sum(eig_vals));
#print(sum(eig_vals[0:2]));



print "\n";
print("--- Question 3... ---");
##########################################
# Question 3: 
##########################################
# Use linalg.eig to find all the eigenvectors, and print the covariance matrix sigma in its eigendecomposition
# form U*lambda*U^T
eig_vals = np.array(eig_vals).reshape((10, 1));
eye = np.eye(len(eig_vals));
Lambda = eye*eig_vals; 

#Sigma_Decomp = np.matmul(np.matmul(eig_vecs, Lambda), eig_vecs.transpose);
Sigma_Decomp = np.dot(eig_vecs, Lambda);
#print(eig_vecs, " dot ", Lambda, " dot ", eig_vecs.transpose(), " = ");
Sigma_Decomp = np.dot(Sigma_Decomp, eig_vecs.transpose());
print((Sigma_Decomp));
#print (np.allclose(Sigma, Sigma_Decomp))




print "\n";
print("--- Question 4... ---");
##########################################
# Question 4: 
##########################################
# Write a subroutine to implement PCA Algorithm (Algorithm 7.1, Page 198)
def PCA_Algorithm(data, percentage_to_capture):
    Z_data = center_data(data);
    covariance = compute_sample_covariance_outerProductMethod(Z_data);
    eig_vals, eig_vecs = np.linalg.eig(covariance);
    eig_vals, eig_vecs = order_eig(np.array(eig_vals), np.array(eig_vecs));

    variance_captured = 0;
    for i in range(0, len(eig_vals)):
        this_val = eig_vals[i];
        #print("variance = ", variance_captured, " + ", this_val, " = ", variance_captured + this_val);
        variance_captured += this_val;
        if(variance_captured / covariance.trace() >= percentage_to_capture):
            final_vector_index = i;
            break;
    
    #print(final_vector_index);
    #print(len(eig_vals[0:final_vector_index+1]));
    #print(sum(eig_vals[0:final_vector_index+1]) / covariance.trace());
    min_basis = eig_vecs[:, 0:final_vector_index+1];
    
    projected_data = np.dot(Z_data, min_basis);
    return projected_data;




print "\n";
print("--- Question 5... ---");
##########################################
# Question 5: 
##########################################
# Use the program above and find the principle vectors that we need to preserve 90% of variance?
# Print the co-ordinate of the first 10 data points by using the above set of vectors as the new basis
# vector.     
proj_data = PCA_Algorithm(np_data, 0.9);
print(proj_data[0:10, :]);
    

