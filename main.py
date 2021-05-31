import matplotlib.pyplot as plt
import numpy as np

#Обычная картинка
path = '0017-200830.jpg'
pic = plt.imread(path)
plt.axis('off')
plt.imshow(pic)
plt.show()

#Сделаем ее в негативе:
img = 1 - pic
plt.imshow(img)
plt.axis('off')
plt.show()

#Сделаем менее насыщенный зеленый (двигаемся в сторону желтого)
pic2 = pic.copy()
pic2[:,:,2]=7
plt.imshow(pic2)
plt.axis('off')
plt.show()

#Воспользуемся парочкой фильтров из cmap:
pic3 = pic.copy()
plt.imshow(pic3.mean(axis=2), cmap='Greys')
plt.axis('off')
plt.show()

pic4 = pic.copy()
plt.imshow(pic4.mean(axis=2), cmap='spring')
plt.axis('off')
plt.show()

pic5 = pic.copy()
plt.imshow(pic5.mean(axis=2), cmap='summer')
plt.axis('off')
plt.show()

#Поищем кружочки в изображении двумя разными kernel:
pic = plt.imread('горох.JPG')

kernel = np.array([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
])

modified = np.zeros_like(pic.mean(2))
pic = pic.mean(2)

for row in range(2, pic.shape[0]-3):
    for col in range(2, pic.shape[1]-3):
        modified[row, col] = (pic[row-2:row+3, col-2:col+3]*kernel).mean()

plt.imshow(modified, cmap='Greys')
plt.axis('off')
plt.show()

###Сравним с таким вариантом (штраф за углы). Видно, что горох стал определяться лучше:

kernel = np.array([
    [-1, 0, 1, 0, -1],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [-1, 0, 1, 0, -1]
])

for row in range(2, pic.shape[0]-3):
    for col in range(2, pic.shape[1]-3):
        modified[row, col] = (pic[row-2:row+3, col-2:col+3]*kernel).mean()

plt.imshow(modified, cmap='Greys')
plt.axis('off')
plt.show()

