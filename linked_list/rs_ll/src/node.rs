#[derive (Debug, Clone)]
pub struct Node {
    pub value: i32,
    pub next: Option<Box<Node>>,
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

impl <'a>Iterator for NodeIter<'a> {
    type Item = &'a Node;

    fn next(&mut self) -> Option<Self::Item> {
        if let Some(next) = &self.cur.next {
            // Advance iterator
            self.cur = next;
            return Some(next);
        }

        None
    }
}

impl <'a> IntoIterator for &'a Node {
    type Item = &'a Node;
    type IntoIter = NodeIter<'a>;

    fn into_iter(self) -> Self::IntoIter {
        self.iter()
    }
}

//impl IntoIterator for Node {
//    type Item = Node;
//    type IntoIter = ;
//
//}

impl Node {
    pub fn new(value: i32) -> Self {
        Self { value, next: None }
    }

//    pub fn delete_ith(&mut self, i: i32) {
//        if i == 0 {
//
//        }
//
//        let mut j = 0;
//
//        let mut cur = &mut self.next;
//
//        while let Some(node) = cur {
//            if j + 1 == i {
//                println!("j: {j} CASE");
//                if let Some(next) = &mut node.next {
//                    node.next = next.next;
//                }
//            }
//            cur = &mut node.next;
//            j += 1;
//        }
//    }

    pub fn iter(&self) -> NodeIter<'_> {
        NodeIter {
            cur: self
        }
    }

    pub fn push(&mut self, value: i32) {
        let mut cur = &mut self.next;

        while let Some(node) = cur {
            cur = &mut node.next;
        }

        *cur = Some(Box::new(Node::new(value)));
    }

    pub fn print(mut self) {
        let mut print_str = format!("{}", self.value);
        'outer: loop {
            if let Some(next) = self.next {
                self = *next;
                print_str += &format!(" -> {}", self.value);
            } else {
                break 'outer;
            }
        }
        println!("{print_str}");
    }
}
