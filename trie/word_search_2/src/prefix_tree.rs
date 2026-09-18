use std::collections::HashMap;




#[derive (Debug)]
pub struct Node {
    pub is_end_of_word: bool,
    pub children: HashMap<char,Node>
}

impl Node {
    pub fn new() -> Self {
        Self {
            is_end_of_word: false,
            children: HashMap::new(),
        }
    }

    pub fn add_word(&mut self, word: String) {
        let mut cur = self;
        for c in word.chars() {
            if !cur.children.contains_key(&c) {
                cur.children.insert(c, Node::new());
            }

            cur = cur.children.get_mut(&c).expect("Key should have been set but is empty");
        }
        cur.is_end_of_word = true;
    }
}
