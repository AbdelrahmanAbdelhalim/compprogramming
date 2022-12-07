///Problem Statement: Given an integer n, return the least number of perfect square numbers that sum to n.

// A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
impl Solution {
    pub fn num_squares(n: i32) -> i32 {
        ///Performance: Runtime 1683 msBeats 5.8% Memory 2.1 MB Beats 73.53%
        ///This is not the best solution and there are some clear optimizations

        if n == 0 {
            return 0;
        }
        if n == 1{
            return 1;
        }
        use std::i32;
        let foo = n;
        let mut dp = vec![i32::MAX; (n + 1) as usize];
        dp[0] = 0;

        for i in 0..dp.len() - 1{
            for j in 1..foo { ///instead of having this loop we can precompute it and store it into a list
                              /// also instead of iterating up to foo we can iterate up to n we can iterate up to sqrt(n)
                let pow  = (j*j) as usize;
                if i + pow <= n as usize {
                    if dp[i + pow] > dp[i] + 1 {
                        dp[i + pow] = dp[i] + 1;
                    }
                }
            }
        }
        return dp[n as usize];   
    }
}