#!/usr/bin/python3
import sys

def parse_line(line):
    """Parse a single line of log and return file size and status code."""
    try:
        parts = line.split()
        if len(parts) < 6:
            return None, None
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
            return file_size, status_code
    except ValueError:
        return None, None
    return None, None

def print_statistics(file_size_total, status_code_count):
    """Print the statistics in the required format."""
    print(f"File size: {file_size_total}")
    for status_code in sorted(status_code_count.keys()):
        print(f"{status_code}: {status_code_count[status_code]}")

def main():
    file_size_total = 0
    status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0
    
    try:
        for line in sys.stdin:
            file_size, status_code = parse_line(line)
            if file_size is not None and status_code is not None:
                file_size_total += file_size
                status_code_count[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(file_size_total, status_code_count)
                file_size_total = 0
                status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    except KeyboardInterrupt:
        print_statistics(file_size_total, status_code_count)

if __name__ == "__main__":
    main()

