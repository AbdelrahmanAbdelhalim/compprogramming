// You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

impl Solution {
    //Solution Performance: Runtime 1 ms Beats 66.39% Memory 2.2 MB Beats 43.44%
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let mut l = 0;
        let mut r = matrix[0].len() - 1;
        // Reflect image on the vertical middle axis
        while r > l {
            for i in 0..matrix.len() {
                let temp = matrix[i][l];
                matrix[i][l] = matrix[i][r];
                matrix[i][r] = temp;
            }
            r -= 1;
            l += 1;
        }
        let mut i = 0;
        let mut j = 0;
        //reflect on x = y;
        while j < matrix.len() {
            if i + j == matrix.len() - 1{
                i = 0;
                j += 1;
                continue
            }
            let temp = matrix[i][j];
            let limit = matrix.len() - 1;
            matrix[i][j] = matrix[limit - j][limit - i];
            matrix[limit - j][limit - i] = temp;
            i += 1;
        }
    }
}
