use std::fs;

pub fn part1(file: &str) -> i32 {
    let contents = fs::read_to_string(file).expect("");

    let instructions: Vec<(String, i32)> = contents.lines().map(|x| {
        let (dir, dist) = x.split_at(1);
        (dir.to_string(), dist.parse().unwrap())
    }).collect();

    let mut dial: i32 = 50;
    let mut res: i32 = 0;

    for instruction in instructions {
        if &instruction.0 == "L" {
            dial -= &instruction.1;
        } else {
            dial += &instruction.1;
        }

        dial = dial.rem_euclid(100);

        if dial == 0 {
            res += 1;
        }
    }
    
    return res;
}

pub fn part2(file: &str) -> i32 {
    let contents = fs::read_to_string(file).expect("");

    let instructions: Vec<(String, i32)> = contents.lines().map(|x| {
        let (dir, dist) = x.split_at(1);
        (dir.to_string(), dist.parse().unwrap())
    }).collect();

    let mut dial: i32 = 50;
    let mut res: i32 = 0;

    for instruction in instructions {
        let mut remaining_click = *&instruction.1;
        let mut small_res = 0;

        if instruction.0 == "L" {
            while 0 < remaining_click {
                dial -= 1;
                remaining_click -= 1;

                if dial == 0 {
                    small_res += 1;
                }
                if dial == -1 {
                    dial = 99;
                }
            } 

        } else {
            while 0 < remaining_click {
                dial += 1;
                remaining_click -= 1;

                if dial == 100 {
                    dial = 0;
                }

                if dial == 0 {
                    small_res += 1;
                }
            }
        }

        res += small_res;
        // println!("{:?} | {} => {} : {} ", instruction, old_dial, dial, small_res)
    }

    return res;
}