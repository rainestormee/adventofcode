use std::fs;

fn get_input(file: &str) -> Vec<Vec<u8>> {
    return fs::read_to_string(file).expect("A file").lines().map(|x| x.chars().map(|y| y.to_digit(10).expect("!!") as u8).collect()).collect();
}

pub fn part1() {

    let mut sum: i32 = 0;

    for input in get_input("test1.yml") {

        let mut biggest = 0;
        let mut second_biggest = 0;

        let last = input.len() - 1;

        // deliberately leaving off the last digit.
        for n in 0..input.len() {

            if input[n] > second_biggest {
                second_biggest = input[n];
            }
            if n < last && input[n] > biggest {
                biggest = input[n];
                second_biggest = 0;
            }
        }

        sum = sum + i32::from(biggest*10) + i32::from(second_biggest);

        println!("{biggest}{second_biggest} : {:?}", input);
    }
    println!("{sum}")
}

pub fn part2() {

    const LENGTH: usize = 12;
    let mut sum: i64 = 0;

    for input in get_input("main1.yml") {

        let mut biggest_vec: [u8; LENGTH] = [0; LENGTH];
        let last = input.len() - 1;

        for n in 0..input.len() {

            for i in 0..biggest_vec.len() {
                let index = biggest_vec.len() - i - 1;
                let remaining_digits = input.len() - n - 1;

                if remaining_digits >= index && input[n] > biggest_vec[index] {
                    biggest_vec[index] = input[n];
                    for wipe in 0..index {
                        biggest_vec[wipe] = 0;
                    }
                    break;
                }
            }
        }
        let mut small_sum: u64 = 0;
        for digit in biggest_vec.iter().rev() {
            small_sum = small_sum * 10 + u64::from(*digit);
        }

        sum += small_sum as i64;
    }
    println!("{sum}")
}
