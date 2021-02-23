# Finding all occurances of a value in a tuple

tt = (1, 2, 1, 2, 3, 6, 4, 3, 2, 3, 6, 8)

def get_indices(values, value):
    index = 0
    indices = []
    while True:
        try:
            new_index = values.index(value, index)
            indices.append(new_index)
            index = new_index + 1
        except ValueError:
            break
    return indices

print(get_indices(tt, 3))