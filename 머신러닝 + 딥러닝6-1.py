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

#샘풀별 평균
plt.hist(np.mean(apple, axis=1), alpha = 0.8)
plt.hist(np.mean(pineapple, axis=1), alpha = 0.8)
plt.hist(np.mean(banana, axis=1), alpha=0.8)
plt.legend(['apple', 'pineapple', 'banana'])
plt.show()

#픽셀의 평균
fig, ax = plt.subplots(1, 3, figsize = (20, 5))
ax[0].bar(range(10000), np.mean(apple, axis = 0))
ax[1].bar(range(10000), np.mean(pineapple, axis = 0))
ax[2].bar(range(10000), np.mean(banana, axis = 0))
plt.show()

#픽셀의 평균 그림으로 나타내기
apple_mean = np.mean(apple, axis = 0).reshape(100, 100)
pineapple_mean = np.mean(pineapple, axis = 0).reshape(100, 100)
banana_mean = np.mean(banana, axis = 0).reshape(100, 100)
fig, ax = plt.subplots(1, 3, figsize=(20, 5))
ax[0].imshow(apple_mean, cmap = 'gray_r')
ax[1].imshow(pineapple_mean, cmap = 'gray_r')
ax[2].imshow(banana_mean, cmap = 'gray_r')
plt.show()

#평균값과 가까운 사진 고르기
abs_diff = np.abs(fruits - apple_mean)
abs_mean = np.mean(abs_diff, axis = (1, 2))
apple_index = np.argsort(abs_mean)[:100]
fig, ax = plt.subplots(10, 10, figsize = (10 , 10))
for i in range(10):
    for j in range(10):
        ax[i, j].imshow(fruits[apple_index[i*10+j]], cmap='gray_r')
        ax[i, j].axis('off') #좌표축 없애기 좌표축 보이게 하기 위해사 'on'으로 변경 또는 삭제
plt.show()