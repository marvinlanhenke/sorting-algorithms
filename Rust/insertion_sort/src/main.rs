fn main() {
    let mut arr = [1, 7, 4, 1, 10, 9, -2];
    println!("Unsorted Array: {:?}", arr);

    insertion_sort(&mut arr);
    println!("Sorted Array: {:?}", arr);
}

fn insertion_sort<T: Ord>(arr: &mut [T]) {
    for i in 1..arr.len() {
        let mut j = i;
        while j > 0 && arr[j] < arr[j - 1] {
            arr.swap(j, j - 1);
            j = j - 1;
        }
    }
}
