use std::io;
use std::io::prelude::*;

fn main() {
    let stdin = std::io::stdin();
    let mut input = String::new();
    stdin.read_line(&mut input).unwrap();

    let vec_org: Vec<String> = input.trim().split(',').map(|x| x.to_owned()).collect();
    for x in 0..vec_org.len() {
        for y in 0..vec_org.len() {
            let mut vec = vec_org.clone();
            vec[1] = x.to_string();
            vec[2] = y.to_string();
            for i in 0..(vec.len() / 4) {
                let i = i * 4;
                let (op, in1, in2, out) = (
                    vec[i].parse::<i32>().unwrap(),
                    vec[i + 1].parse::<usize>().unwrap(),
                    vec[i + 2].parse::<usize>().unwrap(),
                    vec[i + 3].parse::<usize>().unwrap(),
                );
                match op {
                    1 => {
                        let res = (vec[in1].parse::<i32>().unwrap()
                            + vec[in2].parse::<i32>().unwrap())
                        .to_string();
                        vec[out] = res;
                        // println!(
                        //     "{}, {}, {}, {} ended up with {}",
                        //     op, in1, in2, out, &vec[out]
                        // );
                        // println!("{:?}", vec);
                    }
                    2 => {
                        let res = (vec[in1].parse::<i32>().unwrap()
                            * vec[in2].parse::<i32>().unwrap())
                        .to_string();
                        vec[out] = res;
                        // println!(
                        //     "{}, {}, {}, {} ended up with {}",
                        //     op, in1, in2, out, &vec[out]
                        // );
                        // println!("{:?}", vec);
                    }
                    99 => break,
                    _ => panic!("{}, {}, {}", i, vec_org[i], vec[i]),
                }
            }
            if vec[0].parse::<i32>().unwrap() == 19690720 {
                println!("{}, {}", x, y);
                break;
            } else {
                // println!("{}, {} failed", x, y);
            }
        }
    }
}
