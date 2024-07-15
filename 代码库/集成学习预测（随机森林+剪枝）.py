import quandl
from sklearn import preprocessing
#df = quandl.get('WIKI/GOOGL')
df = quandl.get('WIKI/AAPL')
import math
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd


# print(df.head())
# print(df.columns.values) #查看所有的列标签
forecast_col = 'Adj. Close'  # 预测列变量
forecast_out = int(math.ceil(0.01 * len(df)))  # 定于预测天数，数据长度是0.01
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
# HL_PCT为股票最高价与最低价的变化百分比
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
# PCT_change为股票收盘价与开盘价的变化百分比
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# 为真正用到的特征字段
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
df.fillna(-99999, inplace=True)  # scikit-learn不处理空数据，故要把空数据设置为难出现的值
df['label'] = df[forecast_col].shift(-forecast_out)

# 模型最后使用的数据是X,y，以及预测的数据X_lately
X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]
df.dropna(inplace=True)
y = np.array(df['label'])

#回归分析，交叉验证
from sklearn import model_selection, svm
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2,random_state=1)

# 定义随机森林回归模型
rf1 = RandomForestRegressor(n_estimators=400, max_depth=10)
rf2 = RandomForestRegressor(n_estimators=400, max_depth=20)
rf3 = RandomForestRegressor(n_estimators=400, max_depth=30)

# 训练模型
rf1.fit(X_train, y_train)
rf2.fit(X_train, y_train)
rf3.fit(X_train, y_train)

# 在训练集上进行预测
train_preds1 = rf1.predict(X_train)
train_preds2 = rf2.predict(X_train)
train_preds3 = rf3.predict(X_train)

# 计算训练集上的均方误差
train_mse1 = mean_squared_error(y_train, train_preds1)
train_mse2 = mean_squared_error(y_train, train_preds2)
train_mse3 = mean_squared_error(y_train, train_preds3)

print('max_depth=10的训练集均方误差:', train_mse1)
print('max_depth=20的训练集均方误差:', train_mse2)
print('max_depth=30的训练集均方误差:', train_mse3)


# 在测试集上进行预测
test_preds1 = rf1.predict(X_test)
test_preds2 = rf2.predict(X_test)
test_preds3 = rf3.predict(X_test)

# 计算测试集上的均方误差
test_mse1 = mean_squared_error(y_test, test_preds1)
test_mse2 = mean_squared_error(y_test, test_preds2)
test_mse3 = mean_squared_error(y_test, test_preds3)
print('max_depth=10测试集均方误差:', test_mse1)
print('max_depth=20测试集均方误差:', test_mse2)
print('max_depth=30测试集均方误差:', test_mse3)
