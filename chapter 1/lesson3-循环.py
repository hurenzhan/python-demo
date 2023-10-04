# while 循环基础用法
i = 0
while i < 10:
    print(i)
    i = i + 1

# while 99 乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {i * j}", end="\t")
        j += 1
    print()
    i += 1

# for 循环基础用法
for i in range(1, 10, 2):
    print(i)

# for 99 乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()