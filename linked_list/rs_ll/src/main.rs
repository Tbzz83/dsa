use std::ptr::{null, null_mut};


#[derive (Debug)]
struct LinkedList<T> 
where T: std::fmt::Debug + std::fmt::Display,
{
    head: *mut Node<T>,
    tail: *mut Node<T>,
}

#[derive (Debug)]
struct Node<T>
where T: std::fmt::Debug + std::fmt::Display,
{
    value: Option<T>,
    next: *mut Node<T>,
    prev: *mut Node<T>,
}

impl <T>LinkedList<T>
where T: std::fmt::Debug + std::fmt::Display,
{
    pub fn new() -> Self {
        let empty: *mut Node<T> = null_mut();
        LinkedList { 
            head: empty, 
            tail: empty,
        }
    }

    // Push a new element to the front of the linked list. 
    fn push(&mut self, val: T) {
        let new_node = Box::into_raw(Box::new(Node {
            value: Some(val),
            next: self.head,
            prev: null_mut(),
        }));

        unsafe {
            if !self.head.is_null() {
                (*self.head).prev = new_node;
            } 
        }

        self.head = new_node;
    }

    // Pops from the right
    fn pop(&mut self) -> Box<Node<T>> {
        unsafe {
            let prev = (*self.tail).prev;
            let popped = Box::from_raw(self.tail);
            self.tail = prev;
            popped
        }
    }

    fn print(&self) {
        let mut cur: *const Node<T> = self.head;
        while !cur.is_null() {
            unsafe {
                println!("{:?}", *cur);
                cur = (*cur).next;
            }
        }
    }
}

impl <T>Node<T>
where T: std::fmt::Debug + std::fmt::Display,
{
    pub fn new() -> Self {
        Node { 
            value: None,
            next: null_mut(),
            prev: null_mut() 
        }
    }
}

fn main() {
    let mut new_list = LinkedList::<i32>::new();

    new_list.push(1);
    new_list.push(2);
    new_list.push(3);
    new_list.push(4);
    new_list.print();
    let popped = new_list.pop();
    new_list.print();
}
