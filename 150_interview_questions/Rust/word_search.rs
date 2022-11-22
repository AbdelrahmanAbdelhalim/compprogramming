///Problem Statement
///Given an m x n grid of characters board and a string word, return true if word exists in the grid.

///The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



impl Solution {
    ///Solution Performance: Runtime 1242 ms Beats 11.27%, Memory 2.3 MB Beats 14.79%
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        use std::collections::HashSet;
         fn dfs(board: &Vec<Vec<char>>, node: (usize, usize), tracker: usize, word: &[u8], visited: &mut HashSet<(usize, usize)>) -> bool {
        if tracker == word.len(){
            return true;
        }
        let x_offset = vec![0,1,0,-1];
        let y_offset = vec![1,0,-1,0];
        let (x,y) = node;
        let mut possible_children = vec![];
        for i in 0..x_offset.len() {
            let new_x = x as i32 + x_offset[i];
            let new_y = y as i32 + y_offset[i];
            if  new_x < board.len() as i32 && 
                new_x >= 0 && 
                new_y < board[0].len() as i32 &&
                new_y >= 0 &&
                board[new_x as usize][new_y as usize] as u8 == word[tracker] &&
                !visited.contains(&(new_x as usize, new_y as usize)) {
                possible_children.push((new_x as usize, new_y as usize));
            } 
        }
        let mut ans = false;
        for i in 0..possible_children.len() {
            visited.insert((possible_children[i]));
            ans = ans | dfs(board, possible_children[i], tracker + 1, word, visited);
            visited.remove(&possible_children[i]);
        }
        return ans;
}
        let mut visited = HashSet::new();
        let ans = false;
        let tracker = 0;
        let word = word.as_bytes();
        for i in 0..board.len() {
            for j in 0..board[0].len() {
                if board[i][j] as u8 == word[tracker] {
                    println!("{}, {}", i, j);
                    visited.insert((i,j));
                    let ans = dfs(&board, (i,j), tracker + 1, word, &mut visited);
                    visited.remove(&(i,j));
                    if ans == true {
                        return ans
                    }
                }
            }
        }
        ans
        }
}
