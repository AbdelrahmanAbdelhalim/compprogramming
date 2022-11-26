// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

// You must write an algorithm that runs in O(n) time.

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

    pub fn copied_solution(nums: Vec<i32>) -> i32 {
        ///interesting rust stuff here that I want to take a look at 
        let mut set = nums.into_iter().collect::<HashSet<i32>>();
        let mut longest_streak = 0;
        for i in set.iter().copied() {
            if !set.contains(&(i - 1)) {
                let mut current_num = i;
                let mut current_streak = 1;
                
                while set.contains(&(current_num + 1)) {
                    current_num += 1;
                    current_streak += 1;
                }
                
                longest_streak = longest_streak.max(current_streak);
            }
        }
        longest_streak
    }

}
