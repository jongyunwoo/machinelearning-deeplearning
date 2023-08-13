import numpy as np
import matplotlib.pyplot as plt
fruits = np.load('/Users/ujong-yun/Downloads/fruits_300.npy')
print(fruits.shape)
print(fruits[0, 0, :])
plt.imshow(fruits[0], cmap = 'gray')
plt.show()
plt.imshow(fruits[0], cmap = 'gray_r')
plt.show()
fig, ax = plt.subplots(1, 2)
ax[0].imshow(fruits[100], cmap = 'gray_r')
ax[1].imshow(fruits[200], cmap = 'gray_r')
plt.show()

#픽셀값 분석하기
apple = fruits[0:100].reshape(-1, 100*100)
pineapple = fruits[100:200].reshape(-1, 100*100)
banana = fruits[200:300].reshape(-1, 100*100)
print(apple.mean(axis = 1))

plt.hist(np.mean(apple, axis=1), alpha = 0.8)
plt.hist(np.mean(pineapple, axis=1), alpha = 0.8)
plt.hist(np.mean(banana, axis=1), alpha=0.8)
plt.legend(['apple', 'pineapple', 'banana'])
plt.show()