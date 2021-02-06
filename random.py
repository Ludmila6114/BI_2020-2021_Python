from time import time_ns
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#task1

def generate_i_values_random(i):
    sum = 0
    a = []
    start = time_ns()
    for j in range(i):
        a.append(random.random())
    finish = time_ns()
    time = finish - start
    sum = sum + time
    return sum

def generate_j_values_np(j):
    start = time_ns()
    b = np.random.random(size = j)
    finish = time_ns()
    return finish - start


x = np.arange(1000)
y1 = []
y2 = []
for values in np.arange(1000):
    y1.append(generate_i_values_random(values))
    y2.append(generate_j_values_np(values))

df1 = pd.DataFrame({'Value': x, 'Y': y1})
df2 = pd.DataFrame({'Value': x, 'Y': y2})
df1['Method'] = 'Python random'
df2['Method'] = 'Numpy random'
df = pd.concat([df1, df2])
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.set_ylabel('Time')
ax1.set_xlabel('Amount of values')
ax1.set_title('Comparative analysis of np.random and random generation')
sns.lineplot(x='Value',y='Y',data=df,hue='Method')
plt.show()

#result: It's faster to use numpy random.
#Task 2.

def is_sorted(arr):
    rez = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i + 1]:
            rez = False
    return rez

def monkey_sort(a):
    while is_sorted(a) != True:
        np.random.shuffle(a)
    return a

#Задаем число массивов, на котором это все будет теститься, их длина будет рандомной, но пусть небольшой (максимум 4)
N = 10
x = []
y = []

for i in range(N):
    mas = np.random.uniform(1, 100, size = np.random.randint(1, 5))
    time = []
    for j in range(3):
        mas_copy = mas.copy()
        start = time_ns()
        monkey_sort(mas_copy)
        end = time_ns()
        time.append(end - start)
    x.append(len(mas))
    y.append(sum(time)/len(time))

data = {'Size': x, 'Average time': y}
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.set_ylabel('Average time')
ax1.set_xlabel('Amount of values in array')
ax1.set_title('Monkey sorting time for arrays with different length')
sns.lineplot(x='Size',y='Average time',data=data)
plt.show()


#Task3 random walk
x = [0]
y = [0]
#N - число шагов
N = 100
for i in range(N):
    x.append(np.random.choice([x[-1] + 1, x[-1] - 1]))
    y.append(np.random.choice([y[-1]+1, y[-1]-1]))

data = {'X': x, 'Y': y}
fig3 = plt.figure()
ax1 = fig3.add_subplot(211)
ax1.set_ylabel('Y axis')
ax1.set_xlabel('X axis')
ax1.set_title('Random walk task')
sns.scatterplot(x='X',y='Y',data=data)
plt.show()

#Task 4. Перемешиваем буквы в тексте
Text = input().split()
for word in Text:
    word = list(word)
    if len(word) > 2:
        inside = word[1:len(word)-1]
        np.random.shuffle(inside)
        word_new = word[0] + ''.join(inside) + word[-1]
        print(word_new, end=' ')
    else:
        print(word, end=' ')





