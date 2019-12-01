use std::io;
use std::io::prelude::*;

fn main() {
    let stdin = std::io::stdin();
    let res = stdin
        .lock()
        .lines()
        .fold(0, |y, x| x.unwrap().parse::<i32>().unwrap() / 3 - 2 + y);
    println!("{:?}", res)
}
