array = [2, 8, 15, 17, 20, 28, 29, 29, 30, 30, 38, 43, 44, 44, 45, 47, 47, 48, 49, 50]

# left_search only returns the index if target is actually present and returns -1 otherwise.
def left_search(arr: list, target):
    low, high = 0, len(arr)  # [low, high)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:  # arr[mid] >= target
            high = mid
    return low if low < len(arr) and arr[low] == target else -1

# right_search only returns the index if target is actually present and returns -1 otherwise.
def right_search(arr: list, target):
    low, high = 0, len(arr)  # [low, high)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:  # arr[mid] >= target
            high = mid
    return low-1 if low-1 >= 0 and arr[low-1] == target else -1

# bisect_left always returns the index where x should be inserted to keep the list sorted, even if x is not in the list.
def bisect_left(arr: list, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:     # move right if value is too small
            left = mid + 1
        else:                # value >= x → possible answer, shrink right
            right = mid
    return left

# bisect_right always returns the index where x should be inserted to keep the list sorted, even if x is not in the list.
def bisect_right(arr: list, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:    # move right if value ≤ x
            left = mid + 1
        else:                #3 value > x → shrink right
            right = mid
    return left


def binary_search_by_range(arr: list, low, high):
    left = bisect_left(arr, low)
    right = bisect_right(arr, high)
    return arr[left : right]


print(left_search(array, 30))
print(right_search(array, 30))
print(binary_search_by_range(array, 21, 42))


