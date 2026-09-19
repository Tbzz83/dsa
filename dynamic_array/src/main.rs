use crate::{dynamic_array::DynArray, testing::testing};

mod dynamic_array;
mod testing;

fn main() {
    let mut dyn_array: DynArray<i32> = DynArray::with_capacity(1);

    for i in 0..1000 {
        dyn_array.push(i);
    }

    dbg!(dyn_array);
}
