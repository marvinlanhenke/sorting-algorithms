from typing import List


def merge_sort(arr: List[int]) -> None:
    if (n := len(arr)) <= 1:
        return

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    #store remaining elements
    arr[k:] = left[i:] + right[j:]


if __name__ == '__main__':
    arr = [1, 7, 4, 1, 10, 9, -2]

    print(f"Unsorted Array: {arr}")

    merge_sort(arr)
    print(f"Sorted Array: {arr}")