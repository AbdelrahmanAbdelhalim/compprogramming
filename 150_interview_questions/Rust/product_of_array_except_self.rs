// Problem Statement: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// You must write an algorithm that runs in O(n) time and without using the division operation.
impl Solution {
    // Solution Performance: Runtime 12 ms Beats 84.75% Memory 3.2 MB Beats 71.19%
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> { 
        let mut ans = vec![];
        let mut num_zeros = 0;
        let mut product_no_zero = 1;
        let mut product = 1;
        for i in nums.iter() {
            product *= i;
            if *i != 0 {
                product_no_zero *= i;
            }else {
                num_zeros += 1;
            } 
        }

        if num_zeros > 1 {
            product_no_zero = 0;
        }

        for (_, val) in nums.into_iter().enumerate() {
            if val != 0 {
                ans.push(product / val);
            }else {
                ans.push(product_no_zero);
            }
        }
        ans
    }
}