// Problem Link: https://codeforces.com/problemset/problem/401/C
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

fn solve(mut zeros: usize, mut ones: usize) {
    if zeros > ones {
        if zeros - 1 > ones {
            println!("{}", -1);
            return;
        }
    } else {
        if (ones - 1) / 2 > zeros {
            println!("{}", -1);
            return;
        }
    }
    let mut ans = String::new();
    if zeros >= ones {
        if zeros > ones {
            ans.push('0');
        }
        for _ in 0..ones {
            ans.push('1');
            ans.push('0')
        }
        println!("{}", ans);
        return;
    } while ones > zeros && zeros > 0 && ones >= 2{
        ans.push('1');
        ans.push('1');
        ans.push('0');
        ones -= 2;
        zeros -= 1;
    }
    if zeros == ones {
        for _ in 0..zeros {
            ans.push('1');
            ans.push('0');
        }
    }else {
        for _ in 0..ones {
            ans.push('1');
        }
    }
    println!("{}", ans);

}

fn main() {
    let mut scanner = Scanner::default();
    let n: usize = scanner.next();
    let m: usize = scanner.next();
    solve(n, m);
}

