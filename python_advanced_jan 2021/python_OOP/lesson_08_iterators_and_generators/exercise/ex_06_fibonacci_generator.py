def fibonacci():
    initial = 0
    second = 1
    while True:
        yield initial
        initial, second = second, initial + second


generator = fibonacci()
for i in range(10):
    print(next(generator))
