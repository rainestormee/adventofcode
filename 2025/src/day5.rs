use std::fs;
use std::ops::Range;
use std::cmp::max;

fn get_input(file: &str) -> (Vec<Range<u128>>, Vec<u128>) {
    let input = fs::read_to_string(file).expect("A file");

    let mut read_range: bool = true;
    let mut output_ranges: Vec<Range<u128>> = Vec::new();
    let mut output_values: Vec<u128> = Vec::new();

    for line in input.lines() {
        if line == "" {
            read_range = false;
            continue;
        }

        if read_range {
            let first_digit: u128;
            let second_digit: u128;

            let result = line.split_once('-').expect("yes");

            first_digit = result.0.parse().unwrap();
            second_digit = result.1.parse().unwrap();

            output_ranges.push(first_digit..second_digit+1);
        } else {
            output_values.push(line.parse().unwrap());
        }
    }

    return (output_ranges, output_values);
}

fn is_in_ranges(number: u128, ranges: &Vec<Range<u128>>) -> u128 {
    for range in ranges {
        if range.contains(&number) {
            return 1;
        }
    }
    return 0;
}

pub fn part1() {
    let input = get_input("test1.yml");
    let mut answer: u128 = 0;
    
    for number in input.1 {
        answer += is_in_ranges(number, &input.0);
    } 

    println!("{:?}", answer);
}

pub fn part2() {
    let mut input = get_input("test1.yml");
    let mut output: Vec<Range<u128>> = Vec::new();
    input.0.sort_by_key(|r| r.start);
    for range in input.0 {
        if output.len() == 0 {
            output.push(range);
        } else {
            let last_range = output[output.len() - 1].clone();

            if last_range.end >= range.start {
                output.pop();
                output.push(last_range.start..max(range.last().expect("of course"), last_range.last().expect("yk"))+1);
            } else {
                output.push(range);
            }
        }
    }

    let mut result: u128 = 0;

    for range in output {
        result += range.clone().count() as u128;
    }
    println!("{result}");
}