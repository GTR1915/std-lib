array = [2, 8, 15, 17, 20, 28, 29, 29, 30, 30, 38, 43, 44, 44, 45, 47, 47, 48, 49, 50]

def left_search(arr: list, target):
    low, high = 0, len(arr)  # [low, high)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:  # arr[mid] >= target
            high = mid
    return low if low < len(arr) and arr[low] == target else -1

def right_search(arr: list, target):
    low, high = 0, len(arr)  # [low, high)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:  # arr[mid] >= target
            high = mid
    return low-1 if low-1 >= 0 and arr[low-1] == target else -1

print(left_search(array, 30))
print(right_search(array, 30))

