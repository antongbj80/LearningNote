import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np

warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示
plt.rcParams['axes.unicode_minus'] = False  # 解决符号无法显示

#导入数据
data = pd.read_excel("8-8 表8.3.xlsx")
data.head()
print("输出数据矩阵为：\n",data)

#进行适用性检验
# Bartlett's球状检验
# KMO检验
#Bartlett球形检验用于检验变量之间是否相关独立，如果p值小于0.05则适合做因子分析；KMO用于检验变量之间的相关性取值在0-1之间，值越大相关性越强。
from factor_analyzer import FactorAnalyzer, calculate_kmo, calculate_bartlett_sphericity
kmo = calculate_kmo(data)
bartlett = calculate_bartlett_sphericity(data)
print(f'KMO:{kmo[1]}')
print(f'Bartlett:{bartlett[1]}')

print("通过上述两个检验结果，其中KM0>0.6,并且Bartlett检验P值<0.05,因而可以得出该数据可以适合使用因子分析方法\n")

print("---------------------------------------------------------\n")
print("---------------------------------------------------------\n")
print("下面就是答案，特征值和特征向量，以及协方差阵\n")
#计算协方差阵
covX = np.cov(data.T)   #计算协方差矩阵
print("计算出来的协方差阵为：\n",covX)
#求解协方差矩阵的特征值和特征向量
featValue, featVec = np.linalg.eig(covX)
print("输出协方差阵的特征值为：\n",featValue)
print("输出协方差阵的特征向量为：\n",featVec)
print("\n")
print("上面就是答案，协方差阵、特征值、特征向量\n")
print("---------------------------------------------------------\n")
print("---------------------------------------------------------\n")
print("下面就是答案，相关阵、特征值、特征向量\n")
#求相关系数矩阵
corrX = np.around(np.corrcoef(data.T), decimals=3)
print("输出相关系数矩阵：\n", corrX)
featValue1, featVec1 = np.linalg.eig(corrX)
print("输出相关阵的特征值为：\n",featValue1)
print("输出相关阵的特征向量为：\n",featVec1)
print("\n")
print("上面就是答案，相关阵、特征值、特征向量\n")
print("---------------------------------------------------------\n")
print("---------------------------------------------------------\n")

#因子提取
Load_Matrix = FactorAnalyzer(rotation=None, n_factors=len(data.T), method='principal')
Load_Matrix.fit(data)
f_contribution_var = Load_Matrix.get_factor_variance()
matrices_var = pd.DataFrame()
matrices_var["旋转前特征值"] = f_contribution_var[0]
matrices_var["旋转前方差贡献率"] = f_contribution_var[1]
matrices_var["旋转前方差累计贡献率"] = f_contribution_var[2]
print("输出旋转前的因子特征值，方差贡献率以及方差累计贡献率为：\n",matrices_var)

#
#旋转前的因子载荷矩阵
print("旋转前的因子载荷矩阵为：\n",Load_Matrix.loadings_)

#因子数量选择
eigenvalues = 1
N = 0
for c in matrices_var["旋转前特征值"]:
    if c >= eigenvalues:
        N += 1
    else:
        s = matrices_var["旋转前方差累计贡献率"][N-1]
        print("\n选择了" + str(N) + "个因子累计贡献率为" + str(s)+"\n")
        break

#因子数量的选取
# 主要用来看取多少因子合适，一般是取到平滑处左右，当然还要需要结合贡献率
import matplotlib
matplotlib.rcParams["font.family"] = "SimHei"
ev, v = Load_Matrix.get_eigenvalues()
print('\n相关矩阵特征值：', ev)
plt.figure(figsize=(8, 6.5))
plt.scatter(range(1, data.shape[1] + 1), ev)
plt.plot(range(1, data.shape[1] + 1), ev)
plt.title('特征值和因子个数的变化', fontdict={'weight': 'normal', 'size': 25})
plt.xlabel('因子', fontdict={'weight': 'normal', 'size': 15})
plt.ylabel('特征值', fontdict={'weight': 'normal', 'size': 15})
plt.grid()
plt.show()

#进行因子旋转后的因子载荷矩阵
Load_Matrix_rotated = FactorAnalyzer(rotation='varimax', n_factors=2, method='principal')
Load_Matrix_rotated.fit(data)
f_contribution_var_rotated = Load_Matrix_rotated.get_factor_variance()
matrices_var_rotated = pd.DataFrame()
matrices_var_rotated["特征值"] = f_contribution_var_rotated[0]
matrices_var_rotated["方差贡献率"] = f_contribution_var_rotated[1]
matrices_var_rotated["方差累计贡献率"] = f_contribution_var_rotated[2]
print("旋转后的载荷矩阵的贡献率")
print(matrices_var_rotated)
print("旋转后的成分矩阵")
print(Load_Matrix_rotated.loadings_)

#对结果进行可视化，绘制相关系数图
import seaborn as sns
import numpy as np

Load_Matrix = Load_Matrix_rotated.loadings_
df = pd.DataFrame(np.abs(Load_Matrix), index=data.columns)

plt.figure(figsize=(8, 8))
ax = sns.heatmap(df, annot=True, cmap="BuPu", cbar=False)
ax.yaxis.set_tick_params(labelsize=15)  # 设置y轴字体大小
plt.title("因子分析", fontsize="xx-large")
plt.ylabel("因子", fontsize="xx-large")  # 设置y轴标签
plt.show()  # 显示图片

#计算因子得分
# 计算因子得分（回归方法）（系数矩阵的逆乘以因子载荷矩阵）
f_corr = data.corr()# 皮尔逊相关系数
X1 = np.mat(f_corr)
X1 = np.linalg.inv(X1)
factor_score_weight = np.dot(X1, Load_Matrix_rotated.loadings_)
factor_score_weight = pd.DataFrame(factor_score_weight)
col = []
for i in range(N):
    col.append("factor" + str(i + 1))
factor_score_weight.columns = col
factor_score_weight.index = f_corr.columns
print("因子得分：\n", factor_score_weight)




