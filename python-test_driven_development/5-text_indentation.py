#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in characters:
            result += "\n\n"
            # Skip any following spaces
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    # Print the result with stripped lines
    print("\n".join([line.strip() for line in result.split("\n")]))

