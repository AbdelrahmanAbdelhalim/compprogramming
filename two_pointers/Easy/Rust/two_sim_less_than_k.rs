///Problem Statement:
///Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

impl Solution {
    pub fn two_sum_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        ///Two pointer solution
        ///Performance: Runtime: 1ms Memory: 2.1MB
        use std::cmp;
        let mut nums = nums;
        nums.sort();
        let mut right = nums.len() - 1;
        let mut left = 0;
        let mut maxim = std::i32::MIN;
        while left < right {
            if nums[right] + nums[left] >= k {
                right -= 1;
            }else if nums[right] + nums[left] < k {
                maxim = cmp::max(maxim, nums[right] + nums[left]);
                left += 1;
            }
        }
        if maxim != std::i32::MIN {
            return maxim
        }else {
            return -1;
        }
    }
}
