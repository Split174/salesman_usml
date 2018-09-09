import numpy as np
import random as rn


def input_data():
    n = input()
    dist = []
    for i in range(int(n)):
        dist.append(input().split())
    return dist

#  функция ищет ближайшего соседа ( с небольшим рандомом )
def find_neighbor(marking, arr):
    neighbor = -1
    mindist = 2 ** 32

    tmp = rn.random()  # с вероятность 10% выдаёт рандомного соседа
    if tmp <= 0.1:
        while True:
            neighbor = rn.randint(0, N - 1)
            if marking[neighbor] == 0:
                break
        return neighbor

    for i in range(len(arr)):  # иначе выдаём ближайшего соседа
        if arr[i] < mindist and marking[i] != 1:
            mindist = arr[i]
            neighbor = i
    return neighbor


dist = np.array(input_data(), float)  # матрица смежности
floyd = np.array(dist)  # в матрице содержится расстояние от точки i до j
inf = 2 ** 32  # для флойда
N = len(dist)


def neighbor_method(start_point):
    marking = np.zeros(len(dist), int)  # массив точек включённых в путь
    res = 0
    current_point = start_point
    while True:
        marking[current_point] = 1  # посетили точку
        if np.min(marking) != 0: break  # условие выхода, все точки посещены
        floyd[current_point][current_point] = inf  # костыль
        Neighbor = find_neighbor(marking, floyd[current_point, :])  # нашли ближайшего соседа
        res += floyd[current_point][Neighbor]  # прибавили расстояние
        current_point = Neighbor
    if current_point != start_point:  # добавляем расстояние от текущей точки до начальной
        res += floyd[current_point][start_point]
    return int(res)


def main():
    array_result = np.empty(1, int)  # массив в котором хранятся все решения
    for i in range(len(floyd)):  # показываем что нет прямого пути из i в j ( заменяем 0 на inf )
        for j in range(len(floyd)):
            if floyd[i][j] == 0 and i != j:
                floyd[i][j] = inf

    for k in range(len(floyd)):
        for i in range(len(floyd)):
            for j in range(len(floyd)):
                floyd[i][j] = min([floyd[i][j], floyd[i][k] + floyd[k][j]])  # вычисляем флойда

    for i in range(100):  # запускаем "рандомный" метод ближайшего соседа 100 раз
        array_result = np.append(array_result, neighbor_method(rn.randint(0, N - 1)))  # результаты пушим в массив
    #print(ArrayResult)
    print(np.min(array_result))  # выдаём минимальный среди найденных путей


main()