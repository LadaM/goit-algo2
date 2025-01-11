def quick_select(arr, k):
    """
    Finds the k-th smallest element in an unsorted array using the [Quick Select](https://en.wikipedia.org/wiki/Quickselect) algorithm.

    :param arr: List of numbers
    :param k: Index of the k-th smallest element (1-based)
    :return: the k-th smallest element
    """
    if len(arr) == 1:
        return arr[0]

    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and the length of the array")

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return quick_select(left, k)
    elif k <= len(left) + len(middle):
        return pivot
    else:
        return quick_select(right, k - len(left) - len(middle))


if __name__ == "__main__":
    array = [3, 2, 1, 5, 4, 6]
    k = 6
    kth_smallest = quick_select(array, k)
    print(f"The {k}-th smallest element is: {kth_smallest}")
