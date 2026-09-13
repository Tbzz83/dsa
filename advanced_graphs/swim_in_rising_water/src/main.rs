
/*
You are given a square 2-D matrix of distinct integers grid where each integer grid[i][j] represents the elevation at position (i, j).

Rain starts to fall at time = 0, which causes the water level to rise. At time t, the water level across the entire grid is t.

You may swim either horizontally or vertically in the grid between two adjacent squares if the original elevation of both squares is less than or equal to the water level at time t.

Starting from the top left square (0, 0), return the minimum amount of time it will take until it is possible to reach the bottom right square (n - 1, n - 1).

*/

struct Solution {}

use std::{cmp::{self, Reverse, max}, collections::{BinaryHeap, HashSet}};

impl Solution {

    fn get_valid_next_coords(c: (usize,usize), seen: &HashSet<(usize,usize)>, grid: &Vec<Vec<i32>>) -> Vec<(usize,usize)> {
        let mut valid_coords: Vec<(usize,usize)> = vec![];

        let up = (c.0 as i32 -1, c.1 as i32);
        let down = (c.0 as i32 +1, c.1 as i32);
        let left = (c.0 as i32, c.1 as i32 -1);
        let right = (c.0 as i32, c.1 as i32+1);

        if up.0 >= 0 && up.0 < grid.len() as i32 && up.1 >= 0 && up.1 < grid[0].len() as i32 && !seen.contains(&(up.0 as usize, up.1 as usize)) {
            valid_coords.push((up.0 as usize, up.1 as usize));
        }
        if down.0 >= 0 && down.0 < grid.len() as i32 && down.1 >= 0 && down.1 < grid[0].len() as i32 && !seen.contains(&(down.0 as usize, down.1 as usize)) {
            valid_coords.push((down.0 as usize, down.1 as usize));
        }
        if left.0 >= 0 && left.0 < grid.len() as i32 && left.1 >= 0 && left.1 < grid[0].len() as i32 && !seen.contains(&(left.0 as usize, left.1 as usize)) {
            valid_coords.push((left.0 as usize, left.1 as usize));
        }
        if right.0 >= 0 && right.0 < grid.len() as i32 && right.1 >= 0 && right.1 < grid[0].len() as i32 && !seen.contains(&(right.0 as usize, right.1 as usize)) {
            valid_coords.push((right.0 as usize, right.1 as usize));
        }

        valid_coords
    }

    pub fn swim_in_water(grid: Vec<Vec<i32>>) -> i32 {
        let mut seen: HashSet<(usize,usize)> = HashSet::new();
        let mut min_heap = BinaryHeap::new();

        seen.insert((0,0));

        let mut t = grid[0][0];
        //                    val,R,C
        min_heap.push(Reverse((t,0,0)));

        while min_heap.len() > 0 {
            let c = min_heap.pop().unwrap().0;
            let c_val = c.0;
            let c_r = c.1;
            let c_c = c.2;
            seen.insert((c_r,c_c));

            if c_val > t {
                t = c_val;
            }

            if c_r == grid.len()-1 && c_c == grid[0].len()-1 {
                break;
            }

            let valid_coords = Solution::get_valid_next_coords((c_r,c_c), &seen, &grid);
            for coord in valid_coords {
                let coord_val = grid[coord.0][coord.1];
                min_heap.push(Reverse((coord_val,coord.0,coord.1)));
            }
        }

        t
    }
}

fn main() {
    let grid = vec![
        vec![0,1],
        vec![2,3],
    ];

//    let grid = vec![
//        vec![0,1,2,10],
//        vec![9,14,4,13],
//        vec![12,3,8,15],
//        vec![11,5,7,6],
//    ];
//
//    let grid = vec![
//        vec![10,12,4,6],
//        vec![9,11,3,5],
//        vec![1,7,13,8],
//        vec![2,0,15,14],
//    ];

    dbg!(Solution::swim_in_water(grid));
}
