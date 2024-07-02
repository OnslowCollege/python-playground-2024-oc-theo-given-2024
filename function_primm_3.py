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

wibbly_wobbly = alternate_case("13435635463546")
print(wibbly_wobbly)

def calculate_discounted_cost(op: float, dp: float, noi: int):
    print("")