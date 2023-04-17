function mergeSort(arr) {
    const n = arr.length;

    if (n <= 1) return;

    const mid = Math.floor(n / 2);
    const left = arr.slice(0, mid);
    const right = arr.slice(mid, n);

    mergeSort(left);
    mergeSort(right);

    let [i, j, k] = [0, 0, 0];
    while (i < left.length && j < right.length) {
        if (left[i] < right[j]) {
            arr[k] = left[i];
            i += 1;
        } else {
            arr[k] = right[j];
            j += 1;
        }
        k += 1;
    }
    arr.splice(k, arr.length - k, ...left.slice(i), ...right.slice(j));
}

const arr = [1, 7, 4, 1, 10, 9, -2];
console.log(`Unsorted Array: ${arr}`);

mergeSort(arr);
console.log(`Sorted Array: ${arr}`);
