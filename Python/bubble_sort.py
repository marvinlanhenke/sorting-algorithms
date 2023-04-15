from typing import List


def bubble_sort(arr: List[int]) -> None:
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr = [1, 7, 4, 1, 10, 9, -2]

    print(f"Unsorted Array: {arr}")

    bubble_sort(arr)
    print(f"Sorted Array: {arr}")