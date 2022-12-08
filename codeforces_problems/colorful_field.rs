// Problem Link: https://codeforces.com/contest/79/problem/B
#[allow(unused_imports)]
use std::cmp::{min,max};
use std::io::{BufWriter, stdin, stdout, Write};

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

fn solve(mut wastes: Vec<(usize, usize)>, queries: Vec<(usize, usize)>, width: usize, height: usize) {
    wastes.sort();
    for query in queries {
        let mut sum = 0;
        let mut wasteland = false;
        let spaces = (query.0 - 1) * width + query.1;
        for waste in wastes.iter() {
            if *waste == query {
                wasteland = true; 
            }
            if *waste < query {
                sum += 1;
            }
        }
        sum = spaces - sum;
        if wasteland{
            println!("Waste");
        }else {
            match sum % 3 {
                1 => println!("Carrots"),
                2 => println!("Kiwis"),
                0 => println!("Grapes"),
                _ => println!("undefined"),
            }
        }
    }
}


fn main() {
    let mut scan = Scanner::default();
    let n: usize = scan.next();
    let m: usize = scan.next();
    let k: usize = scan.next();
    let t: usize = scan.next();
    let mut wastes: Vec<(usize, usize)> = (0..k).map(|_| (scan.next(), scan.next())).collect();
    let mut queries: Vec<(usize, usize)> = (0..t).map(|_| (scan.next(), scan.next())).collect();
    solve(wastes, queries, m, n);
}