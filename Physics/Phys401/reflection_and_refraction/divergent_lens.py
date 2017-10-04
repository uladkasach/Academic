import numpy as np;


f_1 = float(130.33) ## with a stdev of 1.095


first_object_position         = 836;
set_of_first_lens_positions          = [400, 400, 400, 400, 400, 400, 431, 431, 431, 408, 408, 408, 388, 388, 388];
set_of_second_lens_positions         = [228, 228, 228, 231, 231, 231, 251, 251, 251, 234, 234, 234, 216, 216, 216];
set_of_final_image_positions         = [171, 161, 179, 106, 176,  99, 195, 205, 212, 191, 194, 189, 179, 178, 184];

focal_lengths = [];
for i in range(len(set_of_first_lens_positions)):
    first_object_position = first_object_position;
    first_lens_position = set_of_first_lens_positions[i];
    final_lens_position = set_of_second_lens_positions[i];
    final_image_position = set_of_final_image_positions[i];


    first_object_distance = float(first_object_position -  first_lens_position)
    final_image_distance = float(final_lens_position - final_image_position);


    first_image_distance = 1/float(1/f_1 - 1/first_object_distance)
    first_image_position = first_lens_position - first_image_distance;
    final_object_distance = first_image_position - final_lens_position;
    print("first image distance : " + str(first_image_distance))
    print("first image position : " + str(first_image_position))
    print("final object distance: " + str(final_object_distance));

    f_divergent = 1/float(1/final_object_distance + 1/final_image_distance);

    print("focal length : " + str(f_divergent));
    focal_lengths.append(f_divergent);


n = len(focal_lengths);
avg = np.mean(focal_lengths);
stdev = np.std(focal_lengths);

print("n : " + str(n));
print("avg : " + str(avg));
print("stdev : " + str(stdev));
