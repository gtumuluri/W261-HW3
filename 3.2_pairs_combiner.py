#!/usr/bin/python
import sys
import ast

# Temp variables to track
# key changes and new counts
prev_key = None
count = 0

# Read output from standard input, aggregate counts
# of common keys (including order inversions), and
# output back the key and aggregate count.
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')

    key = ast.literal_eval(items[0])
    value = int(items[1])
    if key == prev_key:
        count += value
    else:
        # Key changed, time to output the previous one.
        if prev_key is not None:
            print '%s\t%s' % (prev_key, count)
        count = value

    prev_key = key

# Don't forget to output the last key that we just counted.
print '%s\t%s' % (prev_key, count)