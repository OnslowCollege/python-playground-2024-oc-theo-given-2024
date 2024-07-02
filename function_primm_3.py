def alternate_case(text: str) -> str | None:
        build_string: str = ""
        for i in range(0, len(text)):
            new_char: str = ""
            if i % 2 == 0:
                new_char = text[i].upper()
            else:
                new_char += text[i].lower()
            build_string = build_string + new_char
        return build_string


wibbly_wobbly: str = alternate_case("industrialisation")
print(wibbly_wobbly)
