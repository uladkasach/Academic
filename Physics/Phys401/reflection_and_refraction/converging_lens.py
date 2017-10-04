import numpy as np;


first_object_position   = 836;
lens_positions          = [398, 398, 398, 353, 353, 353, 331, 331, 331, 320, 320, 320, 296, 296, 296];
image_positions         = [
                            [209, 208, 208, 175, 176, 175, 156, 156, 156, 146, 146, 147, 124, 127, 126],
                            [210, 207, 208, 175, 175, 178, 156, 157, 159, 146, 151, 148, 125, 124, 127],
                          ];

lens_index = 1;
lens_positions = lens_positions;
image_positions = image_positions[lens_index];

focal_lengths = [];
for index in range(len(lens_positions)):
    first_object_position = first_object_position;
    #print(lens_positions);
    first_lens_position = lens_positions[index];
    first_image_position = image_positions[index];
    #print(first_lens_position);
    #print(first_image_position);

    final_object_distance = float(first_object_position -  first_lens_position)
    final_image_distance = float(first_lens_position - first_image_position);

    f_converging = 1/float(1/final_object_distance + 1/final_image_distance);
    focal_lengths.append(f_converging);
    print("focal length : " + str(f_converging));

n = len(lens_positions);
avg = np.mean(focal_lengths);
stdev = np.std(focal_lengths);

print("n : " + str(n));
print("avg : " + str(avg));
print("stdev : " + str(stdev));
