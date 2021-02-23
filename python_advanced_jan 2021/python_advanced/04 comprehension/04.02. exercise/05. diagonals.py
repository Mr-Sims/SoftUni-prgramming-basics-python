def read_matrix():
    return [[int(el) for el in input().split(", ")] for i in range(int(input()))]


def primary_diagonal(matrix):
    return [matrix[i][i] for i in range(len(matrix))]


def secondary_diagonal(matrix):
    return [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]


matrix = read_matrix()
print(f"First diagonal: {', '.join(str(n) for n in primary_diagonal(matrix))}. Sum: {sum(primary_diagonal(matrix))}")
print(f"Second diagonal: {', '.join(str(n) for n in secondary_diagonal(matrix))}. Sum: {sum(secondary_diagonal(matrix))}")

####################################################################################################3
####### someone else`s soluton - not mine:


def input_matrix() -> [[int]]:
    square_size = int(input())
    return [[int(n) for n in input().split(", ")] for _ in range(square_size)]


def print_diagonals_and_their_sums(matrix) -> str:
    size = len(matrix)

    def first_diagonal():
        return [matrix[i][i] for i in range(size)]

    def second_diagonal():
        return [matrix[i][size - 1 - i] for i in range(size)]

    return f"""First diagonal: {', '.join(str(n) for n in first_diagonal())}. Sum: {sum(first_diagonal())}
Second diagonal: {', '.join(str(n) for n in second_diagonal())}. Sum: {sum(second_diagonal())}"""


print(print_diagonals_and_their_sums(input_matrix()))

