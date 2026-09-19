use std::{alloc::{Layout, alloc, alloc_zeroed, handle_alloc_error, realloc}, fmt::{Debug, Display, Formatter}, marker::PhantomData, mem::{replace, take, zeroed}, ptr::read};

#[derive (Debug)]
pub struct DynArray<T> 
where T: Debug {
    raw_dynamic_array: RawDynArray<T>,
}

impl <T>Iterator for DynArray<T>
where T: Debug {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        self.raw_dynamic_array.next()
    }
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
            let capacity = capacity;
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
                // REALLOC
                self.realloc();
                self.push(t);
                return;
            }

            *end = t;
            end = end.add(1);
            self.end = Some(end);
        }
    }

    // Clones the ptrs to self.start and self.end and returns them should they both
    // exist. Handles the exception where one may exist without the other, which 
    // shouldn't be possible
    unsafe fn get_start_and_end_ptr_raw(&self) -> Option<(*mut T, *mut T)> {
        if let Some(start) = self.start {
            let end = self.end.expect("self.start cannot be Some with self.end is None");
            return Some((start.clone(), end.clone()));
        }

        None

    }

    
    fn realloc(&mut self) {
        todo!("Realloc currently broken, as it returns `invalid next size`. https://users.rust-lang.org/t/question-about-realloc/87755/7");
        // Double the size of our container each realloc
        let old_capacity = self.capacity;
        let capacity = self.capacity * 2;


        unsafe {
            let exists = self.get_start_and_end_ptr_raw();

            let offset: isize;
            if let Some((start,end)) = exists {
                offset = end.offset_from(start);
            } else {
                offset = 0;
            }

            let ptr = realloc(self.head as *mut u8, self.layout, capacity) as *mut T;
            if ptr.is_null() {
                handle_alloc_error(self.layout);
            }

            self.head = ptr;
            self.start = Some(self.head);
            self.end = Some(self.head.add(offset as usize));
        }

        // Update our final capacity
        self.capacity = capacity;
        dbg!(format!("Successfully resized our DynArray to capacity of {capacity}. (Old capacity was {old_capacity})"));
    }

    fn is_empty(&self) -> bool {
        if let Some(start) = self.start {
            let end = self.end.expect("self.start cannot be Some with self.end is None");
            return start == end
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

        if let Some(mut cur) = self.start {
            let end = self.end.expect("self.start cannot be Seom while self.end is None");
            while cur != end {
                unsafe {
                    //(*cur).fmt(f)?;
                    Debug::fmt(&(*cur), f);
                    cur = cur.add(1);
                }
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
