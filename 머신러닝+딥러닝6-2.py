import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
fruits = np.load('/Users/ujong-yun/Downloads/fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100)
km = KMeans(n_clusters = 3, random_state=42)
km.fit(fruits_2d)
print(np.unique(km.labels_, return_counts=True))

#labels 그림 그리기
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

draw_fruits(fruits[km.labels_ == 0], 1)

draw_fruits(km.cluster_centers_.reshape(-1, 100, 100), ratio = 3)

print(km.transform(fruits_2d[100:101]))
print(km.predict(fruits_2d[100:101]))
draw_fruits(fruits[100:101])

#최적의 k값 찾기 elbow방법
inertia = []
for k in range(2, 7):
    km = KMeans(n_clusters=k, random_state = 42)
    km.fit(fruits_2d)
    inertia.append(km.inertia_)
plt.plot(range(2, 7), inertia)
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()