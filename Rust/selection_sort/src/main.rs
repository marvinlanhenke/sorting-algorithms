fn main() {
    let mut arr = [1, 7, 4, 1, 10, 9, -2];
    println!("Unsorted Array: {:?}", arr);

    selection_sort(&mut arr);
    println!("Sorted Array: {:?}", arr);
}

fn selection_sort<T: Ord>(arr: &mut [T]) {
    let n = arr.len();

    for i in 0..n {
        let mut min_idx = i;
        for j in (i + 1)..n {
            if arr[j] < arr[min_idx] {
                min_idx = j;
            }
        }
        arr.swap(i, min_idx);
    }
}
