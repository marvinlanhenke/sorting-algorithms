from typing import List


def swap(arr: List[int], left: int, right: int) -> None:
    arr[left], arr[right] = arr[right], arr[left]


def partition(arr: List[int], left: int, right: int) -> int:
    pivot_value = arr[right]

    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot_value:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, right)
    return i + 1


def quick_sort(arr: List[int], left: int, right: int) -> None:
    if left < right:
        pivot = partition(arr, left, right)

        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)


if __name__ == '__main__':
    arr = [1, 7, 4, 1, 10, 9, -2]

    print(f"Unsorted Array: {arr}")

    quick_sort(arr, 0, len(arr) - 1)
    print(f"Sorted Array: {arr}")
