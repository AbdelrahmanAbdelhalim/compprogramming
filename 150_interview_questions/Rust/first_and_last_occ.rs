impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
    if nums.len() == 0 {
        return vec![-1,-1];
    }
    let mut left: i32 = 0;
    let mut right = (nums.len() - 1) as i32;
    let mut directly_smaller_idx = -1;
    let mut directly_bigger_idx = -1;
    while left <= right {
        let mid = ((left + right) / 2) as usize;
        if nums[mid] <= target {
            directly_smaller_idx = mid as i32;
            left = mid as i32 + 1;
        }else {
            right = mid as i32 - 1 ;
        }
    }
    println!("{}", directly_smaller_idx);
    left = 0;
    right = (nums.len() - 1) as i32;
    while left <= right {
        let mid = ((left + right) / 2) as usize;
        if nums[mid] >= target {
            directly_bigger_idx = mid as i32;
            right = mid as i32 - 1;
        }else {
            left = mid as i32 + 1;
        }
    }
    println!("{}", directly_bigger_idx);
    if directly_bigger_idx == -1 || directly_smaller_idx == -1 {
        return vec![-1,-1];
    }
    if directly_bigger_idx == directly_smaller_idx + 1{
        return vec![-1,-1];
    }
    return vec![ directly_bigger_idx, directly_smaller_idx,];
}
}
