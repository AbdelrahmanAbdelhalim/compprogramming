// Problem Statement: Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
impl Solution {
    // Solution Performance: Runtime 3 ms Beats 37.66% Memory 2.3 MB Beats 20.78%
    pub fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        use std::collections::HashMap;
        let mut ans = vec![];
        let mut reserve: HashMap<i32, i32> = HashMap::new();
        for i in nums1.into_iter() {
            if !reserve.contains_key(&i) {
                reserve.insert(i, 1);
            }else {
                *reserve.get_mut(&i).unwrap() += 1;
            }
        }

        for j in nums2.into_iter() {
            if reserve.contains_key(&j){
                *reserve.get_mut(&j).unwrap() -= 1;
                if  *reserve.get_mut(&j).unwrap() >= 0 {
                    ans.push(j);
                }
            }
        }
        ans
    }
}
