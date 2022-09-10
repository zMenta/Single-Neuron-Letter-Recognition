import os
from image_processing import convert_image

data_path = "Data/TrainingData/LetterA/"
data_list = []
desired_output = 1
pixel_density = 2

file_number = 1
for file in os.listdir(data_path):
    # file is str
    # print(file)
    img_list = convert_image(data_path + file, pixel_density)
    data_set = [img_list, desired_output]

    data_list.append(data_set)

    if file_number == 5:
        break

    file_number += 1

# print(data_list)
print(file_number)
