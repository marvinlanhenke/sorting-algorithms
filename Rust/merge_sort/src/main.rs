fn main() {
    let mut arr = [1, 7, 4, 1, 10, 9, -2];
    println!("Unsorted Array: {:?}", arr);

    merge_sort(&mut arr);
    println!("Sorted Array: {:?}", arr);
}

fn merge_sort(arr: &mut [i32]) {
    let n = arr.len();

    if n <= 1 {
        return;
    }

    let mid = n / 2;
    let (left, right) = arr.split_at_mut(mid);
    merge_sort(left);
    merge_sort(right);

    let mut tmp_arr: Vec<i32> = Vec::with_capacity(n);
    let (mut i, mut j) = (0, 0);

    while i < left.len() && j < right.len() {
        if left[i] < right[j] {
            tmp_arr.push(left[i]);
            i += 1;
        } else {
            tmp_arr.push(right[j]);
            j += 1;
        }
    }
    tmp_arr.extend_from_slice(&left[i..]);
    tmp_arr.extend_from_slice(&right[j..]);
    arr.copy_from_slice(&tmp_arr);
}
