width = int(input())
height = int(input())
length = int(input())
command = input()
size = width * height * length

while command != "Done":
    boxes = int(command)
    size -= boxes
    if size <= 0:
        break
    command = input()
if size > 0:
    print(f"{size} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(size)} Cubic meters more.")