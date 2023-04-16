from typing import List


def selection_sort(arr: List[int]) -> None:
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    arr = [1, 7, 4, 1, 10, 9, -2]

    print(f"Unsorted Array: {arr}")

    selection_sort(arr)
    print(f"Sorted Array: {arr}")