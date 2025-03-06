# a = 10
# b = 20
# c = a + b
# print( a, "+", b, "=", c)

# a = 50
# b = 10
# c = a - b
# print(a, "-", b, "=", c)

# a = 100
# b = 50
# c = a * b
# print(a, "*", b, "=", c)

# a = 20
# b = 4
# c = a / b
# print(a, "/", b, "=", c)

# a = 10
# b = 3
# c = a % b
# print(a, "%", b, "=", c)

# a = 10
# b = 5
# c = a ** b
# print(a, "**", b, "=", c)     # 10^5 = 100000    

# a = 10
# b = 3
# c = a // b
# print(a, "//", b, "=", c)     # 10//3 = 3

# a = 10
# b = 3
# c = a & b
# print(a, "&", b, "=", c)     # 10&3 = 2

# a = 10
# b = 3
# c = a | b
# print(a, "|", b, "=", c)     # 10|3 = 11

# a = 10
# b = 3
# c = a ^ b
# print(a, "^", b, "=", c)     # 10^3 = 9

# a = 10
# b = 3
# c = a << b
# print(a, "<<", b, "=", c)     # 10<<3 = 80

# a = 10
# b = 3
# c = a >> b
# print(a, ">>", b, "=", c)     # 10>>3 = 1

a,b,c = (input("请输入三角形三边的长：").split())
a= int(a)
b= int(b)
c= int(c)

#计算三角形的半周长p
p=(a+b+c)/2

#计算三角形的面积s
s=(p*(p-a)*(p-b)*(p-c))**0.5

#输出三角形的面积
print("三角形面积为：",format(s,'.2f'))