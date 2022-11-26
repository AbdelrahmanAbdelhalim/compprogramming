// Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    /// Solution performance Runtime 1 ms Beats 50% Memory 2.4 MB Beats 13.64%

    pub fn zigzag_level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        if root == None {
            return Vec::new();
        }
        use std::collections::VecDeque;
        let mut ans = vec![];
        let mut stack = VecDeque::new();
        let mut order = false ;
        stack.push_back(root.unwrap());
        while stack.len() > 0 {
            let mut level = vec![];
            for i in 0..stack.len() {
                let parent: Rc<RefCell<TreeNode>>;
                parent = stack.pop_front().unwrap();
                level.push(parent.borrow().val);
                if let Some(left_child) = parent.borrow().left.to_owned() {
                    stack.push_back(left_child);
                };
                if let Some(right_child) = parent.borrow().right.to_owned() {
                    stack.push_back(right_child);
                };
            }
            if order {
                level.reverse();
            }
            ans.push(level);
            order = !order;
        } 
        println!("{:?}", ans);
        ans
    }
}
