from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import model_selection
from sklearn import metrics
import numpy as np

df = pd.read_csv('C:\\Users\\Lwen\\Desktop\\my-AI-homework\\week5\\Carlicense.csv')
df['number'] = np.array(range(0, 204))
data = df.iloc[0:61, :]
df.plot(kind='scatter', x='Date', y='lowest price ', title='lowest price with Date')
plt.xlabel("Date")
plt.ylabel("lowest price")
plt.show()
df.plot(kind='scatter', x='Date',y='avg price',title='avg price with Date')
plt.xlabel("Date")
plt.ylabel("avg price")
plt.show()
df.plot(kind='scatter', x='Total number of license issued', y='avg price', title='avg price with Total number of license issued')
plt.xlabel('Total number of license issued')
plt.ylabel('avg price')
plt.show()
df.plot(kind='scatter', x='Total number of applicants', y='avg price', title='avg price with Total number of applicants')
plt.xlabel('Total number of applicants')
plt.ylabel('avg price')
plt.show()

X = data[['number']]
Y = data[['avg price']]

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size = 0.35, random_state=1)
regrT = LinearRegression()
regrT.fit(X_train, y_train)
print(regrT.intercept_, regrT.coef_)

y_train_pred = regrT.predict(X_train)
Y_test_pred = regrT.predict(X_test)
train_err = metrics.mean_squared_error(y_train, y_train_pred)
test_err = metrics.mean_squared_error(y_test, Y_test_pred)
print(f"训练集上预测均方误差为：{train_err},测试集上越策均方误差为{test_err}")
ps = regrT.score(X_test, y_test)
print(f"决定系数为：{ps}")
