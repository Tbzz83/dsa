use crate::{dynamic_array::DynArray, testing::testing};

mod dynamic_array;
mod testing;

fn main() {
    let dyn_array: DynArray<i32> = DynArray::with_capacity(1);
    testing();
}
