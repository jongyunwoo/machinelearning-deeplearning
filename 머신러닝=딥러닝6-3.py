#주성분 분석
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
fruits = np.load('/Users/ujong-yun/Downloads/fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100)
pca = PCA(n_components=50)
pca.fit(fruits_2d)
print(pca.components_.shape)
def draw_fruits(arr, ratio = 1):
    n = len(arr)
    rows = int(np.ceil(n / 10))
    cols = n if rows < 2 else 10
    fig, ax = plt.subplots(rows, cols, figsize=(cols*ratio, rows*ratio), squeeze=False)
    for i in range(rows):
        for j in range(cols):
            if i*10 + j < n:
                ax[i, j].imshow(arr[i*10 + j], cmap='gray_r')
            ax[i, j].axis('off')
    plt.show()

draw_fruits(pca.components_.reshape(-1, 100, 100))
print(fruits_2d.shape)
fruits_pca = pca.transform(fruits_2d)
print(fruits_pca.shape)

#원본 데이터 재구성
fruits_inverse = pca.inverse_transform(fruits_pca)
print(fruits_inverse)

fruits_reconstruct = fruits_inverse.reshape(-1, 100, 100)
for start in [0, 100, 200]:
    draw_fruits(fruits_reconstruct[start:start+100])
    print("\n")

#설명된 분산
print(np.sum(pca.explained_variance_ratio_))
plt.plot(pca.explained_variance_ratio_)
plt.show()

#다른 알고리즘과 함꼐 사용하기
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
target = np.array([0]*100 + [1]*100 + [2]*100)

from sklearn.model_selection import cross_validate
scores = cross_validate(lr, fruits_2d, target)
print(np.mean(scores['test_score']))
print(np.mean(scores['fit_time']))

scores_pca = cross_validate(lr, fruits_pca, target)
print(np.mean(scores_pca['test_score']))
print(np.mean(scores_pca['fit_time']))

pca = PCA(n_components=0.5)
pca.fit(fruits_2d)
print(pca.n_components_)
fruits_pca = pca.transform(fruits_2d)
print(fruits_pca.shape)

scores = cross_validate(lr, fruits_pca, target)
print(np.mean(scores['test_score']))
print(np.mean(scores['fit_time']))

from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_pca)
print(np.unique(km.labels_, return_counts=True))

for label in range(0, 3):
    draw_fruits(fruits[km.labels_ == label])
    print('\n')

for label in range(0, 3):
    data = fruits_pca[km.labels_ == label]
    plt.scatter(data[:, 0], data[:, 1])
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s = 100, color = 'r', marker='*')
plt.legend(['apple', 'banana', 'pineapple'])
plt.show()