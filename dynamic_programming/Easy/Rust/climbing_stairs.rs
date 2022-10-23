///Problem Statement
///You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let n = n as usize;
        let mut dp = vec![0; n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for i in 2..dp.len(){
            dp[i] += dp[i - 1];
            dp[i] += dp[i - 2];
        }
        return dp[dp.len() - 1];
    }
}
