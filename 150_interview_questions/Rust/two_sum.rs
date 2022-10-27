///Problem Statement
///Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
///You may assume that each input would have exactly one solution, and you may not use the same element twice.
///You can return the answer in any order.


impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;
        use std::vec::Vec;
        let mut diffs = HashMap::new();
        let mut ans = Vec::new();
        for i in 0..nums.len() {
            let key = target - nums[i];
            if diffs.contains_key(&key) {
                ans.push(diffs[&key] as i32);
                ans.push(i as i32);
                return ans
            }
            diffs.insert(nums[i], i);

        }
    vec![]
    }
}
