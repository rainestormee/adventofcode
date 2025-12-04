use std::fs;

fn get_input(file: &str) -> Vec<Vec<u8>> {
    return fs::read_to_string(file).expect("A file").lines().map(|x| x.chars().map(|y| { if y == '.' { return 0; } else { return 1; }}).collect()).collect();
}

pub fn part1() {
    let inp = get_input("live1.yml");

    let mut output: u32 = 0; 

    for x in 0..inp.len() {
        for y in 0..inp[0].len() {

            if inp[x][y] == 0 {
                continue;
            }

            let mut n: u8 = 0;

            // can check to the left
            if x != 0 {
                // check to the left
                n += inp[x - 1][y];
                
                if y != 0 {
                    n += inp[x - 1][y - 1];
                }

                if y != inp[0].len() - 1{
                    n += inp[x - 1][y + 1];
                }
            }

            if x != inp.len() - 1 {
                n += inp[x + 1][y];

                if y != 0 {
                    n += inp[x + 1][y - 1];
                }

                if y != inp[x].len() - 1{
                    n += inp[x + 1][y + 1];
                }
            }

            if y != 0 {
                n += inp[x][y - 1];
            }

            if y != (inp[x].len() - 1) {
                n += inp[x][y + 1]
            }

            if n < 4 {
                output += 1;
            }
        }


    }

    println!("{:?}", output);
    
}

pub fn part2() {
    let mut inp = get_input("live1.yml");
    let mut next_iter = inp.clone();

    let mut output: u32 = 0; 

    loop {
        let mut score: u32 = 0;

        for x in 0..inp.len() {
            for y in 0..inp[0].len() {

                if inp[x][y] == 0 {
                    continue;
                }

                let mut n: u8 = 0;

                // can check to the left
                if x != 0 {
                    // check to the left
                    n += inp[x - 1][y];
                    
                    if y != 0 {
                        n += inp[x - 1][y - 1];
                    }

                    if y != inp[0].len() - 1{
                        n += inp[x - 1][y + 1];
                    }
                }

                if x != inp.len() - 1 {
                    n += inp[x + 1][y];

                    if y != 0 {
                        n += inp[x + 1][y - 1];
                    }

                    if y != inp[x].len() - 1{
                        n += inp[x + 1][y + 1];
                    }
                }

                if y != 0 {
                    n += inp[x][y - 1];
                }

                if y != (inp[x].len() - 1) {
                    n += inp[x][y + 1]
                }

                if n < 4 {
                    score += 1;
                    next_iter[x][y] = 0;
                }
            }


        }

        if score == 0 {
            break;
        }

        output += score;
        inp = next_iter.clone();
    }

    println!("{:?}", output);
    
}