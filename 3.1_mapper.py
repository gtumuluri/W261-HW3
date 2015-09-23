#!/usr/bin/python
import sys

# Take input from the standard input, split the line
# and output the item and the corresponding basket
# size it was found in
for line in sys.stdin:
    line = line.strip()
    items = line.split(' ')

    # We don't want to output the basket size for each
    # item found in the basket. Just for the first item.
    # For other items, output -1 for basket size.
    itemnum = 1
    for item in items:
        if itemnum == 1:
            print '%s\t%s' % (item, len(items))
        else:
            print '%s\t%s' % (item, -1)
        itemnum += 1