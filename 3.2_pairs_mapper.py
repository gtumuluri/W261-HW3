#!/usr/bin/python

import sys

# Take input from the standard input with each line
# representing a basket. Split the basket and output
# the order inversion key with count 1 as value, and also 
# co-occurring terms with count 1 as value. Only output
# lexicographically ordered pairs.
for line in sys.stdin:
    line = line.strip()
    items = line.split(' ')
    
    # Sort the items so we can benefit from
    # lexical ordering.
    items = sorted(items)

    # Double loop to output order inversions in
    # first one, and co-occurring terms in the second.
    for item in items:
        print '%s\t%s' % ((item, '*'), 1)
        # Sorted order means, we don't need to
        # iterate over whole list. Only current index
        # to last.
        for peer in items[items.index(item) + 1:]:
            print '%s\t%s' % ((item, peer), 1)