use std::{cell::RefCell, error::{}, fmt::Error, ops::DerefMut, rc::Rc};

#[derive (Debug, Clone)]
pub struct Node {
    pub value: i32,
    pub next: Option<Rc<RefCell<Node>>>,
}

#[derive (Debug)]
pub struct NodeIter<'a> {
    cur: &'a Node
}

impl std::fmt::Display for Node {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.value)
    }
}

//impl <'a>Iterator for NodeIter<'a> {
//    type Item = &'a Node;
//
//    fn next(&mut self) -> Option<Self::Item> {
//        if let Some(next) = &self.cur.next {
//            // Advance iterator
//            self.cur = next;
//            return Some(next);
//        }
//
//        None
//    }
//}

//impl <'a> IntoIterator for &'a Node {
//    type Item = &'a Node;
//    type IntoIter = NodeIter<'a>;
//
//    fn into_iter(self) -> Self::IntoIter {
//        self.iter()
//    }
//}

//impl IntoIterator for Node {
//    type Item = Node;
//    type IntoIter = ;
//
//}

impl Node {
    pub fn new(value: i32) -> Self {
        Self { value, next: None }
    }

    pub fn delete_ith(&self, i: i32) {

    }

    pub fn iter(&self) -> NodeIter<'_> {
        NodeIter {
            cur: self
        }
    }

    pub fn push(&mut self, value: i32) {
    // 1. Handle empty list
    if self.next.is_none() {
        self.next = Some(Rc::new(RefCell::new(Node { value, next: None })));
        return;
    }

    // 2. Start at the first node
    let mut cur = self.next.clone().unwrap();

    // 3. Walk to the end
    loop {
        // We need a block or a temp variable to drop the borrow before we mutate
        let next_node = cur.borrow().next.clone();

        match next_node {
            Some(next) => {
                cur = next; // Move cursor forward
            }
            None => {
                // We reached the end, insert and exit
                cur.borrow_mut().next = Some(Rc::new(RefCell::new(Node { value, next: None })));
                break; 
            }
        }
    }
}

    pub fn print(&self) {
        let mut print_str = format!("{}", self.value);

        if self.next.is_none() {
            println!("{print_str}");
            return;
        }

        let mut cur = self.next.clone().unwrap();

        loop {
            print_str += format!(" -> {}", cur.borrow().value).as_str();
            let next_node = cur.borrow().next.clone();

            match next_node {
                Some(next) => {
                    cur = next
                },
                None => break,
            }
        }

        println!("{print_str}");
    }
}
