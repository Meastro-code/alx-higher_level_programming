#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers and returns the result.

    Args:
        a: An integer or a float.
        b: An integer or a float. Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or a float.

    Returns:
        An integer: the addition of a and b.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)
