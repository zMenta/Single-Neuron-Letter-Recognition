import os
from image_processing import convert_image


def generate_data(folder_path: str, desired_output: float, image_pixel_size: int) -> list:
    """Converts all images from a folder to a list and the desired output of this image.

    Args:
        folder_path (str): Path to the folder that contains the images.
        desired_output (float): Desired output for this image group.
        image_pixel_size (int): Convert the image to be pixel X pixel size.

    Returns:
        list: List containing images data [ [image_data1, desired_output ] ... [ image_data2, desired_output ] ]
    """
    data_list = []

    for file in os.listdir(folder_path):
        # file is str
        img_list = convert_image(folder_path + file, image_pixel_size)
        data_set = [img_list, desired_output]

        data_list.append(data_set)

    return data_list
