"""
Main.

Created by: Theo
Date: 24 June 2024
"""
def get_image_bits(width: int, height: int, depth: int = 32):
    """
    Calculate the required storage size of an uncompressed image.

    Arguments:
    ---------
    - depth: The bit depth of the image, or the number of bits per pixel.
    - width: The width of the image in pixels.
    - height: The height of the image in pixels.

    """
    pixels = width * height
    bit_count = pixels * depth
    print(bit_count)


get_image_bits(100, 200)


def get_string_bytes(string: str):
    """
    Calculate the required storage size of a string.

    Parameters
    ----------
    - string: The string whos size is being calculated

    """
    print(len(string) + 1)


get_string_bytes("Hello!")


def print_square(side_length: int):
    underscore_count = side_length * 2
    underscores = "_" * underscore_count
    spaces = " " * underscore_count
    print(f".{underscores}.")
    for i in range(side_length):
        print(f"|{spaces}|")
    print(f".{underscores}.")


def print_triangle(upside: bool):
    print("")


def print_rectangle(horis_side: int, verti_side: int):
    underscore_count = horis_side * 2
    underscores = "_" * underscore_count
    spaces = " " * underscore_count
    print(f".{underscores}.")
    for i in range(verti_side):
        print(f"|{spaces}|")
    print(f".{underscores}.")


print_square(5)
print_rectangle(9,2)