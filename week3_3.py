# 创建并访问DataFrame对象
import pandas as pd
# 创建3×3DataFrame数据对象：数据内容为1-9；行索引为字符a，b，c；列索引为字符串one，two，three；
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
prpr = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['one', 'two', 'three'])
print(prpr)
# 查询列索引为two和three两列数据
print(prpr.loc[:, ['one', 'three']])
# 查询第0行、第2行、第0列、第2列数据
print(prpr.iloc[[0, 2], :])
print(prpr.iloc[:, [0, 2]])
# 筛选第1列中值大于2的所有行数据，保存到data1对象

# 为data1添加一列数据，列索引为four，值都为10

# 将data1所有值大于9的数据修改为8

# 删除data1中第0行数据
