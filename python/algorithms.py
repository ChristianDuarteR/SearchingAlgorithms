def ternary_search(arr, left, right, target):
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if target == arr[mid1]:
            return mid1
        elif target == arr[mid2]:
            return mid2
        elif target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)
        elif target > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, target)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)


def binary_search(arr, target, left, right):
    """
    Perform binary search on a sorted array to find the target element.

    Args:
    - arr (list): A sorted list of elements.
    - target: The element to search for within the list.
    - left (int): The left index of the current search range.
    - right (int): The right index of the current search range.

    Returns:
    - bool: True if the target element is found, False otherwise.
    """
    if left > right:
        return False

    mid = left + (right - left) // 2  # O(1)

    if arr[mid] == target:  # O(1)
        return True

    elif arr[mid] > target:  # O(1)
        return binary_search(arr, target, left, mid - 1)  # O(log n)

    else:
        return binary_search(arr, target, mid + 1, right)  # O(log n)


def linear_search(arr, target):
    """
    Perform linear search to find the target element in the array.

    Args:
    - arr (list): A list of elements.
    - target: The element to search for within the list.

    Returns:
    - bool: True if the target element is found, False otherwise.
    """
    for i in range(len(arr)):  # O(n)
        if arr[i] == target:
            return True
    return False
