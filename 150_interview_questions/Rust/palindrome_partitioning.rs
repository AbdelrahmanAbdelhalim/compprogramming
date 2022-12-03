///Problem Statement: Given a string s, partition s such that every substring of the partition is a palindrome . Return all possible palindrome partitioning of s.
impl Solution {
    ///Solution Performance: Runtime 123 ms Beats 78.57% Memory 20.7 MB Beats 70%
    fn is_palindrome(word: &str) -> bool {
        let word = word.as_bytes();
        let mut l: i32 = 0;
        let mut r: i32 = word.len() as i32 - 1;
        while r >= l {
            if word[r as usize] != word[l as usize] {
                return false;
            }
            l += 1;
            r -= 1;
        }
        true
    }
    pub fn partition(s: String) -> Vec<Vec<String>> {
        let mut ans = vec![];
        let mut sf = vec![];
        fn traverse(sf: &mut Vec<String>, ans: &mut Vec<Vec<String>>, s: &str) {
            if s.len() <= 0 {
                ans.push(sf.clone());
            }
            for (i, _) in s.chars().enumerate() {
                let branch = &s[0..=i];      
                if Solution::is_palindrome(branch) {
                    sf.push(branch.to_string());
                    traverse(sf, ans, &s[i + 1..]);
                    sf.pop();
                }

            }
        }
        traverse(&mut sf, &mut ans, &s[..]);
        ans
    }
}
