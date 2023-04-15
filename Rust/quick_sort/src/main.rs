fn main() {
    let mut arr = [1, 7, 4, 1, 10, 9, -2];
    println!("Unsorted Array: {:?}", arr);

    let left = 0;
    let right = arr.len() - 1;
    quick_sort(&mut arr, left, right);
    println!("Unsorted Array: {:?}", arr);
}

fn quick_sort<T: Ord>(arr: &mut [T], left: usize, right: usize) {
    if left < right {
        let pivot = partition(arr, left, right);

        if pivot > 0 {
            quick_sort(arr, left, pivot - 1);
        }
        quick_sort(arr, pivot + 1, right);
    }
}

fn partition<T: Ord>(arr: &mut [T], left: usize, right: usize) -> usize {
    let mut i = left as isize - 1;

    for j in left..right {
        if arr[j] <= arr[right] {
            i += 1;
            arr.swap(i as usize, j);
        }
    }

    let new_pivot = (i + 1) as usize;
    arr.swap(new_pivot, right);
    new_pivot
}
