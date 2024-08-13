#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

def print_stats(total_file_size, status_counts):
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")

def signal_handler(sig, frame):
    print_stats(total_file_size, status_counts)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_file_size = 0
status_counts = defaultdict(int)
line_count = 0

for line in sys.stdin:
    parts = line.split()
    if len(parts) >= 7:
        try:
            # Extract the file size and status code from the line
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                total_file_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_file_size, status_counts)
                    # Reset counts for the next batch of 10 lines
                    total_file_size = 0
                    status_counts = defaultdict(int)
        except ValueError:
            # Ignore lines with invalid file size or status code
            continue

