//https://codeforces.com/problemset/problem/1380/C
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



fn solve(mut nums: Vec<i32>, x: i32) {
    nums.sort();
    let mut length = 0;
    let mut ans = 0;
    for (_,v) in nums.into_iter().rev().enumerate() {
        length += 1;
        if v * length >= x {
            ans += 1;
            length = 0;
        }
    }
    println!("{}", ans);
}

fn main() {
    let mut scanner = Scanner::default();
    let cases: usize = scanner.next();
    for _ in 0..cases {
        let n: usize = scanner.next();
        let x: i32 = scanner.next();
        let nums: Vec<i32>  = (0..n).map(|_| scanner.next()).collect();
        solve(nums, x);
    }
}

