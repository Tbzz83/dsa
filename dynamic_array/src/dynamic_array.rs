use std::{alloc::{Layout, alloc, alloc_zeroed, handle_alloc_error, realloc}, fmt::Debug, marker::PhantomData, mem::take, ptr::read};


#[derive (Debug)]
pub struct DynArray<T> {
    capacity: usize,
    raw_dynamic_array: RawDynArray<T>,
}


impl <T>DynArray<T> {
    pub fn new() -> Self {
        Self::_new(10)
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

#[derive (Debug)]
struct RawDynArray<T> {
    layout: Layout,
    capacity: usize,
    end: *mut Option<T>,
    ptr: *mut Option<T>,
}

impl <T>RawDynArray<T> {
    pub fn new(capacity: usize) -> Self {
        unsafe {
            let capacity = capacity + 1;
            let layout = Layout::from_size_align(capacity,size_of::<T>()).expect("Error creating layout");
            let ptr = alloc(layout) as *mut Option<T>;
            if ptr.is_null() {
                handle_alloc_error(layout);
            }
            Self { 
                layout: layout,
                capacity: capacity,
                end: ptr.add(capacity),
                ptr: ptr,
            }
        }
    }
}

impl <T>Iterator for RawDynArray<T> {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        unsafe {
            if self.end == self.ptr {
                return None
            }

            let next = self.ptr.add(1);

            //let x = next.as_mut();
            //return Some(take())
            None
        }
    }
}
