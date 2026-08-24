N=20

start_point = N - 1
num_to_draw = 1
i = 1

while i <= N:
    print(" "*start_point + num_to_draw*"*")
    start_point -= 1
    num_to_draw += 2
    i += 1
