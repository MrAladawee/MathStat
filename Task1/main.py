import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def mean_():
    return sum(Dataset['X']) / n

def median_():

    sorted_dataset = sorted(Dataset['X'])
    length = len(sorted_dataset)

    if n % 2 == 1:
        result = sorted_dataset[length // 2]
    else:
        result = (sorted_dataset[length // 2 - 1] + sorted_dataset[length // 2]) / 2

    return result

def dispersion():
    return sum(math.pow((xi - mean), 2) for xi in Dataset['X']) / (n - 1)

def assim():
    return (1/n) * sum(math.pow((xi - mean), 3) for xi in Dataset['X']) / (math.pow(std_dev, 3))


# Reading dataset
Dataset = pd.read_csv('r1z1.csv')

# Histogram and frequency table
min_arg = Dataset['X'].min()
hist_min = math.floor(min_arg)
max_arg = Dataset['X'].max()
hist_max = math.ceil(max_arg)
Delta = 1

bins = [_ + 0.05 for _ in range(hist_min, hist_max + 1, Delta)]
print(bins)
plt.hist(Dataset['X'], bins = bins, color = 'grey', edgecolor = 'black')

plt.title('Гистограмма силы удара')
plt.xlabel('Значения')
plt.ylabel('Количество')

plt.show()

# Empirical distribution function
sorted_data = np.sort(Dataset['X'])
n = len(sorted_data)

cff_values = np.arange(1, n + 1) / n
mean_x = np.mean(sorted_data)

plt.figure(figsize=(10,6))
plt.step(sorted_data, cff_values, where='pre')
plt.xlabel('Значения')
plt.ylabel('Эмпирическая Функция Распределения')
plt.title('Эмпирическая Функция Распределения данных')
plt.axhline(y = 0, color='black', linewidth=0.5)
plt.axvline(x = mean_x, color='black', linestyle='--', linewidth=0.5)
plt.show()

# Compare histograms
Dataset_1 = pd.read_csv('r1z2.csv')
Dataset_2 = pd.read_csv('r1z1.csv')

colors = ['#E69F00', '#56B4E9']
names = ['Dataset_1', 'Dataset_2']

combined_data = pd.concat([Dataset_1['X'], Dataset_2['X']])
X0 = math.floor(combined_data.min())
X_max = math.ceil(combined_data.max())

bins = [i + 0.05 for i in range(X0, X_max + 1, Delta)]

plt.hist([Dataset_1['X'], Dataset_2['X']], bins=bins, density=True,
         color=colors, label=names)
plt.legend()
plt.xlabel('Сила удара')
plt.ylabel('Частота (в долях)')
plt.title('Гистограммы распределений в % для двух групп')
plt.show()

# Stats
n = len(Dataset)
mean = mean_()
median = median_()
dispersion = dispersion()
std_dev = dispersion**0.5
range_ = max_arg - min_arg
quart1 = Dataset['X'].quantile(0.25)
quart3 = Dataset['X'].quantile(0.75)
iqr = quart3 - quart1
mode = Dataset['X'].mode().values[0]
assim = assim()

stats = {
    "Объём выборки": n,
    "Среднее": mean,
    "Медиана": median,
    "Дисперсия": dispersion,
    "Стандартное отклонение": std_dev,
    "Минимум": min_arg,
    "Максимум": max_arg,
    "Размах": range_,
    "Квартиль 1/4": quart1,
    "Квартиль 3/4": quart3,
    "Интерквартильная широта": iqr,
    "Мода": mode,
    "Асимметрия": assim
}

for first, second in stats.items(): #stat view
    print(f"{first}: {second:.2f}")
