//Problem Link: https://codeforces.com/problemset/problem/1348/B
#[allow(unused_imports)]
use std::cmp::{max, min};
use std::collections::HashSet;
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


fn solve(nums: HashSet<i32>, k: usize, n: usize) {
    if nums.len() > k {
        println!("-1");
        return;
    }
    println!("{}", n*k);

    for _ in 0..n {
        for i in nums.iter() {
            print!("{} ", i);
        }
        for i in 0..k-nums.len() {
            print!("{} ", 1);
        }
    }
    println!("");
}

fn main() {
    
    let mut scanner = Scanner::default();
    let c: usize = scanner.next();
    for _ in 0..c {
        let length: usize = scanner.next();
        let k: usize = scanner.next();
        let nums: HashSet<i32> = (0..length).map(|_| scanner.next()).collect();
        solve(nums,k, length);
    }
}

