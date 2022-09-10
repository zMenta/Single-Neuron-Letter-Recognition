import os
from image_processing import convert_image

data_path = "Data/TrainingData/LetterA/"
data_list = []
desired_output = 1
pixel_density = 40


for file in os.listdir(data_path):
    # file is str
    img_list = convert_image(data_path + file, pixel_density)
    data_set = [img_list, desired_output]

    data_list.append(data_set)
