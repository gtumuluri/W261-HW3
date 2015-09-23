#!/usr/bin/python
import sys
import ast

# Maintain an item frequency map using dict.
item_freq = {}


# Temp variable to track key changes.
prev_item = None

# Read standard input, extract the 2-tuple and the
# count of occurrences, and aggregte them in the
# above dict.
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')

    # Convert two-tuple string into a
    # python tuple and the count value.
    key = ast.literal_eval(items[0])
    value = int(items[1])
    
    # If key is same, keep adding up the count.
    # Otherwise, start a new counter after initializing
    # a new key in the dict.
    if key == prev_item:
        item_freq[key[0]][key[1]] += value
    else:
        item_freq.setdefault(key[0], {})
        item_freq[key[0]][key[1]] = value

    # Keep track of key changes.
    prev_item = key

# Walk through the item frequency map and
# build a list of frequent 1-itemsets (items
# with 100 or more occurrences)
freq_itemsets_one = []
for key in item_freq:
    if item_freq[key]['*'] >= 100:
        freq_itemsets_one.append(key)
print 'Number of frequent 1-item sets:', len(freq_itemsets_one)

# Walk through the 1-item sets, and review the full
# n-squared possible two item sets and see if they
# have sufficient frequncy of co-occurrence (100) and
# add them to the 2-itemset if they do.
freq_itemsets_two = []
for item in freq_itemsets_one:
    for peer in freq_itemsets_one:
        if (item == peer or
            peer not in item_freq[item] or
            item_freq[item][peer] < 100):
            continue
        if ((item, peer) in freq_itemsets_two or
           (peer, item) in freq_itemsets_two):
            continue

        if item < peer:
            freq_itemsets_two.append((item, peer, item_freq[item][peer]))
        else:
            freq_itemsets_two.append((peer, item, item_freq[peer][item]))
print 'Number of frequent 2-item sets:', len(freq_itemsets_two)

# Walk through the 2-itemset list and compute confidence.
# Remember, the item pairs are already in the lexical order
# since our mapper did that job for us.
freq_itemsets_two_conf = []
for item in freq_itemsets_two:
    conf = round(item[2] * 1.0 / item_freq[item[0]]['*'], 2)
    freq_itemsets_two_conf.append((item[0], item[1], conf))

# Sort the 2-itemset confidence map by confidence score first in
# descending order, and by item ID next, in lexical order.
freq_itemsets_two_conf = sorted(freq_itemsets_two_conf,
                                key = lambda(x): (-x[2], x[0]))

# Output the first five entries in the list.
print '\nTop Five Rules with Confidence Scores:'
for item in freq_itemsets_two_conf[:5]:
    print item