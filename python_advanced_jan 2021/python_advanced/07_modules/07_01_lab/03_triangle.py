def draw_line(n):
    # row = []
    # for j in range(1, n + 1):
    #     row.append(str(j))
    # print(" ".join(row))
    print(*[str(i) for i in range(1, n+1)], sep=" ")


def triangle(n):
    for i in range(1, n+1):
        draw_line(i)

    for i in range(n-1, 0, -1):
        draw_line(i)

triangle(5)