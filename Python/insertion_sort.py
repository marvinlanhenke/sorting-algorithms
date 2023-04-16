from typing import List


def insertion_sort(arr: List[int]) -> None:
    if (n := len(arr)) <= 1:
        return

    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


if __name__ == '__main__':
    arr = [1, 7, 4, 1, 10, 9, -2]

    print(f"Unsorted Array: {arr}")

    insertion_sort(arr)
    print(f"Sorted Array: {arr}")