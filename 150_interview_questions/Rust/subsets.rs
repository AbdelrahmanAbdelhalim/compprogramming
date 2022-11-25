// Given an integer array nums of unique elements, return all possible
// subsets
// (the power set).

// The solution set must not contain duplicate subsets. Return the solution in any order.
impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        ///Solution performance Runtime 0 ms Beats 100% Memory 2.1 MB Beats 71.43%
        let mut ans = vec![];
        let mut sf: Vec<i32> = vec![]; 
        fn helper(ans: &mut Vec<Vec<i32>>, sf: &mut Vec<i32>, tracker: usize, nums: &Vec<i32>) {
            if tracker == nums.len() {
                ans.push(sf.clone());
                return;
            }
            helper(ans, sf, tracker + 1, nums);
            sf.push(nums[tracker]);
            helper(ans, sf, tracker + 1, nums);
            sf.pop();
        }
        helper(&mut ans, &mut sf, 0, &nums);
        ans
    }
}
