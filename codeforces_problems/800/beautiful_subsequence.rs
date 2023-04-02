//Problem Link: https://codeforces.com/contest/1810/problem/A
#[allow(unused_imports)]
use std::cmp::{min,max};
use std::io::{BufWriter, stdin, stdout, Write};
use std::time::Instant;
 
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
fn check(mid: i64, players: &Vec<i64>) -> bool {
    let mut total = players[mid as usize];
    for (i, v) in players.iter().enumerate() {
        if i == mid as usize { 
            continue;
        } 
        if total < *v {
            return false;
        }
        total += *v;
    }
    return true;
}
fn search(nums: &Vec<i64>) -> i64 {
    let mut l = 0 as i64;
    let mut r = (nums.len() - 1) as i64;
    let mut ans = 0;
    while l <= r {
        let mid = (r + l) / 2;
        if check(mid, nums) {
            ans = mid;
            r = mid - 1;
        }else {
            l = mid + 1;
        }
    }
    return ans;
}
 
fn solve(nums: Vec<i64>) {
    for (i,v) in nums.into_iter().enumerate() {
        if v <= (i + 1) as i64 {
            println!("YES");
            return;
        }
    }
    println!("NO");
}
 
fn main() {
    let mut scanner = Scanner::default();
    let c: usize = scanner.next();
    for _ in 0..c {
        let l: usize = scanner.next();
        let nums: Vec<i64> = (0..l).map(|_| scanner.next()).collect();
        solve(nums);
    }
}

