def draw_line(size, i):
    offset = (size - i - 1) * ' '
    content = ("* " * (i + 1)).strip()
    print(f'{offset}{content}')


def draw_rhombus(size):
    for i in range(size):
        draw_line(size, i)

    for i in range(size - 2, -1, -1):
        draw_line(size, i)


draw_rhombus(int(input()))


##########################
### v2

def generate_line(count, symbol, offset_count=0):
    offset = offset_count * " "
    content = (f"{symbol} " * count).strip()
    return f'{offset}{content}'


def draw_line(count, symbol, offset_count=0):
    print(generate_line(count, symbol, offset_count))


def draw_rhombus(n):
    for i in range(n):
        draw_line(i + 1, '*', n - i - 1)

    for i in range(n -  2, -1, -1):
        draw_line(i + 1, '*', n - i - 1)


draw_rhombus(int(input()))