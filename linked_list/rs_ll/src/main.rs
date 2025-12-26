use std::rc::Rc;

use crate::node::Node;

mod node;

fn main() {

    let mut head = Node::new("a");

    head.push("b");
    head.push("c");
    head.push("d");
    head.push("e");
    //head.delete_ith(1);
    head.print();
    head = head.delete_ith(3).unwrap();
    head.print();

    let x = Rc::new(10);
    *x += 1;

    //head.delete_ith(1);
}
