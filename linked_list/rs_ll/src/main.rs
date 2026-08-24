use crate::linked_list::LinkedList;

mod linked_list;

fn main() {

    let mut ll = LinkedList::<i32>::new();
    ll.push(1);
    ll.push(2);
    ll.push(3);

    let my_vec: Vec<i32> = vec![1,2,3,4];

    for val in &my_vec {
        dbg!(val);
    }
}
