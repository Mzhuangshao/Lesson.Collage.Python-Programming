def sort_three_numbers(x, y, z):
    # 将三个数放入列表中
    numbers = [x, y, z]
    # 对列表进行排序
    numbers.sort()
    # 输出排序后的列表
    return numbers

x = int(input("第一个整数: "))
y = int(input("第二个整数: "))
z = int(input("第三个整数: "))

sorted_numbers = sort_three_numbers(x, y, z)
print("从小到大排序:", sorted_numbers)