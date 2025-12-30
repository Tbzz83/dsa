use std::{cell::RefCell, rc::Rc};

#[derive(Debug)]
pub struct LinkedList<T> {
    head: Link<T>,
    tail: Link<T>,
}

type Link<T> = Option<Rc<RefCell<Node<T>>>>;

#[derive(Debug)]
pub struct Node<T> {
    pub value: Option<T>,
    next: Link<T>,
    prev: Link<T>,
}

impl <T>Iterator for LinkedList<T> {
    type Item = Link<T>;
    fn next(&mut self) -> Option<Self::Item> {
        match self.pop_left() {
            Some(node) => return Some(Some(node)),
            None => return None,
        }
    }
}

impl <T>LinkedList<T> {
    pub fn new() -> Self {
        LinkedList { head: None, tail: None }
    }

    pub fn peek_left(&self) -> &Link<T> {
        &self.head
    }

    pub fn peek_right(&self) -> &Link<T> {
        &self.tail
    }

    pub fn append(&mut self, value: T) {
        let new_link: Link<T> = Some(Rc::new(RefCell::new(
            Node::new(value)
        )));
        // head empty
        if self.head.is_none() {
            self.head = new_link.clone();

            // tail also empty
            if self.tail.is_none() {
                // Can move here or clone
                self.tail = new_link;
            }
        } else {
            // Make current head next of new value being pushed
            self.tail.clone().map(|node| {
                node.borrow_mut().next = new_link.clone();
            });

            new_link.clone().map(|node| {
                node.borrow_mut().prev = self.tail.clone();
            });

            self.tail = new_link;
        }
    }

    pub fn push(&mut self, value: T) {
        let new_link: Link<T> = Some(Rc::new(RefCell::new(
            Node::new(value)
        )));
        // head empty
        if self.head.is_none() {
            self.head = new_link.clone();

            // tail also empty
            if self.tail.is_none() {
                // Can move here or clone
                self.tail = new_link;
            }
        } else {
            // Set head.prev == new_link
            self.head.clone().map(|node| {
                node.borrow_mut().prev = new_link.clone();
            });

            // Make current head next of new value being pushed
            new_link.clone().map(|node| {
                node.borrow_mut().next = self.head.take();
            });

            self.head = new_link;
        }
    }

    pub fn pop(&mut self) -> Link<T> {
        if self.tail.is_none() {
            return None;
        }

        let tail = self.tail.take();

        let prev = tail.clone().and_then(|node| {
            node.borrow_mut().prev.clone()
        });

        prev.clone().map(|node| {
            node.borrow_mut().next = None;
        });

        self.tail = prev;

        if self.tail.is_none() {
            self.head = None;
        }

        tail
    }

    // Pops from the left
    pub fn pop_left(&mut self) -> Link<T> {
        if self.head.is_none() {
            return None;
        }

        let head = self.head.take();
        let next = head.clone().and_then(|node| {
            node.borrow().next.clone()
        });

        next.clone().map(|node| {
            node.borrow_mut().prev = None;
        });

        self.head = next;

        // We removed the last node, need to remove the 
        // tail as well
        if self.head.is_none() {
            self.tail = None;
        }

        head
    }
}

impl <T>Node<T> {
    pub fn new(value: T) -> Self {
        Node { value: Some(value), next: None, prev: None }
    }

    fn set_next(&mut self, link: Link<T>) {
        self.next = link;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_node() {
        let new_node = Node::<i32>::new(1);
        //println!("{:?}", new_node);
    }

    #[test]
    fn test_list() {
        let mut new_list = LinkedList::<i32>::new();
        new_list.push(1);
        new_list.push(2);
        new_list.push(3);

        let popped = new_list.pop_left();
        assert_eq!(popped.clone().unwrap().borrow().value, Some(3));
        let popped = new_list.pop_left();
        assert_eq!(popped.clone().unwrap().borrow().value, Some(2));
        let popped = new_list.pop_left();
        assert_eq!(popped.clone().unwrap().borrow().value, Some(1));
        let popped = new_list.pop_left();
        assert!(popped.is_none());
        assert!(new_list.head.is_none());
        assert!(new_list.tail.is_none());
        let popped = new_list.pop_left();
        assert!(popped.is_none());

        new_list.append(1);
        new_list.append(2);
        new_list.append(3);

        let peek_left = new_list.peek_left();
        assert_eq!(peek_left.clone().unwrap().borrow().value, Some(1));
        let peek_right = new_list.peek_right();
        assert_eq!(peek_right.clone().unwrap().borrow().value, Some(3));

        let popped = new_list.pop_left();
        assert_eq!(popped.clone().unwrap().borrow().value, Some(1));
        let popped = new_list.pop_left();
        assert_eq!(popped.clone().unwrap().borrow().value, Some(2));
        let popped = new_list.pop_left();
        assert_eq!(popped.clone().unwrap().borrow().value, Some(3));
        let popped = new_list.pop_left();
        assert!(popped.is_none());

        new_list.push(1);
        new_list.push(2);
        new_list.push(3);

        let popped = new_list.pop();
        assert_eq!(popped.clone().unwrap().borrow().value, Some(1));
        let popped = new_list.pop();
        assert_eq!(popped.clone().unwrap().borrow().value, Some(2));
        let popped = new_list.pop();
        assert_eq!(popped.clone().unwrap().borrow().value, Some(3));
        let popped = new_list.pop();
        assert!(popped.is_none());

        dbg!(new_list);

    }
}
