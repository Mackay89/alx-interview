#!/usr/bin/python3
"""UTF-8 validation module.
"""

def validUTF8(data):
    """Checks if a given list of integers data set represents a valid UTF-8 encoding.

    A character in UTF-8 can be 1 to 4 bytes long.
    The data set can contain multiple characters.
    The data will be represented by a list of integers.

    Args:
        data (list): A list of integers where each integer represents a byte
        of the data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    for num in data:
        if n_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if num >> 7 == 0:
                # 1-byte character (ASCII)
                continue
            elif num >> 5 == 0b110:
                n_bytes = 1
            elif num >> 4 == 0b1110:
                n_bytes = 2
            elif num >> 3 == 0b11110:
                n_bytes = 3
            else:
                return False
        else:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if num >> 6 != 0b10:
                return False
        n_bytes -= 1

    # If there are leftover bytes to be processed, return False
    return n_bytes == 0

