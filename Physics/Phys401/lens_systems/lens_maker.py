
focal_len = 33.64;
first_object_position   = 836;
lens_positions = lens_positions;
image_positions = image_positions[lens_index];



def focal_from_distance(object_distance, image_distance):
    focal_len = 1/float(1/object_distance + 1/image_distance);
    return focal_len;

def image_from_object_and_focal(focal_len, object_distance):
    image_distance = 1/float(1/focal_len - 1/object_distance);
    return image_distance;


def return_distances_from_single_set(object, lens, image):
    flipper = (object - lens < 0)?  -1 : 1;
    return {
        "object" : flipper*(object - lens),
        "image" : flipper*(lens - image);
    }


#distances = return_distances_from_single_set(object_position, lens_start, image_position, lens_thickness)
