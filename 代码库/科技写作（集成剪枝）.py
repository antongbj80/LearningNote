from sklearn.ensemble import RandomForestClassifier, VotingClassifier,BaggingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_wine,load_breast_cancer,load_iris

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target


# 这里假设我们有一个名为X的特征数据集和一个名为y的标签数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=531)

# 初始化多个基分类器
clf1 = RandomForestClassifier(n_estimators=500, random_state=42)
clf4 = BaggingClassifier(n_estimators=100, random_state=531)
clf2 = SVC(kernel='linear', probability=True)
clf3 = GaussianNB()

# 构建集成模型
eclf = VotingClassifier(estimators=[('rf', clf1), ('svc', clf2), ('nb', clf3),("rf2",clf4)], voting='soft')

# 训练集成模型
eclf.fit(X_train, y_train)

# 预测
y_pred = eclf.predict(X_test)

# 评估性能
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

# 计算每个基分类器的准确率，并分配权重
weights = [accuracy_score(y_test, clf.predict(X_test)) for clf in eclf.estimators_]
print(weights)

# 使用权重对集成模型进行剪枝
eclf_final = VotingClassifier(estimators=[('rf', clf1), ('svc', clf2), ('nb', clf3),("rf2",clf4)], voting='soft', weights=weights)

# 重新训练剪枝后的集成模型
eclf_final.fit(X_train, y_train)

# 使用最终的集成模型进行预测
y_pred_final = eclf_final.predict(X_test)

# 评估性能
accuracy_final = accuracy_score(y_test, y_pred_final)
print("Final Accuracy: ", accuracy_final)
