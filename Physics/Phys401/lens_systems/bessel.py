import numpy as np;


object_position         = 880;
image_positions         = [171, 10, 124, 163, 182, 199, 178, 156, 114, 54]
lens_position_pairs     = [
                            [(700, 344), (715, 167), (704, 292), (704, 334), (700, 354), (659, 372), (700, 350), (700, 322), (708, 281), (710, 215)],
                            [(701, 342), (715, 164), (707, 290), (702, 333), (697, 356), (697, 374), (700, 345), (700, 328), (705, 278), (711, 215)],
                            [(699, 342), (714, 170), (710, 292), (702, 331), (695, 354), (696, 372), (701, 346), (699, 330), (706, 279), (711, 212)]
                          ];

def find_focal_len(L, D):
    f = (L**2 - D**2)/(4*L)
    return f;

delta_s = 0.5; # 0.5mm imprecision of measurement

focal_lengths = [];
focal_errors = [];
for index in range(len(image_positions)):

    L = object_position - image_positions[index];
    D_list = [];
    for person_set in lens_position_pairs:
        D_list.append(person_set[index][0] - person_set[index][1]);


    print(L, "& ", D_list[0], "& ", D_list[1], "& ", D_list[2], "\\\\");

    for D in D_list:
        f = find_focal_len(L, D);
        focal_lengths.append(f);
        focal_error = f*((2*L*delta_s - 2*D*delta_s)/float(L**2 - D**2) - delta_s/float(L));
        focal_errors.append(focal_error);




print("---------------");

n = len(focal_errors);
avg = np.mean(focal_errors);
stdev = np.std(focal_errors);

print("n : " + str(n));
print("avg : " + str(avg));
print("stdev : " + str(stdev));

print("---------------");


print("mean : ", np.mean(focal_lengths));
print("stdev: ", np.std(focal_lengths));
