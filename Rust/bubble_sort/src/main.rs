fn main() {
    let mut arr = [1, 7, 4, 1, 10, 9, -2];
    println!("Unsorted Array: {:?}", arr);

    bubble_sort(&mut arr);
    println!("Sorted Array: {:?}", arr);
}

fn bubble_sort<T: Ord>(arr: &mut [T]) {
    let n = arr.len();

    for i in 0..n {
        for j in 0..(n - i - 1) {
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1)
            }
        }
    }
}
