//Problem Statement
//Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

// A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


impl Solution {
    ///Performance of submission
    /// Runtime: 2 ms, faster than 50.28% of Rust online submissions for Letter Combinations of a Phone Number.
    // Memory Usage: 2.1 MB, less than 88.27% of Rust online submissions for Letter Combinations of a Phone Number.

    pub fn letter_combinations(input: String) -> Vec<String>{
        use std::collections::HashMap;
        let mut mappings: HashMap<char, Vec<char>> = HashMap::new();
        mappings.insert('2', Vec::from(['a','b','c']));
        mappings.insert('3', Vec::from(['d','e','f']));
        mappings.insert('4', Vec::from(['g','h','i']));
        mappings.insert('5', Vec::from(['j','k','l']));
        mappings.insert('6', Vec::from(['m','n','o']));
        mappings.insert('7', Vec::from(['p','q','r', 's']));
        mappings.insert('8', Vec::from(['t','u','v']));
        mappings.insert('9', Vec::from(['w','x','y', 'z']));

        let mut sf = String::new();
        let mut answer = Vec::new();
        let tracker = 0;

        if input.len() == 0 {
         return vec![];
        }
        
        fn helper(mappings: &HashMap<char, Vec<char>>, tracker: usize, input: &String, answer: &mut Vec<String>, sf: &mut String){
            if tracker == input.len() {
                answer.push(sf.clone());
                return;
            }
            let current = input.chars().nth(tracker).unwrap();
            let chars = mappings.get(&current).unwrap();
            for character in chars { 
                sf.push(*character);
                helper(mappings, tracker + 1, &input, answer, sf);
                sf.pop();
            }
        }
        
        helper(&mappings, tracker, &input, &mut answer, &mut sf);
        return answer;
    }
}