from typing import List


def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


if __name__ == '__main__':
    arr = [1, 7, 4, 1, 10, 9, -2]

    print(f"Unsorted Array: {arr}")

    quick_sort(arr, 0, len(arr) - 1)
    print(f"Sorted Array: {arr}")
