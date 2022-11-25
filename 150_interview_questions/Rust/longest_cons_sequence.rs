impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        use std::collections::HashSet;
        use std::i32;
        let mut ans = i32::MIN;
        let mut storage = HashSet::new();
        for i in nums.iter() {
            storage.insert(i);
        }
        for i in 0..nums.len() {
            let mut clone = nums[i];
            let mut current_streak = 1;
            if storage.contains(&(clone - 1)) {
                continue
            }
            while storage.contains(&(clone + 1)) {
                current_streak += 1;
                clone = **storage.get(&(clone + 1)).unwrap();
            } 
            if current_streak > ans {
                ans = current_streak;
            }
        }
        if ans == i32::MIN {
            return 0;
        }else {
            return ans;
        }
    }
}
