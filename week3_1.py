# “天天”、“家乐”、“联华”和“农工”四个超市都卖苹果、香蕉、桔子和芒果四种水果。使用NumPy创建一维和二维数组对象，管理超市水果价格
import numpy as np
# 创建2个一维数组分别存储超市名称和水果名称
name = np.array(["天天", "家乐", "联华", "农工"])
fruit = np.array(["苹果", "香蕉", "桔子", "芒果"])
print(name)
print(fruit)
# 创建1个4×4的二维数组存放各超市的水果价格，价格由4到10的随机数生成
price = np.random.randint(4, 11, 16).reshape(4, 4)
print(price)
# 将“天天”的苹果价格增加1元
price[name == '天天', fruit == '苹果'] = price[name == '天天', fruit == '苹果'] + 1
print(price)
# 将“农工”的所有水果价格减少2元
price[name == '农工'] = price[name == '农工'] - 2
print(price)
# 统计四个超市各类水果的销售均价
apple = price[fruit == '苹果'].mean()
banana = price[fruit == '香蕉'].mean()
orange = price[fruit == '桔子'].mean()
mango = price[fruit == '芒果'].mean()
print(apple)
print(banana)
print(orange)
print(mango)
# 找出桔子价格最贵的超市名称（不是编号）
max_shop = name[price[fruit == '桔子'].argmax()]
print(max_shop)
