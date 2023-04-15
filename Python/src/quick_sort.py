from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [n for n in arr if n < pivot]
    middle = [n for n in arr if n == pivot]
    right = [n for n in arr if n > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(f"Unsorted Array: {arr}")

    print(f"Sorted Array: {quick_sort(arr)}")
