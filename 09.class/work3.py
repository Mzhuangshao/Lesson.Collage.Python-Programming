number_sum = 0
for number in range(1, 100):
    if number % 2 != 0:
        number_sum += number
    else:
        number_sum -= number
print("结果是:", number_sum)
