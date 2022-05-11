import pandas as pd
from sklearn.datasets import load_wine

wine=load_wine()
wine


df_wine = pd.DataFrame(wine.data,columns=wine.feature_names)
df_wine


wine.target


df_wine["class"]=wine.target
df_wine.head()


from sklearn.preprocessing import StandardScaler
#iloc[行][列] iloc[:]→all python 配列 [始まり:終わり] or [始まり:終わり:スキップする数] 
# or [始まり:終わり, 行選択(次元選択)] 
X = df_wine.iloc[:, :-1].values
y = df_wine.iloc[:, -1].values
sc = StandardScaler()
X_std = sc.fit_transform(X)


import numpy as np
cov_mat = np.cov(X_std.T)
#固有値と固有ベクトルを求める
eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)


eigen_vecs


eigen_vecs[:,0]


eigen_vecs[0]


eigen_vecs[:1]


eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:,i]) for i in range(len(eigen_vals))]


eigen_pairs


eigen_pairs.sort(key=lambda k: k[0], reverse=True)


eigen_pairs


w1 = eigen_pairs[0][1]
w1


w2 = eigen_pairs[1][1]
w2


# 射影行列の作成
W = np.stack([w1, w2], axis=1)
# 次元圧縮 (13次元 -> 2次元)
X_pca = X_std @ W


# データの可視化
import matplotlib.pyplot as plt

colors = ['#de3838', '#007bc3', '#ffd12a']  # 緋色、露草色、山吹色 
markers = ['o', 'x', ',']
for l, c, m, in zip(np.unique(y), colors, markers):
    plt.scatter(X_pca[y==l, 0], X_pca[y==l, 1],
                c=c, marker=m, label=l)


plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend()
plt.show()


from sklearn.decomposition import PCA

# 次元圧縮 (13次元 -> 2次元)
X_pca = PCA(n_components=2, random_state=42).fit_transform(X_std)  # n_componentsは圧縮後の次元数


# データの可視化
import matplotlib.pyplot as plt

colors = ['#de3838', '#007bc3', '#ffd12a']  # 緋色、露草色、山吹色 
markers = ['o', 'x', ',']
for l, c, m, in zip(np.unique(y), colors, markers):
    plt.scatter(X_pca[y==l, 0], X_pca[y==l, 1],
                c=c, marker=m, label=l)


plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend()
plt.show()



