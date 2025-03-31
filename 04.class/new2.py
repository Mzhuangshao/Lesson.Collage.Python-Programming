number1 = 1
number2 = 1

for i in range(1, 10):                           # 外层循环控制行数
    for j in range(1, 10):                       # 内层循环控制列数
        if j > i:                                # 如果列数大于行数，则跳过当前迭代
            continue                             # 增加列数，继续下一次内层循环迭代
        print(f"{i} * {j} = {i * j}", end="\t")  # 打印当前行和列数的乘积
    print()                                      # 每完成一行的打印后，换行

i = 1
while i < 10:  # 外层循环控制行数
    j = 1
    while j < 10:  # 内层循环控制列数
        if j > i:  # 如果列数大于行数，则跳过当前迭代
            j += 1  # 增加列数，继续下一次内层循环迭代
            continue
        print(f"{i} * {j} = {i * j}", end="\t")  # 打印当前行和列数的乘积
        j += 1  # 增加列数
    print()  # 每完成一行的打印后，换行
    i += 1  # 增加行数，继续下一次外层循环迭代
