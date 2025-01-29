import timeit
from functools import lru_cache

import matplotlib.pyplot as plt
import pandas as pd

from splay_tree import SplayTree  # Importing custom SplayTree implementation


@lru_cache(maxsize=1000)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def fibonacci_splay(n, tree):
    if tree.find(n) is not None:
        return tree.find(n)
    if n < 2:
        tree.insert(n, n)
        return n
    result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result


# Fibonacci test values
fib_tests = list(range(0, 950, 50))

fib_lru_times = []
fib_splay_times = []

for n in fib_tests:
    tree = SplayTree()  # New tree for each run

    lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=5) / 5
    splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=5) / 5
    fib_lru_times.append(lru_time)
    fib_splay_times.append(splay_time)

# display results as table
data = pd.DataFrame({
    'n': fib_tests,
    'LRU Cache Time (s)': fib_lru_times,
    'Splay Tree Time (s)': fib_splay_times
})
print("\nFibonacci Computation Performance Comparison:\n")
print(data.to_string(index=False))

# plot results
plt.figure()
plt.plot(fib_tests, fib_lru_times, marker='o', linestyle='-', label='LRU Cache')
plt.plot(fib_tests, fib_splay_times, marker='s', linestyle='-', label='Splay Tree')
plt.xlabel('n (Fibonacci Number)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Fibonacci Computation Time Comparison')
plt.grid()
plt.show()
