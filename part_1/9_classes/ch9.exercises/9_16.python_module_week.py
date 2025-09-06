# Seeding - from https://pymotw.com/
"""
random() produces different values each time it is called and has a very large period before it repeats any numbers. This is useful for producing unique values or variations, but there are times when having the same data set available to be processed in different ways is useful. One technique is to use a program to generate random values and save them to be processed by a separate step. That may not be practical for large amounts of data, though, so random includes the seed() function for initializing the pseudorandom generator so that it produces an expected set of values.


The seed value controls the first value produced by the formula used to produce pseudorandom numbers, and since the formula is deterministic it also sets the full sequence produced after the seed is changed. The argument to seed() can be any hashable object. The default is to use a platform-specific source of randomness, if one is available. Otherwise, the current time is used.
"""
import random

random.seed(1)

for i in range(5):
    print('{:04.3f}'.format(random.random()), end=' ')
print()
# 0.134 0.847 0.764 0.255 0.495 