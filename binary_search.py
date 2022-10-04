# Binary Search 


def binary_itr(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid

    return start


arr = [2, 5, 8, 9, 10, 16, 22]
target = 10

print(binary_itr(arr, 0, len(arr) - 1, target))