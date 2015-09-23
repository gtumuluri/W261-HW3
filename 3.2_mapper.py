#!/usr/bin/python

import sys

item_freq = {}

# Take input from the standard input
for line in sys.stdin:
    line = line.strip()
    items = line.split(' ')

    for item in items:
        item_freq.setdefault(item, {'*': 0})
        item_freq[item]['*'] += 1
        for peer in items:
            if peer != item:
                item_freq[item].setdefault(peer, 0)
                item_freq[item][peer] += 1

for item in item_freq:
    print '%s\t%s' % (item, item_freq[item])
