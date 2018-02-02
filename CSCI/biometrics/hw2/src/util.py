import os;
import pickle;
import numpy as np;
import hashlib;

def name_gen(image_number, k_number):
    image_name = {'0' : "haiying", '1': "lihua"}[image_number];
    k_number = str(k_number);

    source_path = "images/source/"+image_name+".jpg";
    output_path = "images/pred/"+image_name+".k_" + k_number + ".jpg";
    return source_path, output_path;

def load_from_cache(cache_path):
    cache_path = "cache/" + cache_path ;
    bool_overwrite = "OVERWRITE" in os.environ and os.environ["OVERWRITE"] == "true"; ## if environmental variable set to overwrite, overwrite
    if(os.path.isfile(cache_path) and not bool_overwrite):
        with open(cache_path, 'rb') as pkl_file:
            try:
                return pickle.load(pkl_file)
            except EOFError:
                return False; ## error loading file
    else:
        return False; ## file DNE

def save_to_cache(cache_path, data):
    cache_path = hashlib.md5(cache_path).hexdigest(); ## makes it simpler
    cache_path = "cache/" + cache_path + ".pkl";
    with open(cache_path, 'wb') as pkl_file:
        pickle.dump(data, pkl_file)

def map_probabilities_to_image(image, prob):
    print 'mapping pixels to clusters to render image...'
    prediction = np.array(image); ## create a copy
    for index, probability in enumerate(prob):
        prediction[index] = np.array(probability);
    return prediction;
