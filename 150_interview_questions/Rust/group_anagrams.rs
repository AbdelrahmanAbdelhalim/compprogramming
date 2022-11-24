// Problem Statement
// Given an array of strings strs, group the anagrams together. You can return the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

impl Solution {
    ///Submission performance Runtime 12 ms Beats 85.46% Memory 4.1 MB Beats 97.92%
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        use std::collections::HashMap;
        let mut words : HashMap<Vec<u8>, Vec<String>> = HashMap::new();
        let mut ans = vec![];
        for word in strs.into_iter() {
            let mut word_clone = word.clone().into_bytes();
            word_clone.sort();
            if words.contains_key(&word_clone){
                words.get_mut(&word_clone).unwrap().push(word); 
            }else {
                words.insert(word_clone, vec![word]);
            }
        }

        for (_ , val) in words {
            ans.push(val);
        } 
        ans
    }
}
