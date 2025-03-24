number1 = 1
number2 = 1

for i in range(1, 10):
    for j in range(1, 10):
        if j > i:
            continue
        print(f"{i} * {j} = {i * j}", end="\t")
    print()