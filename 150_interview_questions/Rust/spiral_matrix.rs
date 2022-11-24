// Given an m x n matrix, return all elements of the matrix in spiral order.
impl Solution {
    ///Performance numbers seem inaccurate. A massive improvement here is to mark the cells in place as visited with a certai vaue
    ///Dropping the space complexity from O(MxN) to O(1). The bounds on the question help in acheiving that where the numbers in the
    ///matrix are between -100 and 100
    pub fn spiral_order(nums: Vec<Vec<i32>>) -> Vec<i32> {
        use std::collections::HashSet;
        let mut visited = HashSet::new();
        let mut direction: u8 = 0;
        let mut ans = vec![];
        let mut i: i32 = 0; let mut j: i32 = 0 ;
        while ans.len() != nums.len() * nums[0].len() {
            ans.push(nums[i as usize][j as usize]);
            visited.insert((i,j));
            if direction == 0 {
                if j + 1 >= nums[0].len() as i32 || visited.contains(&(i,j + 1)){
                    direction = 1;
                    i += 1;
                }else {
                    j += 1;
                }
            }else if direction == 1 {
                if i + 1 >= nums.len() as i32|| visited.contains(&(i + 1,j)){
                    direction = 2;
                    j -= 1;
                }else {
                    i += 1;
                }
            }else if direction == 2 {
                if j - 1 < 0 || visited.contains(&(i,j - 1)){
                    direction = 3;
                    i -= 1;
                }else {
                    j -= 1
                }
            }else if direction == 3 {
                if i - 1 < 0 || visited.contains(&(i - 1 ,j)){
                    direction = 0;
                    j += 1;
                }else {
                    i -= 1;
                }
            
            }
        }
        ans
    }
}
