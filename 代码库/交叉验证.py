from sklearn.datasets import load_wine
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import pandas as pd

# 读取数据
wine = load_wine()
X = wine.data
y = wine.target


# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 定义随机森林模型
rf = RandomForestClassifier()

# 定义参数网格
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30]
}

# 使用网格搜索进行交叉验证和参数调整
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

# 输出最佳参数组合
print(grid_search.best_params_)

# 使用最佳参数组合的模型进行交叉验证评估
best_rf = grid_search.best_estimator_
cv_scores = cross_val_score(best_rf, X_train, y_train, cv=5)
print('交叉验证得分:', cv_scores)
print('平均交叉验证得分:', cv_scores.mean())

# 在测试集上评估模型性能
test_score = best_rf.score(X_test, y_test)
print('测试集得分:', test_score)
