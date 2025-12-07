use std::fs;

fn read_input(file: &str) -> Vec<Vec<char>> {
    return fs::read_to_string(file).expect(file).lines().map(|x| x.chars().collect()).collect();
}

pub fn part1(file: &str) {
    let mut inp = read_input(file);
    // let mut previous: Vec<bool>  = Vec::new();
    // let mut this: Vec<bool> = Vec::new();
    let mut split: usize = 0;

    for i in 0..inp.len() - 1 {
        for j in 0..inp[i].len() {
            if inp[i][j] == 'S' {
                inp[i+1][j] = '|';
            }
            if inp[i][j] == '|' {

                if inp[i + 1][j] == '.' {
                    inp[i + 1][j] = '|';
                } else if inp[i + 1][j] == '^' {
                    split += 1;
                    inp[i + 1][j - 1] = '|';

                    if j <= inp.len() - 1{
                        inp[i + 1][j + 1] = '|';
                    }
                }
            }
        }
    }

    for line in inp {
        println!("{:?}", line);
    }
    println!("{}", split);
}

pub fn part2(file: &str) {
    let mut inp = read_input(file);

    for i in 0..inp.len() - 1 {
        for j in 0..inp[i].len() {
            if inp[i][j] == 'S' {
                inp[i+1][j] = '|';
            }
            if inp[i][j] == '|' {

                if inp[i + 1][j] == '.' {
                    inp[i + 1][j] = '|';
                } else if inp[i + 1][j] == '^' {
                    inp[i + 1][j - 1] = '|';

                    if j <= inp.len() - 1{
                        inp[i + 1][j + 1] = '|';
                    }
                }
            }
        }
    }

    let mut count: usize = 0;
    let mut out: Vec<Vec<usize>> = Vec::new();

    for i in 0..inp.len() {
        let mut out_line: Vec<usize> = Vec::new();

        for j in 0..inp[i].len() {
            if i == 0 {
                if inp[i][j] == '.' {
                    out_line.push(0);
                } else {
                    out_line.push(1);
                }
            } else {
                if inp[i][j] == '|' {
                    out_line.push(out[i - 1][j]);

                    if j != 0 && inp[i][j - 1] == '^' {
                        out_line[j] += out[i - 1][j - 1];
                    }
                    if j < inp[i].len() - 1 && inp[i][j + 1] == '^' {
                        out_line[j] += out[i - 1][j + 1];
                    }

                } else {
                    out_line.push(0);
                }
            }
        }
        out.push(out_line.clone());
    }

    for i in out[out.len() - 1].clone() {
        count += i;
    }

    println!("{count}");
}
// 3116 == too low