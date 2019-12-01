use std::io;
use std::io::prelude::*;

fn find_fuel(mass: i32) -> i32 {
    let add_fuel = std::cmp::max(0, mass / 3 - 2);
    println!("{}", add_fuel);
    add_fuel + if add_fuel > 2 { find_fuel(add_fuel) } else { 0 }
}

fn main() {
    let stdin = std::io::stdin();
    let res = stdin
        .lock()
        .lines()
        .fold(0, |y, x| y + find_fuel(x.unwrap().parse::<i32>().unwrap()));
    println!("{:?}", res)
}
