function bubbleSort(arr) {
    const n = arr.length;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
}

const arr = [1, 7, 4, 1, 10, 9, -2];
console.log(`Unsorted Array: ${arr}`);

bubbleSort(arr);
console.log(`Sorted Array: ${arr}`);
