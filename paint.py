import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from Bio import SeqIO
import pandas as pd


#Сделаем lineplot на примере данных о зарегистрированных новорожденных детях по месяцам в 2012 году.

birth = {'Месяц': ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'], 'Число рожденных детей в 2012 году в России': [143790, 150544, 157323, 140563, 160160, 153359, 170949, 176707, 155869, 177661, 157272, 152066]}
sns.lineplot(data=birth, x='Месяц', y='Число рожденных детей в 2012 году в России')
plt.show()


#Построим распределение длин последовательностей в базе повторов RepBase

Rep_base = SeqIO.parse(open('/media/pro_milka/56b10cc5-cfc8-41ee-b57b-637401e16448/pro_milka/IMB/rep_base.fasta'),'fasta')
len_massiv = []
for object in Rep_base:
        name, sequence = object.id, str(object.seq)
        len_massiv.append(len(sequence))


Len = {'Sequence length': len_massiv}
sns.histplot(Len, x='Sequence length')
plt.show()

# Любимый график - boxplot, чтобы было посимпатичнее - разделим на группы
test_massiv = {'Value': np.random.normal(0, 1, 1000), 'Group':np.random.randint(0, 7, 1000)}
test_massiv = pd.DataFrame(test_massiv)
sns.boxplot(data=test_massiv, x='Group', y='Value', palette="Set3")
plt.show()



