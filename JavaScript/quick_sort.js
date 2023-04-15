const swap = (arr, left, right) =>
    ([arr[left], arr[right]] = [arr[right], arr[left]]);

function partition(arr, left, right) {
    const pivotValue = arr[right];

    let i = left - 1;

    for (let j = left; j < right; j++) {
        if (arr[j] <= pivotValue) {
            i += 1;
            swap(arr, i, j);
        }
    }

    swap(arr, i + 1, right);
    return i + 1;
}

function quickSort(arr, left, right) {
    if (left < right) {
        let pivot = partition(arr, left, right);

        quickSort(arr, left, pivot - 1);
        quickSort(arr, pivot + 1, right);
    }
}

const arr = [1, 7, 4, 1, 10, 9, -2];
console.log(`Unsorted Array: ${arr}`);

quickSort(arr, 0, arr.length - 1);
console.log(`Sorted Array: ${arr}`);
