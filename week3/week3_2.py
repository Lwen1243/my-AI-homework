# 创建一个Series对象存放学校一年内各类活动次数
import pandas as pd

# 创建Series对象存储如下信息：讲座:70, 演出:15, 科技赛:82，会议:20，球赛:8
act = pd.Series({"讲座": 70, "演出": 15, "科技赛": 82, "会议": 20, "球赛": 8})
# 增加活动：论坛:12；
a = pd.Series({"论坛": 12})
act = act.append(a)
# 修改演出对应的值为18
act["演出"] = 18
# 查询后3个活动
print(act[2:5])
# 查询次数大于20的活动
print(act[act.values > 20])
# 删除球赛的数据
act = act.drop(["球赛"])
print(act)
