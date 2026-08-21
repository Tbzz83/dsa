/*
Of course, after 24 hours trying to solve this in Python 
I look online and see that Python handles integers arbitrarily so 
of course this solution doesn't work in Python.
*/
class Solution {
    public static int getSum(int a, int b) {
        int carry = (a&b) << 1;

        while (a != 0) {
            b = a ^ b;
            a = carry;
            carry = (a&b) << 1;
        }

        return b;
    }

    public static void main(String[] args) {
        int res = getSum(7, 100);
        System.out.println(res);
    }
}
