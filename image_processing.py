from PIL import Image


def average(tuple_data: tuple) -> float:
    if type(tuple_data) != tuple:
        return tuple_data

    return sum(tuple_data) / len(tuple_data)


def convert_image(image_path: str, resize_value: int) -> list:
    """Resizes and convert the image pixels to a binary list.

    Args:
        image_path (string): Path to the image.
        resize_value (int): Value in pixels to resize the image. Converts the image to resize_value X resize_value pixels.

    Returns:
        list: Binary list of pixels in the image.
    """
    image = Image.open(image_path)
    image = image.resize((resize_value, resize_value))
    image_data = list(image.getdata())

    bit_image = []
    for pixel in image_data:
        color_average = average(pixel)
        # 127.7 = 255 / 2
        # value = 1 if color_average >= 127.5 else 0

        bit_image.append(color_average)

    return bit_image
