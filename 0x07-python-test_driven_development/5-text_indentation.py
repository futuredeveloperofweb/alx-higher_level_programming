#!/usr/bin/python3
"""Module for text_indentation function"""


def text_indentation(text):
    """a function that prints a text with 2 new
    lines after each of these characters: ., ? and:

    Args:
        test (str): the text to print
    Returns:
        the text with new lines whenever it reacchs ". or , or ?"
    Raises:
        TypeError: if the text is not of str type
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for delim in ".?:":
        text = (delim + '\n\n').join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end='')


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')
