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


    """
    if op < 0 or 1 < dp < 0 or noi <= 0:
        return (None)
    return (op * (1-dp) * noi)

result_cost = (calculate_discounted_cost(5, 0.25, 10))
print (result_cost)

def print_square(side_length: int):
    """
    Print a square of specified side length.

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