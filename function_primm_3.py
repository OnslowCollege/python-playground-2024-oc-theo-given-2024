"""WIBBLY WOBBLY."""
def alternate_case(text: str) -> str | None:
    """
    Make a strings characters alternate between being uppercase and lowercase.

    Arguments:
    ---------
        text: The text that is going wibbly wobbly

    Returns: The resulting wobbly text or "None" if that is not possible.

    """
    build_string: str = ""
    if isinstance(text, str):
        for i in range(0, len(text)):
            new_char: str = ""
            if i % 2 == 0:
                new_char = text[i].upper()
            else:
                new_char += text[i].lower()
            build_string = build_string + new_char
        return build_string
    return None

wibbly_wobbly = alternate_case("oh. i see.")
print(wibbly_wobbly)

def calculate_discounted_cost(op: float, dp: float, noi: int) -> float | None:
    """
    Calculate the price of items using the op, dp and noi.

    Arguments:
    ---------
        op: length of the horizontal side of the rectangle
        dp: length of the vertical side of the rectangle
        noi: blah blah blah

    Returns:
    -------
        The resulting cost in a float format

    """
    if op < 0 or 1 < dp < 0 or noi <= 0:
        return (None)
    return (op * (1-dp) * noi)

result_cost = (calculate_discounted_cost(5, 0.25, 10))
print (result_cost)

def get_square(side_length: int) -> str:
    """
    Return a square of specified side length.

    Arguments:
    ---------
        side_length: The length of all sides of the square

    Returns:
    -------
        The entire square in a string format

    """
    underscore_count = side_length * 3
    underscores = "_" * underscore_count
    spaces = " " * underscore_count
    
    square: str = (f".{underscores}.")
    for _i in range(side_length):
        square = square + (f"\n|{spaces}|")
    return square + (f"\n.{underscores}.")

def get_triangle(down: bool):
    """
    Return a triangle, Parameter decides if this is facing downwards or not.

    Arguments:
    ---------
        down: If this is true, the triangle is facing downwards

    Returns:
    -------
        The entire triangle in a string format

    """
    if down:
        triangle = (".____.")
        triangle = triangle + ("\n \\  / ")
        return(triangle + ("\n  \\/  "))
    triangle = (r"  /\  ")
    triangle = triangle + ("\n /  \\ ")
    return(triangle + ("\n.____."))

def get_rectangle(horis_side: int, verti_side: int):
    """
    Return a rectangle where lengths of both sides are specified.

    Arguments:
    ---------
        horis_side: length of the horizontal side of the rectangle
        verti_side: length of the vertical side of the rectangle

    Returns:
    -------
        The entire rectangle in a string format

    """
    underscore_count = horis_side * 3
    underscores = "_" * underscore_count
    spaces = " " * underscore_count
    
    rectangle = (f".{underscores}.")
    for _i in range(verti_side):
        rectangle = rectangle +(f"\n|{spaces}|")
    return(rectangle + f"\n.{underscores}.")


square = (get_square(3))
triangle = (get_triangle(False))
rectangle = (get_rectangle(6,3))
print (square)
print (triangle)
print (rectangle)