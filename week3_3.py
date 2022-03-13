# 创建并访问DataFrame对象
import pandas as pd
import numpy as np
# 创建3×3DataFrame数据对象：数据内容为1-9；行索引为字符a，b，c；列索引为字符串one，two，three；
data = np.array(np.arange(1, 10)).reshape(3, 3)
prpr = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['one', 'two', 'three'])
print(prpr)
# 查询列索引为two和three两列数据
print(prpr.loc[:, ['one', 'three']])
# 查询第0行、第2行、第0列、第2列数据
print(prpr.iloc[[0, 2], :])
print(prpr.iloc[:, [0, 2]])
# 筛选第1列中值大于2的所有行数据，保存到data1对象
data1 = prpr.loc[prpr['two'].loc[:] > 2]
print(data1)
# 为data1添加一列数据，列索引为four，值都为10
data1.insert(3, 'four', 10)
print(data1)
# 将data1所有值大于9的数据修改为8
for i in data1.index:
    data1.loc[i, data1.loc[i].values > 9] = 8
print(data1)
# 删除data1中第0行数据
tmp = data1.drop(list(data1.index[0]), axis=0)
print(tmp)
