use std::iter::{Zip, zip};

fn knapsack(mut max_weight: i32, profits: Vec<i32>, weights: Vec<i32>) -> i32 {
    let mut total_profit: i32 = 0;
    let data: Vec<(i32, i32)>;

    let mut data = weights
        .iter()
        .enumerate()
        .map(|(i,&w)| (i, profits[i] as f64/ w as f64))
        //.map(|(i,&w)| (i, profits[i] / w ))
        .collect::<Vec<(usize, f64)>>();
        
    data.sort_by(|a,b| b.1.partial_cmp(&a.1).unwrap());

    for (i, _) in data {

        if weights[i] > max_weight {
            todo!();
        }

        total_profit += profits[i];
        max_weight -= weights[i];
    }

    total_profit
}

fn main() {
    println!("Hello, world!");
    let profits = vec![10,5,15,7,6,18,3];
    let weights = vec![2,3,5,7,1,4,1];

    dbg!(knapsack(15, profits, weights));
}
