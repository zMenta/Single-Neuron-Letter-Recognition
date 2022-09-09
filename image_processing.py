from audioop import avg
from PIL import Image


def average(tuple_data: tuple) -> float:
    return sum(tuple_data) / len(tuple_data)


im = Image.open("godot_image")

# im.show()

processed_image = im.resize((20, 20))

image_data = list(processed_image.getdata())

print(image_data[10])

print(len(image_data))

print(average(image_data[10]))

# print(processed_image.histogram())
