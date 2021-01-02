n = int(input())
total = 0

for i in range(1, n + 1):
    letter = input()
    total += ord(letter)
print(f"The sum equals: {total}")