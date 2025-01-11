def find_min_max(arr):
    """
    Finds the minimum and maximum elements in an array using the divide and conquer approach.

    :param arr: List of numbers
    :return: Tuple (min_element, max_element)
    """
    # if array has only one element - base case
    if len(arr) == 1:
        return arr[0], arr[0]

    # if array has two elements - base case
    if len(arr) == 2:
        return min(arr[0], arr[1]), max(arr[0], arr[1])

    # divide array in two
    mid = len(arr) // 2
    # recursively find minimum and maximum values in left and right subarrays
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    return min(left_min, right_min), max(left_max, right_max)


if __name__ == '__main__':
    array = [3, 1, 4, 1, 5, 9, -10, 6, 5, 3, 5]
    min_value, max_value = find_min_max(array)
    print(f"Minimum: {min_value}, Maximum: {max_value}")
