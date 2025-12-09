use std::fs;
use std::collections::HashMap;

#[derive(Debug)]
#[derive(Eq, Hash, PartialEq)]
struct Point(i64, i64, i64);

fn get_input(file_name: &str) -> Vec<Point>{
    return fs::read_to_string(file_name).expect(file_name).lines().map(|x| {
        let split: Vec<_> = x.split(",").collect();
        return Point(split[0].parse().unwrap(), split[1].parse().unwrap(), split[2].parse().unwrap());
    }).collect();
}

pub fn part1(file_name: &str) {
    let points: Vec<Point> = get_input(file_name);
    let mut hm: HashMap<&Point, HashMap<&Point, f64>> = HashMap::new();

    // Process distances between points.
    for point1 in &points {

        let mut hm2: HashMap<&Point, f64> = HashMap::new();

        for point2 in &points {

            if point1 == point2 {
                continue;
            }

            let distance: f64 = (((point2.0 - point1.0).pow(2) + (point2.1 - point1.1).pow(2) + (point2.2 - point1.2).pow(2)) as f64).sqrt();
            hm2.entry(point2).or_insert(distance);
        }
        hm.entry(point1).or_insert(hm2);
    }

    let mut circuit: Vec<Vec<&Point>> = Vec::new(); 

    for _ in 0..1000 {

        let mut small_1: &Point = &Point(0, 0, 0);
        let mut small_2: &Point = &Point(0, 0, 0);
        let mut small_distance: f64 = f64::MAX;


        for (point1, distances) in &hm {
            for (point2, distance) in distances {
                if *distance < small_distance {
                    small_1 = point1;
                    small_2 = point2;
                    small_distance = *distance;
                }
            }
        }
        
        let mut point1_array_index = usize::MAX;
        let mut point2_array_index = usize::MAX;

        for i in 0..circuit.len() {
            let connected_points = &circuit[i];

            if connected_points.contains(&small_1) {
                point1_array_index = i;
            }
            if connected_points.contains(&small_2) {
                point2_array_index = i;
            }
        }

        let needs_merging = point1_array_index != usize::MAX && point2_array_index != usize::MAX;

        if needs_merging {

            if point1_array_index != point2_array_index {
                let from = point1_array_index.max(point2_array_index);
                let to = point1_array_index.min(point2_array_index);


                let removed = circuit.remove(from);
                circuit[to].extend(removed);
            }
        } else {

            let mut inserted = false;
            
            for connected_points in &mut circuit {
                if connected_points.contains(&small_1) {
                    connected_points.push(small_2);
                    inserted = true;
                    break;
                } else if connected_points.contains(&small_2) {
                    connected_points.push(small_1);
                    inserted = true;
                    break;
                }
            }

            if !inserted {
                circuit.push(vec![small_1, small_2]);
            }
        }

        hm.get_mut(small_1).expect("yes").remove(small_2);
        hm.get_mut(small_2).expect("yes").remove(small_1);
    }

    circuit.sort_by(|b, a| a.len().cmp(&b.len()));
    let result: usize = circuit[0].len() * circuit[1].len() * circuit[2].len();
    println!("{result}");
}

pub fn part2(file_name: &str) {
    let points: Vec<Point> = get_input(file_name);
    let mut hm: HashMap<&Point, HashMap<&Point, f64>> = HashMap::new();

    // Process distances between points.
    for point1 in &points {

        let mut hm2: HashMap<&Point, f64> = HashMap::new();

        for point2 in &points {

            if point1 == point2 {
                continue;
            }

            let distance: f64 = (((point2.0 - point1.0).pow(2) + (point2.1 - point1.1).pow(2) + (point2.2 - point1.2).pow(2)) as f64).sqrt();
            hm2.entry(point2).or_insert(distance);
        }
        hm.entry(point1).or_insert(hm2);
    }

    let mut circuit: Vec<Vec<&Point>> = Vec::new(); 

    for _ in 0..1000 {

        let mut small_1: &Point = &Point(0, 0, 0);
        let mut small_2: &Point = &Point(0, 0, 0);
        let mut small_distance: f64 = f64::MAX;


        for (point1, distances) in &hm {
            for (point2, distance) in distances {
                if *distance < small_distance {
                    small_1 = point1;
                    small_2 = point2;
                    small_distance = *distance;
                }
            }
        }
        
        let mut point1_array_index = usize::MAX;
        let mut point2_array_index = usize::MAX;

        for i in 0..circuit.len() {
            let connected_points = &circuit[i];

            if connected_points.contains(&small_1) {
                point1_array_index = i;
            }
            if connected_points.contains(&small_2) {
                point2_array_index = i;
            }
        }

        let needs_merging = point1_array_index != usize::MAX && point2_array_index != usize::MAX;

        if needs_merging {

            if point1_array_index != point2_array_index {
                let from = point1_array_index.max(point2_array_index);
                let to = point1_array_index.min(point2_array_index);


                let removed = circuit.remove(from);
                circuit[to].extend(removed);
            }
        } else {

            let mut inserted = false;
            
            for connected_points in &mut circuit {
                if connected_points.contains(&small_1) && !connected_points.contains(&small_2) {
                    connected_points.push(small_2);
                    inserted = true;
                } else if connected_points.contains(&small_2) && !connected_points.contains(&small_1) {
                    connected_points.push(small_1);
                    inserted = true;
                }
            }

            if !inserted {
                circuit.push(vec![small_1, small_2]);
            }
        }

        hm.get_mut(small_1).expect("yes").remove(small_2);
        hm.get_mut(small_2).expect("yes").remove(small_1);
    }

    let mut last_x: i64 = 0;
    let mut last_x_2: i64 = 0;

    while circuit.len() != 1 {

        let mut small_1: &Point = &Point(0, 0, 0);
        let mut small_2: &Point = &Point(0, 0, 0);
        let mut small_distance: f64 = f64::MAX;


        for (point1, distances) in &hm {
            for (point2, distance) in distances {
                if *distance < small_distance {
                    small_1 = point1;
                    small_2 = point2;
                    small_distance = *distance;
                }
            }
        }
        
        let mut point1_array_index = usize::MAX;
        let mut point2_array_index = usize::MAX;

        for i in 0..circuit.len() {
            let connected_points = &circuit[i];

            if connected_points.contains(&small_1) {
                point1_array_index = i;
            }
            if connected_points.contains(&small_2) {
                point2_array_index = i;
            }
        }

        let needs_merging = point1_array_index != usize::MAX && point2_array_index != usize::MAX;

        if needs_merging {

            if point1_array_index != point2_array_index {
                let from = point1_array_index.max(point2_array_index);
                let to = point1_array_index.min(point2_array_index);


                let removed = circuit.remove(from);
                circuit[to].extend(removed);
            }
        } else {

            let mut inserted = false;
            
            for connected_points in &mut circuit {
                if connected_points.contains(&small_1) && !connected_points.contains(&small_2) {
                    connected_points.push(small_2);
                    inserted = true;
                } else if connected_points.contains(&small_2) && !connected_points.contains(&small_1) {
                    connected_points.push(small_1);
                    inserted = true;
                }
            }

            if !inserted {
                circuit.push(vec![small_1, small_2]);
            }
        }

        hm.get_mut(small_1).expect("yes").remove(small_2);
        hm.get_mut(small_2).expect("yes").remove(small_1);

        last_x = small_1.0;
        last_x_2 = small_2.0;
    }
    println!("{}", last_x * last_x_2);
}
