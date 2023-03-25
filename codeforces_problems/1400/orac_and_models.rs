//Problem Link: https://codeforces.com/contest/1350/problem/B 
#[allow(unused_imports)]
use std::cmp::{max, min};
use std::{
    ascii,
    io::{stdin, stdout, BufWriter, Write},
};

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



fn solve(nums: Vec<i32>) {
    let mut dp = vec![1; nums.len()];
    let k = dp.len();
    for i in 1..k {
        let mut j = 2*i;
        while j < dp.len() {
            if nums[j] > nums[i] {
                dp[j] = max(dp[j], dp[i] + 1);
            }
            j += i;
        }
    }
    let ans = dp.into_iter().max().unwrap();
    println!("{}", ans);
}

fn main() {
    let mut scanner = Scanner::default();
    let c: usize = scanner.next();
    for _ in 0..c {
        let l: usize = scanner.next();
        let mut nums = Vec::with_capacity(l + 1);
        nums.push(0);
        for _ in 0..l {
            nums.push(scanner.next());
        }
        solve(nums);
    }
}

