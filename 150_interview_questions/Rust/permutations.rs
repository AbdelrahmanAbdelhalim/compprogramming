///Problem Statement
// Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
impl Solution {
    ///Solution Performance
    ///Runtime 20 ms Beats 6.48% Memory 2.1 MB Beats 97.22%
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut ans = vec![];
    let mut  used = vec![false; nums.len()];
    let mut sf = vec![];
    fn helper(used: &mut Vec<bool>, nums: &Vec<i32>, ans: &mut Vec<Vec<i32>>, sf: &mut Vec<i32>, tracker: usize) {
        if sf.len() == nums.len() {
            ans.push(sf.to_vec());
            return
        }
        if tracker == nums.len() {
            return
        }
        for i in 0..nums.len() {
            if !used[i] {
                helper(used, nums, ans, sf, tracker + 1);
                sf.push(nums[i]);
                used[i] = true;
                helper(used, nums, ans, sf, tracker + 1);
                used[i] = false;
                sf.pop();
            }
        }
    }
    helper(&mut used, &nums, &mut ans, &mut sf, 0);
   ans 
    }
}
