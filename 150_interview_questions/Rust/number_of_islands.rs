///Problem Statement
/// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
///An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

fn sol(grid: Vec<Vec<char>>) -> i32 {
    ///Solution Performance:
    /// Runtime 63 ms Beats 5.74% Memory 9 MB Beats 81.15%
    /// There is much simpler implementations and other with better runtime that are definitely worth checking out
    /// This follows the algo monster approach more or less
    use std::collections::HashSet;
    let mut answer = 0;
    fn get_neighbors(x: i32, y: i32, grid: &Vec<Vec<char>>) -> Vec<(i32, i32)> {
        let mut neighbors = vec![];
        let x_offset = vec![0, 1, 0, -1];
        let y_offset = vec![1, 0, -1, 0];
        for i in 0..x_offset.len() {
            let new_x = x + x_offset[i];
            let new_y = y + y_offset[i];

            if  new_x >= 0
                && new_x < grid.len() as i32
                && new_y >= 0
                && new_y < grid[0].len() as i32
                && grid[new_x as usize][new_y as usize] == '1'
            {
                neighbors.push((new_x, new_y))
            }
        }
        neighbors
    }
    let mut visited: HashSet<(usize, usize)> = HashSet::new();
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if !visited.contains(&(i, j)) && grid[i][j] != '0' {
                let mut children = vec![];
                children.push((i as i32,j as i32));
                while children.len() > 0 {
                    let child = children.pop().unwrap();
                    let (childx, childy) = child;
                    visited.insert((childx as usize, childy as usize));
                    let new_children = get_neighbors(childx, childy, &grid);
                    for i in 0..new_children.len() {
                        let (new_child_x, new_child_y) = new_children[i];
                        if !visited.contains(&(new_child_x as usize, new_child_y as usize)) {
                            children.push((new_child_x as i32, new_child_y as i32));
                        }
                    }
                }
                answer += 1;
            }
        }
    }
    answer
}
