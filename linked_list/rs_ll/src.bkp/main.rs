use crate::node::Node;

mod node;

fn main() {
    let mut head = Node::new(1);

    head.push(2);
    head.push(3);

    //head.delete_ith(1);
}
