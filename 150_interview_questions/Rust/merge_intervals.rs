///Problem Statement
// Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
impl Solution {
    ///Solution Performance
    ///Runtime 17 ms Beats 19.53% Memory 3 MB Beats 53.25%
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        use std::cmp;
        let mut ans: Vec<Vec<i32>> = vec![];
        intervals.sort_by(|a,b| a[0].cmp(&b[0]));
        for i in intervals.into_iter() {
            if let Some(last) = ans.last_mut() {
                if cmp::max(last[0], i[0]) <= cmp::min(last[1], i[1]) {
                    last[1] = cmp::max(i[1],last[1]);
                }else {
                    ans.push(i);
                }
            }else {
                ans.push(i);
            }
        }
        ans
    }
}