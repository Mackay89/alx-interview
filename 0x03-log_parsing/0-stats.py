#!/usr/bin/python3
import sys
import signal
import re
from collections import defaultdict

# Initialize data structures
status_codes = defaultdict(int)
total_size = 0
line_count = 0

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def process_line(line):
    global total_size, line_count
    pattern = r'(\d+\.\d+\.\d+\.\d+) - \[(.*)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    match = re.match(pattern, line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
            status_codes[status_code] += 1
            total_size += file_size
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    try:
        for line in sys.stdin:
            process_line(line)
    except KeyboardInterrupt:
        print_stats()

