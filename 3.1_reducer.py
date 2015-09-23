#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

# Initialize basket size frequency dictionary,
# number of items, and a temp variable to detect
# item changes
basket_size_freq = {}
nitems = 0
prev_item = None

# Read standard input, extract item number (key)
# and basket size, and build up a count of unique
# items and the frequency distribution of the basket
# sizes.
for line in sys.stdin:
    line = line.strip()
    item, basket_size = line.split('\t')
    
    # If the item changed, increment unique item count
    if item != prev_item:
        nitems += 1
    prev_item = item
    
    # Increment the number of times a given basket size
    # occurred, after initializing default if the size
    # is found for the first time.
    basket_size_freq.setdefault(int(basket_size), 0)
    basket_size_freq[int(basket_size)] += 1

# Remove -1 from the basket sizes.
# It was just a place holder value.
basket_size_freq.pop(-1)

# Print some key statistics
print '%s\t%s' % ('Number of Unique Items:', nitems)
print '%s\t%s' % ('Largest Basket Size:', max(basket_size_freq))
print '%s\t%s' % ('Smallest Basket Size:', min(basket_size_freq))
print '%s\t%s' % ('Most Frequent Size:',
                  max(basket_size_freq, key = basket_size_freq.get))
print '%s\t%s' % ('Number of Baskets of Most Frequent Size:',
                  basket_size_freq[max(basket_size_freq,
                                       key = basket_size_freq.get)])

# Plot the histogram of the basket sizes (frequency distribution)
plt.hist(basket_size_freq.keys(), len(basket_size_freq), weights = basket_size_freq.values())
plt.xlabel('Basket Size')
plt.ylabel('Number of Baskets')
plt.ylim(0, 3000)
plt.title('Distribution of Basket Sizes')
plt.show()