from PIL import Image


im = Image.open("godot_image")

# im.show()

processed_image = im.resize((20, 20))

image_data = list(processed_image.getdata())

print(image_data[0])

print(len(image_data))

# print(processed_image.histogram())
