use std::alloc::{Layout, alloc, handle_alloc_error};


#[derive (Debug)]
struct Data {
    data: String,
}

pub fn testing() {
    unsafe {
        let layout = Layout::from_size_align(1, size_of::<i32>()).expect("ERROR CREATING LAYOUT");
        let mut ptr = alloc(layout);

        if ptr.is_null() {
            handle_alloc_error(layout);
        }

        *(ptr as *mut i32) = 1;
        ptr = ptr.offset(100);
        dbg!(*ptr);
    }

    let my_vec: Vec<Data> = vec![
        Data{data: String::from("Hello")},
    ];

    for num in my_vec {
        dbg!(num);
    }
}
