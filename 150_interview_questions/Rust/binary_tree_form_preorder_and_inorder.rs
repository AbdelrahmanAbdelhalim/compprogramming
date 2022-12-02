// Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}

/// Important notes:
/// I have got the idea perfectly, problems with the execution tho. The iteration part can be done much
/// more nicely. Also doing the recursion inside the struct is an idea that I was unable to come up with on
/// my own. To practice: Rc<RefCell<>>, slicing and converting vector slices to i32 slices and reviewing ref coercion
/// Reviewing better and creative ways of iterating over vectors and slices
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        fn traverse(preorder: &[i32], inorder: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
            if preorder.len() == 0 {
                return None;
            }
            let parent = preorder[0];
            let mut end = 0;
            for i in 0..inorder.len() {
                if inorder[i] == parent {
                    end = i;
                } 
            }           
            let node = Some(Rc::new(RefCell::new(TreeNode {
                val: parent,
                left: traverse(&preorder[1..(1 + end)], &inorder[..end as usize]), 
                right: traverse(&preorder[(1 + end)..],&inorder[end + 1 as usize..]),
            }
            )));
            node
        }
        return traverse(&preorder, &inorder);
    }
}