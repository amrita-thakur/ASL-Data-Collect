## Create Augmented Dataset folder somewhere and provide its path in "new_path" variable, keep category_name[j] as it is.

import imageio
import os
import imgaug as ia
import imgaug.augmenters as iaa
from random import shuffle


def create_category(path_name):
    if not os.path.exists(path_name):
        try:
            os.mkdir(path_name)
        except OSError:
            print ("Creation of the directory {} failed".format(path_name))
        else:
            print ("Successfully created the directory {}".format(path_name))
			
			
path = "C:/Python/Python37/Scripts/Project/QT Designer ASL camera/ASL alphabets/"
category_name = os.listdir(path)

for j in range(len(category_name)):
    data_path= path + category_name[j] + '/'
    files = os.listdir(data_path)
    
    for i in range(100):
        shuffle(files)
    
    count = 0
    for filename in files:
        count = count + 1
        image_path = data_path + filename
        image = imageio.imread(image_path)

        new_path = 'Augmented Dataset/'+ category_name[j]
        create_category(new_path)
        final_path = new_path + '/' + str(random.randint(1,10000000))+ ".jpg"
        if count <= 50:
            flip_hr = iaa.Fliplr(p = 1.0)
            flip_hr_image = flip_hr.augment_image(image)
            imageio.imwrite(final_path, flip_hr_image) 