V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

pipe_1_litres = P1 * H
pipe_2_litres = P2 * H
pool_fill = pipe_1_litres + pipe_2_litres
pipe_1_percentage = (pipe_1_litres / pool_fill) * 100
pipe_2_percentage = (pipe_2_litres / pool_fill) * 100
fill_percentage = (pool_fill / V) * 100

if V >= pool_fill:
    print(f"The pool is {(fill_percentage):.2f}% full. Pipe 1: {(pipe_1_percentage):.2f}%. Pipe 2: {(pipe_2_percentage):.2f}%.")
else:
    overflow = pool_fill - V
    print(f"For {H} hours the pool overflows with {(overflow)} liters.")