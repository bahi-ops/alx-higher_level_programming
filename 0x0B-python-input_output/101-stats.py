#!/usr/bin/python3
"""Reads from standard input and computes metrics
"""

def print_stats(size, status_codes):
    """Print accumulated metrics
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.strip().split('\t')  # Assuming tab-separated input
            
            try:
                if len(line) >= 3:
                    size += int(line[-1])
                    
                    if line[-2] in valid_codes:
                        status_codes[line[-2]] = status_codes.get(line[-2], 0) + 1
            except (IndexError, ValueError):
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
