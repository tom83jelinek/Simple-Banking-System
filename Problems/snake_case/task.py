def to_snake_case(string_to_convert):
    converted_string = ''

    for letter in string_to_convert:
        if letter.islower():
            converted_string += letter
        elif letter.isupper():
            converted_string += ('_' + letter.lower())

    return converted_string


print(to_snake_case(input()))
