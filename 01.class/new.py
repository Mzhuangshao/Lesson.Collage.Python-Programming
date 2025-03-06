import random
import string
from datetime import datetime

# 获取当前时间
Time_now = datetime.now()

def generate_random_numbers_30(length=30):
    # 生成一个包含20个随机数字的字符串
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return random_numbers

def generate_random_numbers_8(length=8):
    # 生成一个包含20个随机数字的字符串
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return random_numbers

# def generate_random_letters(length=8):
#     letters = string.ascii_letters  # 包含大小写字母
#     random_string = ''.join(random.choice(letters) for i in range(length))
#     return random_string

def generate_random_letters_and_numbers_8(length=8):
    # 定义字母和数字的集合
    characters = string.ascii_letters + string.digits
    # 随机选择字符并生成字符串
    random_letters_and_numbers = ''.join(random.choice(characters) for _ in range(length))
    return random_letters_and_numbers

print("门店：微盟广告（上海）有限公司")
print("订单号：",generate_random_numbers_8())
print("商户订单号：",generate_random_letters_and_numbers_8())
print("微信支付交易号：",generate_random_numbers_30())
print("结账时间：", Time_now.strftime("%Y-%m-%d %H:%M:%S"))
print("==================")
print("消费总额：¥100.00")
print("优惠金额：¥0.00")
print("应付金额：¥100.00")
