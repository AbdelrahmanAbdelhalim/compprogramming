//Problem: https://codeforces.com/contest/1195/problem/C
#[allow(unused_imports)]
use std::cmp::{max, min};
use std::io::{stdin, stdout, BufWriter, Write};
#[derive(Default)]
struct Scanner {
    buffer: Vec<String>,
}
impl Scanner {
    fn next<T: std::str::FromStr>(&mut self) -> T {
        loop {
            if let Some(token) = self.buffer.pop() {
                return token.parse().ok().expect("Failed parse");
            }
            let mut input = String::new();
            stdin().read_line(&mut input).expect("Failed read");
            self.buffer = input.split_whitespace().rev().map(String::from).collect();
        }
    }
}
fn solve(row1: Vec<i64>, row2: Vec<i64>) {
    let mut dp :Vec<Vec<i64>>= vec![vec![0; 3]; row1.len() + 1];
    dp[0][0] = 0;
    dp[0][1] = 0;
    dp[0][2] = 0;
    for i in 0..row1.len() {
        let i = i + 1;
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]);
        dp[i][1] = max(dp[i - 1][2] + row1[i - 1],max( dp[i - 1][0] + row1[i - 1], row1[i - 1]));
        dp[i][2] = max(dp[i - 1][1] + row2[i - 1],max(dp[i - 1][0] + row2[i - 1], row2[i - 1]));
    }
    let ans = dp[dp.len() - 1].iter().max().unwrap();
    println!("{}", ans);
}
fn main() {
    let mut scan = Scanner::default();
    let n: usize = scan.next();
    let mut row1: Vec<i64> = vec![];
    let mut row2: Vec<i64> = vec![];
    for _ in 0..n {
        row1.push(scan.next());
    }
    for _ in 0..n {
        row2.push(scan.next());
    }
    solve(row1, row2);
}
