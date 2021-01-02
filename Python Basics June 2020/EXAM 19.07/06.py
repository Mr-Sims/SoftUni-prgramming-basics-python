num1 = input()
num2 = input()
i1 = int(num1[0])
i2 = int(num2[0])
j1 = int(num1[1])
j2 = int(num2[1])
k1 = int(num1[2])
k2 = int(num2[2
l1 = int(num1[3])
l2 = int(num2[3])
for i in range(i1, i2+1):
    for j in range(j1, j2+1):
        for k in range(k1, k2 + 1):
            for l in range(l1, l2 + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f"{i}{j}{k}{l}", end = " ")