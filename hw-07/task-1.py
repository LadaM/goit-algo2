import random
import time

from lru import LRUCache

# Initialize LRU Cache
K = 1000
lru_cache_instance = LRUCache(K)


def range_sum_no_cache(array, L, R):
    return sum(array[L:R + 1])


def update_no_cache(array, index, value):
    array[index] = value


def range_sum_with_cache(array, L, R):
    key = (L, R)
    cached_result = lru_cache_instance.get(key)
    if cached_result is not None:
        return cached_result
    result = sum(array[L:R + 1])
    lru_cache_instance.put(key, result)
    return result


def update_with_cache(array, index, value):
    array[index] = value
    # invalidating the cache when a value is updated
    keys_to_remove = [key for key in lru_cache_instance.cache.keys() if key[0] <= index <= key[1]]
    for key in keys_to_remove:
        lru_cache_instance.delete(key)

if __name__ == "__main__":
    N = 100_000  # size of the array
    array = [random.randint(1, 1000) for _ in range(N)]

    Q = 50_000  # number of queries
    queries = []
    p = 0.7  # probability of range query
    for _ in range(Q):
        if random.random() < p:
            L, R = sorted(random.sample(range(N), 2))
            queries.append(("Range", L, R))
        else:
            index = random.randint(0, N - 1)
            value = random.randint(1, 1000)
            queries.append(("Update", index, value))

    # Measure execution times
    start_no_cache = time.time()
    for query in queries:
        if query[0] == "Range":
            range_sum_no_cache(array, query[1], query[2])
        else:
            update_no_cache(array, query[1], query[2])
    end_no_cache = time.time()

    time_no_cache = end_no_cache - start_no_cache

    start_with_cache = time.time()
    for query in queries:
        if query[0] == "Range":
            range_sum_with_cache(array, query[1], query[2])
        else:
            update_with_cache(array, query[1], query[2])
    end_with_cache = time.time()

    time_with_cache = end_with_cache - start_with_cache

    print(f"Time without caching: {time_no_cache:.2f} seconds")
    print(f"Time with LRU caching: {time_with_cache:.2f} seconds")
