///Problem Link: https://codeforces.com/problemset/problem/489/C
/// Lessons learned: Pushing chars to string in rust
#[allow(unused_imports)]
use std::cmp::{min,max};
use std::{io::{BufWriter, stdin, stdout, Write}, ascii};

#[derive(Default)]
struct Scanner {
    buffer: Vec<String>
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
fn can(n:i32 , s: i32) -> bool {
    s >= 0 && s <= 9 * n 
}
fn measuer(n: i32, s: i32) -> bool {
    (s >= 1 && s <= 9 * n) || (n == 1 && s == 0)
}

fn solve(m: i32, s: i32) {
    let mut sum = s;
    let mut minn = String::new();
    if !measuer(m, s) {
        println!("{} {}", -1, -1);
        return
    }
    for i in 0..m {
        'inner: for d in 0..=9 {
            if can(m - i - 1, sum - d) && (i > 0 || d > 0 || (m == 1 && d == 0)) {
                let newchar = '0' as u8 + d as u8;
                minn.push(newchar as char);
                sum -= d;
                break 'inner;
            }
        }
    }
    let mut mxx = String::new();
    sum = s;
    for i in 0..m {
        'inner: for d in (0..=9).rev() {
            if can(m - i - 1, sum - d) && (i > 0 || d > 0 || (m == 1 && d == 0)) {
                let newchar = '0' as u8 + d as u8;
                mxx.push(newchar as char);
                sum -= d;
                break 'inner;
            }
        }
    }
    println!("{} {}", minn, mxx);
}
fn main() {
    let mut scan = Scanner::default();
    let n: i32 = scan.next();
    let s: i32 = scan.next();
    solve(n,s);
}

