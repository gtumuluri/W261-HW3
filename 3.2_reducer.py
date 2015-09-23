#!/usr/bin/python
import sys
import ast

item_freq = {}
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    d = ast.literal_eval(items[1])

    item_freq.setdefault(items[0], d)

freq_itemsets_one = []
for key in item_freq:
    if item_freq[key]['*'] >= 100:
        freq_itemsets_one.append(key)

print 'Number of frequent 1-item sets:', len(freq_itemsets_one)

freq_itemsets_two = []
for item in freq_itemsets_one:
    for peer in freq_itemsets_one[freq_itemsets_one.index(item) + 1:]:
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

freq_itemsets_two_conf = []
for item in freq_itemsets_two:
    conf = round(item[2] * 1.0 / item_freq[item[0]]['*'], 2)
    freq_itemsets_two_conf.append((item[0], item[1], conf))

freq_itemsets_two_conf = sorted(freq_itemsets_two_conf,
                                key = lambda(x): (-x[2], x[0]))

print '\nTop Five Rules with Confidence Scores:'
for item in freq_itemsets_two_conf[:5]:
    print item
