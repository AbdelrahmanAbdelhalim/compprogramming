//https://codeforces.com/problemset/problem/1369/C
#[allow(unused_imports)]
use std::cmp::{max, min};
use std::io::stdin;

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

fn solve(mut nums: Vec<i64>, mut friends: Vec<i64>) {
    nums.sort();
    friends.sort();
    let mut foo = nums.into_iter();
    let mut ans = 0;
    for f in friends.iter() {
        if *f == 1 {
            ans += foo.next_back().unwrap() * 2;
        }
    }
    for f in friends.into_iter().rev() {
        if f != 1 {
            let r = foo.next_back().unwrap();
            let l = foo.next().unwrap();
            ans += l + r;
            for _ in 0..(f - 2) {
                foo.next();
            }
        }
    }
    println!("{}", ans);
}

fn main() {
    let mut scanner = Scanner::default();
    let c: usize = scanner.next();
    for _ in 0..c {
        let i: usize = scanner.next();
        let f: usize = scanner.next();
        let integs: Vec<i64> = (0..i).map(|_| scanner.next()).collect();
        let friends: Vec<i64> = (0..f).map(|_| scanner.next()).collect();
        solve(integs, friends);
    }
}

