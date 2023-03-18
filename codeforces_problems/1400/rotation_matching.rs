//Problem Link: https://codeforces.com/problemset/problem/1365/C
//All me!
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


fn solve(arr1: Vec<i32>, arr2: Vec<i32>) {
    use std::collections::HashMap;
    let mut reserve: HashMap<i32,usize> = HashMap::new();
    for (i,v) in arr1.iter().enumerate() {
        reserve.insert(*v, i);
    }

    let mut cou: Vec<i32> = vec![0; 2*arr1.len() + 1];
    for (i,v) in arr2.iter().enumerate() {
        let loc = *reserve.get(v).unwrap();
        let diff: i32 = loc as i32 - i as i32;

        if diff >= 0 {
            cou[diff as usize] += 1;
            cou[arr1.len() - diff as usize + arr1.len()];
        }else {
            cou[diff.abs() as usize + arr1.len()] += 1;
            cou[arr1.len() - diff.abs() as usize] += 1;
        }
    }
    let ans = cou.into_iter().max().unwrap();
    println!("{}", ans);
}

fn main() {
    let mut scanner = Scanner::default();
    let l: usize = scanner.next();
    let arr1: Vec<i32> = (0..l).map(|_| scanner.next()).collect();
    let arr2: Vec<i32> = (0..l).map(|_| scanner.next()).collect();
    solve(arr1, arr2);
}

