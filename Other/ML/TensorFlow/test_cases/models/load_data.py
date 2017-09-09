###############
## Import Libraries
###############
import tensorflow as tf
import load_inputs as inputs
import sys

##########################################################################
## Read a line of data
##########################################################################
def read_csv_data(filename_queue):
    #############################
    ## DataSource dependent inputs, 
    ############################
    #y_index = [2];
    #data_keys_index = [0, 1];
    #record_defaults = [[1], [1], [1], [0.1], [0.1], [0.1], [0.1], [0.1], [0.1]] # Default values, in case of empty columns. Also specifies the type of the decoded result.
    y_index = inputs.label_index;
    one_hot_depth = inputs.one_hot_depth;
    data_keys_index = inputs.keys_index;
    record_defaults = inputs.record_defaults;
    
    ##############################
    ## Define reader
    ##############################
    reader = tf.TextLineReader(skip_header_lines=1)
    key, next_line_string = reader.read(filename_queue)

    ##############################
    ## Define decoding
    ##############################
    list_of_columns = tf.decode_csv(next_line_string, record_defaults=record_defaults)
    
    ##############################
    ## Define feature, label, and key columns
    ##############################
    data_keys_columns = [list_of_columns[i] for i in data_keys_index];
    y_columns = [tf.to_int32(list_of_columns[i]) for i in y_index];
    feature_index = list(set(list(range(len(list_of_columns)))) - set(y_index)  - set(data_keys_index));
    feature_columns = [tf.to_float(list_of_columns[i]) for i in feature_index];

    ##############################
    ## Convert data to one hot, if not one hot already (if is already, y_index length > 1
    ##############################
    if one_hot_depth != 0:
        y_columns = tf.one_hot(y_columns[0], one_hot_depth);
        
    if one_hot_depth == 0 and len(y_index) < 2:
        print('One hot depth is not set, yet y_index is not two or more inputs (data is not one hot already). Error.');
        sys.exit();
    
    key = tf.pack(data_keys_columns);
    label = tf.pack(y_columns);
    features = tf.pack(feature_columns); 
    return features, label, key
##########################################################################


##########################################################################
## Read batches of input
##########################################################################
def batch_input_pipeline(filenames, batch_size, num_epochs=None):
    filename_queue = tf.train.string_input_producer(filenames, num_epochs=num_epochs, shuffle=True);
        
    features, label, key = read_csv_data(filename_queue)

    # min_after_dequeue defines how big a buffer we will randomly sample
    #   from -- bigger means better shuffling but slower start up and more
    #   memory used.
    # capacity must be larger than min_after_dequeue and the amount larger
    #   determines the maximum we will prefetch.  Recommendation:
    #   min_after_dequeue + (num_threads + a small safety margin) * batch_size
    min_after_dequeue = 100
    capacity = min_after_dequeue + 3 * batch_size
    feature_batch, label_batch, key_batch = tf.train.shuffle_batch([features, label, key], batch_size=batch_size, capacity=capacity, min_after_dequeue=min_after_dequeue)
    return feature_batch, label_batch, key_batch


