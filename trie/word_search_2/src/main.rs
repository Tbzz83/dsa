/*
Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
*/

struct Solution {}

use std::collections::HashSet;

#[derive (Debug, Default)]
struct Node {
    pub is_end_of_word: bool,
    pub children: [Option<Box<Node>>; 26]
}

impl Node {
    pub fn new() -> Self {
        Default::default()
    }

    pub fn add_word(&mut self, word: String) {
        let mut cur = self;
        for c in word.as_bytes() {
            let child_idx = (c - b'a') as usize;
            if cur.children[child_idx].is_none() {
                cur.children[child_idx] = Some(Box::new(Node::new()));
            }

            cur = cur.children[child_idx].as_mut().expect("Child node must exist");
        }
        cur.is_end_of_word = true;
    }
}

impl Solution {
    fn dfs(
        r: i32, 
        c: i32, 
        mut node: &mut Node, 
        mut cur_str: String, 
        rows: i32, 
        cols: i32, 
        board: &mut [Vec<char>],
        res: &mut HashSet<String>,
    ) 
    {
        const VISITED: char = '#';

        if (r < 0 || r >= rows) || (c < 0 || c >= cols) || board[r as usize][c as usize] == VISITED {
            return;
        }


        let next_char = board[r as usize][c as usize];
        let next_idx = ((next_char as u8) - b'a') as usize;
        if node.children[next_idx].is_none() {
            return
        }

        node = node.children[next_idx].as_mut().expect("Key should exist");
        cur_str += &next_char.to_string();
        if node.is_end_of_word && !res.contains(&cur_str) {
            res.insert(cur_str.clone());
        }
        let prior = std::mem::replace(&mut board[r as usize][c as usize], VISITED);

        Self::dfs(r+1,c,node,cur_str.clone(),rows,cols,board,res);
        Self::dfs(r-1,c,node,cur_str.clone(),rows,cols,board,res);
        Self::dfs(r,c+1,node,cur_str.clone(),rows,cols,board,res);
        Self::dfs(r,c-1,node,cur_str.clone(),rows,cols,board,res);

        let _ = std::mem::replace(&mut board[r as usize][c as usize], prior);
    }

    pub fn find_words(mut board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
        let mut root = Node::new();
        let mut res: HashSet<String> = HashSet::new();

        for word in words {
            root.add_word(word);
        }

        let rows = board.len() as i32;
        let cols = board[0].len() as i32;

        for r in 0..rows {
            for c in 0..cols {
                Self::dfs(r,c,&mut root,"".to_string(),rows,cols, &mut board, &mut res);
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
