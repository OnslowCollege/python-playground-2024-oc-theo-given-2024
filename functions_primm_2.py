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
        depth: The bit depth of the image, or the number of bits per pixel.
        width: The width of the image in pixels.
        height: The height of the image in pixels.

    """
    pixels = width * height
    bit_count = pixels * depth
    print(bit_count)


get_image_bits(100, 200)


def get_string_bytes(string: str):
    """
    Calculate the required storage size of a string.

    Arguments:
    ---------
        string: The string whos size is being calculated

    """
    print(len(string) + 1)


get_string_bytes("Hello!")


def print_square(side_length: int):
    """
    Calculate the required storage size of a string.

    Arguments:
    ---------
        side_length: The length of all sides of the square

    """
    underscore_count = side_length * 2
    underscores = "_" * underscore_count
    spaces = " " * underscore_count
    print(f".{underscores}.")
    for _i in range(side_length):
        print(f"|{spaces}|")
    print(f".{underscores}.")


def print_triangle(down: bool):
    """
    Calculate the required storage size of a string.

    Arguments:
    ---------
        down: If this is true, the triangle is facing downwards

    """
    if down:
        print(".____.")
        print(r" \  / ")
        print(r"  \/  ")
    else:
        print(r"  /\  ")
        print(r" /  \ ")
        print(".____.")



def print_rectangle(horis_side: int, verti_side: int):
    """
    Calculate the required storage size of a string.

    Arguments:
    ---------
        horis_side: length of the horizontal side of the rectangle
        verti_side: length of the vertical side of the rectangle

    """
    underscore_count = horis_side * 2
    underscores = "_" * underscore_count
    spaces = " " * underscore_count
    print(f".{underscores}.")
    for _i in range(verti_side):
        print(f"|{spaces}|")
    print(f".{underscores}.")


print_square(5)
print_rectangle(10,2)
print_triangle(True)