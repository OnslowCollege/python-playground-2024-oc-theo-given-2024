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
    Calculate the price of items using the op, dp and noi. (F u line limit).

    Arguments:
    ---------
        op: The text that is going wibbly wobbly
        dp: 1
        noi: 2

    Returns: The resulting discounted price or "None" if that is not possible.

    """
    if op < 0 or 1 < dp < 0 or noi <= 0:
        return (None)
    result_cost = ((op * dp) * noi)
    return 
    

print (calculate_discounted_cost(5, 0.8, 10))