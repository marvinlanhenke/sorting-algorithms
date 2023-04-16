function insertionSort(arr) {
    const n = arr.length;

    if (n <= 1) return;

    for (let i = 1; i < n; i++) {
        let j = i;
        while (j > 0 && arr[j] < arr[j - 1]) {
            [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]];
            j -= 1;
        }
    }
}

const arr = [1, 7, 4, 1, 10, 9, -2];
console.log(`Unsorted Array: ${arr}`);

insertionSort(arr);
console.log(`Sorted Array: ${arr}`);
