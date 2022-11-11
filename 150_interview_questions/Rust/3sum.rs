//Problem Statement
//Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

// A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

pub fn three_sum(mut input: Vec<i32>) -> Vec<Vec<i32>> {
    input.sort();
    let mut answer = vec![];
    for i in 0..input.len() {
        let mut right = input.len() - 1;
        let mut left = i + 1;
        let current = input[i];
        while left < right {
            if i > 0 && input[i - 1] == input[i] {
               break 
            }
            if current > 0 {
                break
            }else {
                if current + input[left] + input[right] == 0 {
                    let mut group = vec![];
                    group.push(current);
                    group.push(input[left]);
                    group.push(input[right]);
                    answer.push(group);
                    right -= 1;
                    left += 1; 
                    while left < right && input[left] == input[left - 1] {
                        left += 1;
                    }
                }else if current + input[left] + input[right] > 0 {
                    right -= 1;
                }else if current + input[left] + input[right] < 0 {
                    left += 1;
                }
            }
        }
    }
    answer
}
fn main() {
    let answer = three_sum(vec![-2,0,0,2,2]);
    dbg!("{}", answer);
}