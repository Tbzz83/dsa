mod find_min_rotated;
mod search_rotated;

struct Solution;

fn main() {
    println!("---Find Min---");
    println!("{}", Solution::find_min(vec![4,5,6,7,0,1,2]));
    println!("{}", Solution::search(vec![4,5,6,7,0,1,2], 0));
}
