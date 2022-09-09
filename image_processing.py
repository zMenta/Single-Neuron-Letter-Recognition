from audioop import avg
from PIL import Image


def average(tuple_data: tuple) -> float:
    return sum(tuple_data) / len(tuple_data)


im = Image.open("godot_image")


processed_image = im.resize((20, 20))

image_data = list(processed_image.getdata())

bit_image = []
for pixel in image_data:
    color_average = average(pixel)

    value = 1 if color_average >= 127.5 else 0

    bit_image.append(value)

print(bit_image)
