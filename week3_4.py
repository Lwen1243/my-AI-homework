# 读取文件并绘图
import matplotlib as plt
import pandas as pd
import numpy as np

# 读取provinceGDP.csv文件中的各省GDP数据，保存到DataFrame对象
pg = pd.read_csv('/home/aistudio/data/data12847/ProvinceGDP.csv', index_col='Province')
print(pg)
# 计算各省人均GDP，增加到最后1列；(注意数据中的人口单位万人，GDP单位亿元)
pg['PERGDP'] = pg['GDP'] * (10 ** 8) / (pg['Population'] * 10000)
print(pg)
# 计算全国GDP总量
print(f"全国GDP总量为:{pg['GDP'].sum()}")
# 计算人口和GDP的相关系数
tmp = pg['GDP'].corr(pg['Population'])
print(f"人口和GDP的相关系数为{tmp}")
# 筛选出GDP>10000万亿的省份，显示省份和GDP值
print(pg[['GDP']].loc[pg['GDP'] > 10000])
# 将这些省份及GDP值保存到GDPTop.csv的文件中
ans = pg[['GDP']].loc[pg['GDP'] > 10000]
print(ans)
# 绘制GDP>10000亿的GDP柱状图（如下图），并保存为JPG图像
plt.rcParams['font.sans-serif'] = ['Kaiti']
ans.plot(kind='bar', title='Top GDP', linewidth=2, color='g', grid=True, alpha=0.9, use_index=True)
plt.savefig('TopGDP.jpg')
