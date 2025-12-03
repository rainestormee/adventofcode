use std::fs;

fn get_input(input: &str) -> Vec<(u64, u64)> {
    return fs::read_to_string(input).expect("File").lines().collect::<Vec<_>>().first().unwrap().split(",").map(|x| { 
        let split: Vec<_> = x.split("-").collect();
        return (split[0].parse().unwrap(), split[1].parse().unwrap());
    }).collect();
}

pub fn part1() {

    let inputs = get_input("live1.yml");

    let result: u128 = inputs.iter().map(|input| {

        let numbers: u128 = (input.0..input.1 + 1).filter(|n| n.to_string().len() % 2 == 0).filter(|x| {
            // for 1 -> string.length / 2 => try to do match of substrings.
        
            let y = x.to_string();
            let big_len = y.len();

            for len in 1..(big_len/2)+1 {
                
                if big_len % len != 0 {
                    continue;
                }
                if len != (big_len / 2) {
                    continue;
                }
                    
                // get substring.
                let x = y.chars().take(len).collect::<String>();
                let mut fnstr = x.clone();

                while fnstr.len() < y.len() {
                    fnstr = fnstr + &x;
                }

                if fnstr == y {
                    return true;
                }
            }
            return false;
        }).map(|x| u128::from(x)).sum();
        println!("{numbers}");
        return numbers;
    }).sum();

    // 3349553331
    // 1227775554
    println!("Final {result}")
}

pub fn part2() {

    let inputs = get_input("live1.yml");

    let result: u128 = inputs.iter().map(|input| {

        let numbers: u128 = (input.0..input.1 + 1).filter(|x| {
            // for 1 -> string.length / 2 => try to do match of substrings.
            let y = x.to_string();
            let big_len = y.len();

            for len in 1..(big_len/2)+1 {
                
                if big_len % len != 0 {
                    continue;
                }
                    
                // get substring.
                let x = y.chars().take(len).collect::<String>();
                let mut fnstr = x.clone();

                while fnstr.len() < y.len() {
                    fnstr = fnstr + &x;
                }

                if fnstr == y {
                    return true;
                }
            }
            return false;
        }).map(|x| u128::from(x)).sum();
        return numbers;
    }).sum();

    println!("Final {result}")
}
