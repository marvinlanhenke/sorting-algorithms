function insertionSort(arr) {
    const n = arr.length;

    for (let i = 0; i < n; i++) {
        let minIdx = i;
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];
    }
}

const arr = [1, 7, 4, 1, 10, 9, -2];
console.log(`Unsorted Array: ${arr}`);

insertionSort(arr);
console.log(`Sorted Array: ${arr}`);
