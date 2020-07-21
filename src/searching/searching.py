def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    low = 0
    mid = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) //2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            low = mid -1
        else:
            return mid


    return -1  # not found
