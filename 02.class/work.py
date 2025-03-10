def calculator():
    print("输入第一个数字:")
    num1 = float(input())
    print("输入运算符 (+, -, *, /):")
    operator = input()
    print("输入第二个数字:")
    num2 = float(input())

    if operator == '+':
        result = num1 + num2
        print(f"结果: {num1} + {num2} = {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"结果: {num1} - {num2} = {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"结果: {num1} * {num2} = {result}")
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"结果: {num1} / {num2} = {result}")
        else:
            print("错误: 除数不能为零。")
    else:
        print("错误: 未知的运算符，请输入 '+', '-', '*', 或 '/'。")

if __name__ == "__main__":
    calculator()
