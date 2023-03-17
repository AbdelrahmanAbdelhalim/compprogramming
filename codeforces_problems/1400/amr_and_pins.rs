//Problem Link: https://codeforces.com/contest/507/problem/B
//Good solution on your own
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


fn solve(r: f64, x1: i64, y1: i64, x2: i64, y2: i64) {
    let distance2 = ((x2 - x1).pow(2) + (y2 - y1).pow(2)) as f64; 
    let distance = distance2.sqrt();
    let ans = (distance / r).ceil();
    println!("{}", ans);
}

fn main() {
    let mut scanner = Scanner::default();
    let r: f64 = scanner.next();
    let x1: i64 = scanner.next();
    let y1: i64 = scanner.next();
    let x2: i64 = scanner.next();
    let y2: i64 = scanner.next();
    solve(2 as f64 *r, x1, y1, x2, y2);
}

