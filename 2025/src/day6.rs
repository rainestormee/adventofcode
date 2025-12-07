use std::fs;
use std::str::Chars;

fn get_input(file_name: &str) -> (Vec<Vec<String>>, Vec<bool>) {

    // True == Multiplication, because i said so
    let mut operations: Vec<bool> = Vec::new();
    let mut lengths: Vec<usize> = Vec::new();

    let file = fs::read_to_string(file_name).expect(":)");

    let mut since_last: usize = 0; 
    let mut lines: Vec<Chars> = file.lines().map(|x| x.chars()).collect();
    let mut numbers: Vec<Vec<String>> = Vec::new();

    for character in lines[lines.len() - 1].clone() {
        if character == '*' {
            operations.push(true);
            lengths.push(since_last);
            since_last = 0;
        } else if character == '+' {
            operations.push(false);
            lengths.push(since_last);
            since_last = 0;
        } else {
            since_last += 1;
        }
    }
    lengths.push(since_last + 1);
    lengths.drain(0..1);

    for _ in 0..lines.len()-1 {
        numbers.push(Vec::new());
    } 

    for len in lengths {
        for i in 0..lines.len()-1 {
            numbers[i].push(lines[i].by_ref().take(len + 1).collect());
        }
    }

    return (numbers, operations);
}

pub fn part1(file_name: &str) {
    let input = get_input(file_name);
    let numbers = input.0;

    let mut result: usize = 0;

    let operations = input.1;

    for i in 0..operations.len() {

        let mut small_number: usize = 0;

        if small_number == 0 && operations[i] {
            small_number = 1;
        }
    

        for j in 0..numbers.len() {
            if operations[i] {
                small_number *= numbers[j][i].trim().parse::<usize>().unwrap();
            } else {
                small_number += numbers[j][i].trim().parse::<usize>().unwrap();
            }
        }

        result += small_number;
    }
}

pub fn part2(file_name: &str)  {
    let input = get_input(file_name);
    let numbers = input.0;

    let mut result: usize = 0;

    let operations = input.1;

    for i in 0..operations.len() {

        let mut small_number: usize = 0;

        if small_number == 0 && operations[i] {
            small_number = 1;
        }

        let mut these_numbers: Vec<String> = Vec::new();

        for j in 0..numbers.len() {
            these_numbers.push(numbers[j][i].clone());
        }

        for x in 0..these_numbers[0].len() {

            let mut created: Vec<char> = Vec::new();

            for y in 0..these_numbers.len() {
                created.push(these_numbers[y].chars().collect::<Vec<_>>()[x]);
            }
            if created.iter().all(|z| *z == ' ') {
                continue;
            }  
            

            let number: usize = created.iter().collect::<String>().trim().parse::<usize>().unwrap();

            if operations[i] {
                small_number *= number;
            } else {
                small_number += number;
            }
        }

        result += small_number;
    }

    println!("{result}");
}