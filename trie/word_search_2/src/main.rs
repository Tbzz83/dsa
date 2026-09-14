/*
Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
*/

use std::collections::{HashMap, HashSet, VecDeque};

struct Solution {}

#[derive (Clone, Debug)]
struct Node {
    coord: (usize,usize),
    children: HashMap<char, Vec<Node>>,
}

impl Node {
    fn new(coord: (usize,usize)) -> Self {
        Self { children: HashMap::new(), coord: coord }
    }
}


#[derive (Debug)]
struct Trie {
    root: Node,
}

impl Trie {
    fn new(coord: (usize,usize)) -> Self {
        Self { 
            root: Node::new(coord)
        }
    }

    fn populate(mut node: Node, board: &Vec<Vec<char>>, seen: &mut HashSet<(usize,usize)>) {
        if seen.contains(&node.coord) {
            return;
        }

        seen.insert(node.coord);

        let c = board[node.coord.0][node.coord.1];

        if !node.children.contains_key(&c) {
            node.children.insert(c, vec![]);
        }

        let directions = vec![
            (node.coord.0-1,node.coord.1),
            (node.coord.0+1,node.coord.1),
            (node.coord.0,node.coord.1+1),
            (node.coord.0,node.coord.1-1),
        ];

        for direction in directions {
            if !seen.contains(&direction) {
                let new_node = Node::new(direction);
                node.children.get_mut(&c).expect("node should have children already!").push(new_node.clone());
                Trie::populate(new_node, board, seen);
            }
        }
    }
}

impl Solution {
    pub fn find_words(board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
        let x = vec!["Hello".to_string()];
        let trie = Trie::new((0,0));

        Trie::populate(trie.root.clone(), &board, &mut HashSet::new());

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
