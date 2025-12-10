use std::fs;

#[derive(Debug)]
#[derive(Eq, Hash, PartialEq, Clone)]
struct Point(i64, i64);

fn get_input(file_name: &str) -> Vec<Point> {
    return fs::read_to_string(file_name).expect(file_name).lines().map(|x| {
        let split: Vec<_> = x.split(",").collect();
        return Point(split[0].parse().unwrap(), split[1].parse().unwrap());
    }).collect();
}

pub fn part1(file_name: &str) {
    let points: Vec<Point> = get_input(file_name);

    let mut biggest_a: &Point = &Point(0, 0);
    let mut biggest_b: &Point = &Point(0, 0);
    let mut area: i64 = 0;


    for a in &points {
        for b in &points {

            let ar: i64 = (b.0.max(a.0) - a.0.min(b.0) + 1) * (b.1.max(a.1) - a.1.min(b.1) + 1);

            if area < ar {
                println!("Found bigger, {a:?}, {b:?}");
                biggest_a = &a;
                biggest_b = &b;
                area = ar;
            }
        }
    }

    println!("{area}");
    println!("{biggest_a:?}, {biggest_b:?}");
}

pub fn part2(file_name: &str) {
    let points: Vec<Point> = get_input(file_name);

    let mut biggest_a: &Point = &Point(0, 0);
    let mut biggest_b: &Point = &Point(0, 0);

    let mut area: i64 = 0;


    for a in &points {
        for b in &points {

            if a == b {
                continue;
            }
            let ar: i64 = (b.0.max(a.0) - a.0.min(b.0) + 1) * (b.1.max(a.1) - a.1.min(b.1) + 1);

            if area < ar {

                let mut invalid: bool = false;

                for c in &points {
                    if a == c || b == c {
                        continue;
                    }
                    if a.0.min(b.0) < c.0 && c.0 < a.0.max(b.0) && a.1.min(b.1) < c.1 && c.1 < a.1.max(b.1) {
                        println!("Trial {a:?} => {b:?} broke by {c:?}");
                        invalid = true;
                        break;
                    }
                }

                if !invalid {
                    println!("Found bigger, {a:?}, {b:?}");
                    biggest_a = &a;
                    biggest_b = &b;
                    area = ar;
                }
            }
        }
    }


    println!("{area}");
    println!("{biggest_a:?}, {biggest_b:?}");
}