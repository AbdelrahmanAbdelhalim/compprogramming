// Porblem Statement: Given a string s and an integer k, return the length of the longest
// substring
// of s that contains at most k distinct characters.
impl Solution {
    pub fn length_of_longest_substring_k_distinct(s: String, k: i32) -> i32 {
        // Solution Performance: Runtime 7 ms Beats 42.86% Memory 2.3 MB Beats 28.57%
        use std::i32;
        use std::collections::HashMap;
        let mut ans = i32::MIN;
        let mut right = 0;
        let mut left = 0;
        let mut reserve: HashMap<u8, i32> = HashMap::new();
        let s = s.as_bytes();
        while right < s.len() {
            if !reserve.contains_key(&s[right]) {
                reserve.insert(s[right], 1);
            }else {
                *reserve.get_mut(&s[right]).unwrap() += 1;
            }
            while reserve.len() > k as usize {
                *reserve.get_mut(&s[left]).unwrap() -= 1;
                if *reserve.get(&s[left]).unwrap() == 0  {
                    reserve.remove(&s[left]);
                }
                left += 1;
            }
            right += 1;
            if ans < (right - left) as i32 {
                ans = (right - left) as i32;
            }
        }
        ans
    }
}