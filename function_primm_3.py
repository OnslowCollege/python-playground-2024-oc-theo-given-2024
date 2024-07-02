def alternate_case(text) -> str | None:
    build_string: str = ""
    if text == isinstance(text, str):
        for i in range(0, len(text)):
            new_char: str = ""
            if i % 2 == 0:
                new_char = text[i].upper()
            else:
                new_char += text[i].lower()
            build_string = build_string + new_char
        return build_string
    else:
        return None


wibbly_wobbly = alternate_case("wait what whyyy")
print(wibbly_wobbly)
