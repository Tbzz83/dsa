def main():
    my_int_a = 5
    print(f"The binary representation of {my_int_a} is: {bin(my_int_a)[2:]}")

    my_binary = "111"

    print(f"The decimal representation of binary {my_binary} is: {int(my_binary, 2)}")

    my_int_b = 7

    print(f"bitwise AND of {my_int_a} and {my_int_b} is: {my_int_a & my_int_b}")
    print(f"bitwise OR of {my_int_a} and {my_int_b} is: {my_int_a | my_int_b}")
    print(f"bitwise XOR of {my_int_a} and {my_int_b} is: {my_int_a ^ my_int_b}")
    print(f"bitwise NOT of {my_int_a} is: {~my_int_a}")

    shift_magnitude = 1

    print(f"bitwise LEFT SHIFT of {my_int_a} << {shift_magnitude} is: {my_int_a << shift_magnitude}")
    print(f"bitwise RIGHT SHIFT of {my_int_a} >> {shift_magnitude} is: {my_int_a >> shift_magnitude}")

    print(f"Hex representation of {my_int_a*my_int_b} is: {hex(my_int_a*my_int_b)}")

if __name__ == "__main__":
    main()
