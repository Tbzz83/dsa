/*
Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
*/

use std::collections::{HashMap, HashSet, VecDeque};

struct Solution {}

#[derive (Clone, Debug)]
struct Node<'a> {
    coord: (usize,usize),
    children: HashMap<char, Vec<&'a Node<'a>>>,
}

impl <'a>Node<'a> {
    fn new(coord: (usize,usize)) -> Self {
        Self { children: HashMap::new(), coord: coord }
    }
}


#[derive (Debug)]
struct Trie<'a> {
    root: &'a Node<'a>,
}

impl <'a>Trie<'a> {
    fn new(root_node: &'a Node) -> Self {
        Self { 
            root: root_node
        }
    }

    fn get_valid_directions(coord: (usize,usize), board_height: i32, board_width: i32) -> Vec<(usize,usize)> {
        let mut res = vec![];
        let directions = vec![
            (coord.0 as i32 -1,coord.1 as i32),
            (coord.0 as i32 +1,coord.1 as i32),
            (coord.0 as i32 ,coord.1 as i32 +1),
            (coord.0 as i32,coord.1 as i32 -1),
        ];

        for direction in directions {
            if direction.0 < 0 || direction.0 >= board_height || direction.1 < 0 || direction.1 >= board_width {
                continue;
            }

            res.push((direction.0 as usize, direction.1 as usize));
        }

        res
    }

    fn populate(node: &mut Node, board: &Vec<Vec<char>>, seen: &mut HashSet<(usize,usize)>) {
        if seen.contains(&node.coord) {
            return;
        }

        seen.insert(node.coord);

        let c = board[node.coord.0][node.coord.1];

        if !node.children.contains_key(&c) {
            node.children.insert(c, vec![]);
        }

        for direction in Trie::get_valid_directions(node.coord, board.len() as i32, board[0].len() as i32) {
            if !seen.contains(&direction) {
                let mut new_node = Node::new(direction);
                node.children.get_mut(&c).expect("node should have children already!").push(&new_node);
                Trie::populate(&new_node, board, seen);
            }
        }
    }
}

impl Solution {
    pub fn find_words(board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
        let x = vec!["Hello".to_string()];
        let root_node = Node::new((0,0));
        let trie = Trie::new(&root_node);

        Trie::populate(trie.root, &board, &mut HashSet::new());

        dbg!(trie);
        x 
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
    let words = vec!["bad".into(), "ad".into()];
    dbg!(Solution::find_words(board, words));
}
