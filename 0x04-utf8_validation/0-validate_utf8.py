#!/usr/bin/python3
"""
This module provides a method to validate UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list): A list of integers representing bytes.
    
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 7) == 0:
                # 1-byte character (ASCII), continue
                continue
            elif (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            else:
                return False
        else:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
        n_bytes -= 1

    # If there are leftover bytes to be processed, return False
    return n_bytes == 0

