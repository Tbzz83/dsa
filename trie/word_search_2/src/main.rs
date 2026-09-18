/*
Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
*/

use std::collections::HashSet;

use crate::prefix_tree::Node;

mod prefix_tree;

struct Solution {}

impl Solution {
    fn dfs(
        r: i32, 
        c: i32, 
        mut node: &mut Node, 
        mut cur_str: String, 
        rows: i32, 
        cols: i32, 
        seen: &mut HashSet<(i32,i32)>, 
        board: &Vec<Vec<char>>,
        res: &mut HashSet<String>,
    ) 
    {
        if (r < 0 || r >= rows) || (c < 0 || c >= cols) || seen.contains(&(r,c)) {
            return;
        }

        let next_char = board[r as usize][c as usize];
        if !node.children.contains_key(&next_char) {
            return
        }

        node = node.children.get_mut(&next_char).expect("Key should exist");
        cur_str += &next_char.to_string();
        if node.is_end_of_word && !res.contains(&cur_str) {
            res.insert(cur_str.clone());
        }
        seen.insert((r,c));

        Self::dfs(r+1,c,node,cur_str.clone(),rows,cols,seen,board,res);
        Self::dfs(r-1,c,node,cur_str.clone(),rows,cols,seen,board,res);
        Self::dfs(r,c+1,node,cur_str.clone(),rows,cols,seen,board,res);
        Self::dfs(r,c-1,node,cur_str.clone(),rows,cols,seen,board,res);

        seen.remove(&(r,c));
    }

    pub fn find_words(board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
        let mut root = Node::new();
        let mut res: HashSet<String> = HashSet::new();

        for word in words {
            root.add_word(word);
        }

        let rows = board.len() as i32;
        let cols = board[0].len() as i32;

        for r in 0..rows {
            for c in 0..cols {
                Self::dfs(r,c,&mut root,"".to_string(),rows,cols,&mut HashSet::new(), &board, &mut res);
            }
        }

        res.into_iter().collect()
    }
}

fn main() {
    let board: Vec<Vec<char>> = vec![
      vec!['a','b','c','d'],
      vec!['s','a','a','t'],
      vec!['a','c','k','e'],
      vec!['a','c','d','n'],
    ];

    let board: Vec<Vec<char>> = vec![
        vec!['b','a'],
        vec!['o','d'],
    ];
    let words = vec!["cat".to_string(), "back".to_string(), "backend".to_string()];
    let words = vec!["bad".into(), "ad".into(), "badger".into()];
    dbg!(Solution::find_words(board, words));
}
