fn knapsack(mut max_weight: i32, profits: Vec<i32>, weights: Vec<i32>) -> f64 {
    let mut total_profit: f64 = 0.0;
    let mut idx_profit_by_weight: Vec<(usize, f64)>;
    idx_profit_by_weight = weights
        .iter()
        .enumerate()
        .map(|(i,&w)| (i, profits[i] as f64/ w as f64))
        .collect();
        
    idx_profit_by_weight.sort_by(|a,b| b.1.partial_cmp(&a.1).unwrap());

    for (i, _) in idx_profit_by_weight {
        if weights[i] > max_weight {
            total_profit += profits[i] as f64 * (max_weight as f64 / weights[i] as f64);
            break;
        }

        total_profit += profits[i] as f64;
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
