use std::rc::Rc;

use crate::node::Node;

mod node;

struct Data {
    val: Option<Rc<i32>>,
}

fn main() {

    let mut head = Node::new(1);

    head.push(2);
    head.push(3);
    head.push(4);
    head.push(5);
    //head.delete_ith(1);
    head.print();

    //head.delete_ith(1);
}
