//Problem Link: https://codeforces.com/problemset/problem/1363/B
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


fn solve(num: String) {
    let mut zeros: i64 = 0;
    for i in num.chars() {
        if i == '0' {
            zeros += 1;
        } 
    }
    let mut ones = 0;
        for i in num.chars() {
            if i == '1' {
                ones += 1;
            } 
        }
    let mut ans = min(zeros, ones);
    let mut zerossf = 0; let mut onessf = 0;
    for (_,v) in num.chars().into_iter().enumerate(){
        if v == '0' {
            zerossf += 1;
        }
        if v == '1' {
            onessf += 1;
        }
        ans = min(ans, onessf + zeros - zerossf);
        ans = min(ans, zerossf + ones - onessf);
    }
    println!("{}", ans);
}

fn main() {
    let mut scanner = Scanner::default();
    let c: usize = scanner.next();
    for _ in 0..c {
        let case: String = scanner.next();
        solve(case);
    }
    
}

