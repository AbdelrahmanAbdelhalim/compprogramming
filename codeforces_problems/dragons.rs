//Problem Link: https://codeforces.com/problemset/problem/230/A    
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
     
    fn solve(mut strengh: usize, mut drakes: Vec<(usize, usize)>) {
        let mut drakes_defeated: usize = 0;
        drakes.sort();
        for drake in drakes.iter() {
            if strengh > drake.0 {
                strengh += drake.1;
                drakes_defeated += 1;
            }else {
                break;
            }
        }
        if drakes_defeated == drakes.len() {
            println!("YES");
        }else {
            println!("NO");
        }
    }
     
    fn main() {
        let mut scan = Scanner::default();
        let mut strength: usize = scan.next();
        let dragons: usize = scan.next();
        let mut drakes : Vec<(usize, usize)>= vec![];
        for i in 0..dragons {
            drakes.push((scan.next(), scan.next()));
        }
     
        solve(strength, drakes);
    }
