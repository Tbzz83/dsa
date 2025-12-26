use std::{cell::RefCell, rc::Rc};

#[derive (Debug, Clone)]
pub struct Node<T: std::fmt::Display> {
    pub value: Option<T>,
    pub next: Option<Rc<RefCell<Node<T>>>>,
}

//#[derive (Debug)]
//pub struct NodeIter<'a> {
//    cur: &'a Node
//}

impl <T> std::fmt::Display for Node<T>
where T: std::fmt::Display {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        if let Some(ref val) = self.value {
            return write!(f, "{}", val);
        }

        write!(f, "None")
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

impl <T>Node<T>
where T: std::fmt::Display + std::fmt::Debug {
    pub fn new(value: T) -> Self {
        Self { value: Some(value), next: None }
    }

//    pub fn iter(&self) -> NodeIter<'_> {
//        NodeIter {
//            cur: self
//        }
//    }
    

    // Deletes the ith element of the linked list, and returns
    // node that was passed in. The root of the linked list should
    // be passed in, or else memory leaks can be created with 
    // orphaned previous nodes.
    pub fn delete_ith(mut self, i: i32) -> Result<Node<T>, String> {
        if i < 0 {
            return Err(format!("index to delete must be greater than 0. got {i}").into());
        }

        let mut j = 0;

        if self.next.is_none() {
            if i == 0 {
                return Ok(
                    Node { value: None, next: None }
                )
            } else {
                return Err(
                    format!("index {i} out of range")
                );
            }
        } else {
            // Return next node
            if i == 0 {
                let next = self.next
                    .clone()
                    .unwrap();

                self.next = None;

                let ref_cell = Rc::try_unwrap(next)
                    .ok()
                    .unwrap()
                    .into_inner();

                return Ok(
                    ref_cell
                )

            }

            // If trying to delete the second node
            if i == 1 {
                self.next = self.next
                    .take()
                    .unwrap()
                    .borrow()
                    .next
                    .clone();

                return Ok(self);
            }
        }

        let mut cur = self.next.clone().unwrap();
        j += 1;

        loop {
            let next_node = cur.borrow_mut().next.clone();

            match next_node {
                // index out of range
                None => {
                    return Err(
                        format!("index {i} out of range")
                    );
                },
                Some(next) => {
                    // Need to delete next
                    if j+1 == i {
                        let mut next_next = next.borrow().next.clone();
                        cur.borrow_mut().next = next_next.take();
                        break;
                    }

                    // update cur
                    cur = next;
                }
            }
        }

        Ok(self)
    }

    pub fn push(&mut self, value: T) {
    // 1. Handle empty list
    if self.next.is_none() {
        self.next = Some(Rc::new(RefCell::new(Node { value: Some(value), next: None })));
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
                cur.borrow_mut().next = Some(Rc::new(RefCell::new(Node { value: Some(value), next: None })));
                break; 
            }
        }
    }
}

    pub fn print(&self) {
        let mut print_str = format!("{:?}", self.value);

        if self.next.is_none() {
            println!("{print_str}");
            return;
        }

        let mut cur = self.next.clone().unwrap();

        loop {
            print_str += format!(" -> {:?}", cur.borrow().value).as_str();
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
