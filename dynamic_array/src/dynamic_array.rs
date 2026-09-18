use std::{alloc::{Layout, alloc, alloc_zeroed, handle_alloc_error, realloc}, fmt::{Debug, Formatter}, marker::PhantomData, mem::{replace, take, zeroed}, ptr::read};


#[derive (Debug)]
pub struct DynArray<T> 
where T: Debug {
    capacity: usize,
    raw_dynamic_array: RawDynArray<T>,
}


impl <T>DynArray<T> 
where T: Debug {
    pub fn new() -> Self {
        Self::_new(10)
    }

    pub fn push(&mut self, t: T) {
        self.raw_dynamic_array.push(t);
    }

    pub fn with_capacity(capacity: usize) -> Self {
        Self::_new(capacity)
    }

    fn _new(capacity: usize) -> Self {
        Self {
            capacity: capacity,
            raw_dynamic_array: RawDynArray::new(capacity),
        }
    }
}

struct RawDynArray<T>
where T: Debug {
    layout: Layout,
    capacity: usize,

    // Head points the start of the DynArray whether 
    // there is valid data there or not
    head: *mut T,

    // Tail points to the last valid item if it exists
    end: Option<*mut T>,

    // Cur points to first valid item if it exists
    start: Option<*mut T>,
}

impl <T>RawDynArray<T> 
where T: Debug {
    pub fn new(capacity: usize) -> Self {
        unsafe {
            let capacity = capacity + 1;
            let layout = Layout::from_size_align(capacity,size_of::<T>()).expect("Error creating layout");
            let ptr = alloc(layout) as *mut T;
            if ptr.is_null() {
                handle_alloc_error(layout);
            }
            Self { 
                layout: layout,
                capacity: capacity,
                end: None,
                start: None,
                head: ptr,
            }
        }
    }
}

impl <T>RawDynArray<T> 
where T: Debug {
    pub fn push(&mut self, t: T) {
        unsafe {
            if self.is_empty() {
                dbg!("DynArray is empty");
                let start = self.head;
                *start = t;
                self.start = Some(start);
                self.end = Some(start.add(1));
                return;
            } 

            let mut end = self.end.expect("self.end must be set here");
            if end == self.head.add(self.capacity) {
                // RESIZE
                dbg!("DynArray at max capacity, cannot allocate more items");
                return;
            }

            end = end.add(1);
            *end = t;
            self.end = Some(end);
        }
    }

    fn is_empty(&self) -> bool {
        if let Some(start) = self.start {
            dbg!("Start exists");
            let end = self.end.expect("self.start cannot be Some with self.end is None");
            return !(start == end)
        }

        self.start.is_none() && self.end.is_none()
    }
}

impl <T>Debug for RawDynArray<T> 
where T: Debug {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        if self.is_empty() {
            return write!(f, "DynArray is empty");
        }

        let res: String;

        while let Some(cur) = self.start {
            unsafe {
                (*cur).fmt(f)?;
            }
        }

        write!(f,"End")
    }
}

impl <T>Iterator for RawDynArray<T> 
where T: Debug {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        unsafe {
            if let Some(start) = self.start {
                let end = self.end.expect("self.start cannot be Some with self.end is None");

                // At the end
                if start == end {
                    return None;
                }

                let next = start.add(1);

                let taken = replace(&mut *start, zeroed());

                self.start = Some(next);

                return Some(taken);
            } 
            None
        }
    }
}
