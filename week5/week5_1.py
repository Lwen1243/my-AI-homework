from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import model_selection
from sklearn import metrics
import numpy as np

df = pd.read_csv('C:\\Users\\Lwen\\Desktop\\my-AI-homework\\week5\\Salary.csv')
data = df.iloc[0:21, :]

X = data[['YearsExperience']]
Y = data[['Salary']]

x1 = df[['YearsExperience']]
y1 = df[['Salary']]

plt.scatter(x1, y1)
plt.xlabel('工龄')
plt.ylabel('薪水')
plt.title('工龄薪水散点图')
plt.show()

regr = LinearRegression()
regr.fit(x1, y1)
plt.scatter(x1, y1)
plt.plot(x1, regr.predict(x1), color='r')
plt.xlabel('工龄')
plt.ylabel('薪水')
plt.title('工龄薪水关系图')
plt.show()


X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size = 0.35, random_state=1)
regrT = LinearRegression()
regrT.fit(X_train, y_train)
# print(regrT.intercept_, regrT.coef_)

y_train_pred = regrT.predict(X_train)
Y_test_pred = regrT.predict(X_test)
train_err = metrics.mean_squared_error(y_train, y_train_pred)
test_err = metrics.mean_squared_error(y_test, Y_test_pred)
print(f"训练集上预测均方误差为：{train_err},测试集上越策均方误差为{test_err}")
ps = regrT.score(X_test, y_test)
print(f"决定系数为：{ps}")

new_x = np.array([[6.5]])
pridict = regr.predict(new_x)
print(f"预测工资为{pridict}")
