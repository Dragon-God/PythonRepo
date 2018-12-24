Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from __future__ import division, print_function
import random

total_samples = 0
good_heads    = 0
good_samples  = 0
N = 10 # 20 coins total
while True:
    try:
        # flip 2 * N coins; 1 = heads, 0 = tails
        coins = tuple(random.randint(0, 1) for _ in range(2 * N))
        total_samples += 1
        # choose a random half
        A = frozenset(random.sample(range(2 * N), N))
        # reject sample if not all coins in the subset are heads
        if not all(coins[i] for i in A):
            continue
        # sum heads in the complement subset
        heads = sum(c for i, c in enumerate(coins) if i not in A)
        print('{} heads'.format(heads))
        good_samples += 1
        good_heads += heads
    except KeyboardInterrupt:
        break

print()
print('{} total samples, {} good samples ({:.2}%)'.format(
    total_samples, good_samples, 100 * good_samples / total_samples))
print('{} heads in good samples, average: {}'.format(
    good_heads, good_heads / good_samples))
