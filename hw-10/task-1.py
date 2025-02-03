import random
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


if __name__ == "__main__":
    array_sizes = [10_000, 50_000, 100_000, 500_000]
    num_repeats = 5

    results = {"Array Size": [], "Randomized QuickSort (s)": [], "Deterministic QuickSort (s)": []}

    for size in array_sizes:
        # test data
        test_array = [random.randint(0, 1_000_000) for _ in range(size)]

        # measure the execution time for Randomized QuickSort
        randomized_times = []
        for _ in range(num_repeats):
            test_copy = test_array.copy()
            start_time = time.time()
            randomized_quick_sort(test_copy)
            randomized_times.append(time.time() - start_time)

        results["Array Size"].append(size)
        results["Randomized QuickSort (s)"].append(np.mean(randomized_times))

        # measure the execution time for Deterministic QuickSort
        deterministic_times = []
        for _ in range(num_repeats):
            test_copy = test_array.copy()
            start_time = time.time()
            deterministic_quick_sort(test_copy)
            deterministic_times.append(time.time() - start_time)

        results["Deterministic QuickSort (s)"].append(np.mean(deterministic_times))

    df_results = pd.DataFrame(results)

    plt.figure(figsize=(10, 6))
    plt.plot(df_results["Array Size"], df_results["Randomized QuickSort (s)"], marker='o', label="Randomized QuickSort")
    plt.plot(df_results["Array Size"], df_results["Deterministic QuickSort (s)"], marker='s',
             label="Deterministic QuickSort")

    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (s)")
    plt.title("Performance Comparison of QuickSort Variants")
    plt.legend()
    plt.grid(True)
    plt.show()
