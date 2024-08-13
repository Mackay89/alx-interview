#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """Print the metrics for file size and status codes."""
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes):
        print(f"{status_code}: {status_codes[status_code]}")

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) == 7 and parts[2] == '-' and parts[3] == '[':
                try:
                    file_size = int(parts[6])
                    status_code = int(parts[5])
                    if status_code in status_codes:
                        total_size += file_size
                        status_codes[status_code] += 1
                except ValueError:
                    continue
            
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
        
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()

