from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier


# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=531)

# 创建随机森林模型
rf_model = RandomForestClassifier(n_estimators=500, random_state=531)
rf_model.fit(X_train, y_train)

# 评估模型在测试集上的表现
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("未剪枝模型的准确率：", accuracy)

# 使用剪枝算法剪枝模型
rf_model_pruned = RandomForestClassifier(n_estimators=500, random_state=531, ccp_alpha=0.01)
rf_model_pruned.fit(X_train, y_train)

# 评估剪枝后的模型在测试集上的表现
y_pred_pruned = rf_model_pruned.predict(X_test)
accuracy_pruned = accuracy_score(y_test, y_pred_pruned)
print("剪枝后模型的准确率：", accuracy_pruned)

