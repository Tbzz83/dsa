/*
You are given a signed 32-bit integer x.

Return x after reversing each of its digits. After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.

Solve the problem without using integers that are outside the signed 32-bit integer range.

solution:
Just because it's in the bitwise category doesn't mean you need to find some combination
of bitwise operations to solve this one...
Hey IDIOT! Yes you. Just use mod bro
123 % 10 = 12 with '3' remainder (returns 3)

So you can pretty easily see how you can use a combination of floor division and mod 
in order to build the new int (each new digit picked off through division is multiplied by 10 each iteration 
in order to build)

The hard part comes with knowing the overflow


if i32::MAX == 2147483647

then you know you're going to overflow when you are at the last digit,
and your current result is either:
equal to i32::MAX / 10 and the last digit is greater than 7

or

current result is greater than i32::MAX / 10

inverse true for negatives and bingo you're done!
*/


struct Solution;

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut num = x;
        let mut res = 0;

        while num != 0 {

            let next_digit = num % 10;

            if num / 10 == 0 && (((res == i32::MAX / 10) && (next_digit > i32::MAX % 10)) || res > i32::MAX / 10) {
                return 0;
            }

            if num / 10 == 0 && (((res < i32::MIN / 10 ) && (next_digit < i32::MIN % 10)) || res < i32::MIN / 10) {
                return 0;
            }
 
            res *= 10;
            res += next_digit;
            num = num / 10;
        }

        res
    }
}


fn main() {
    dbg!(format!("{:b}", 23));
    dbg!(format!("{:b}", 32));
    //dbg!(format!("{:b}", 100));
    dbg!(Solution::reverse(1234236467));
}
