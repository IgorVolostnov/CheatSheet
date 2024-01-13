if __name__ == '__main__':
    D = {k: 100 for k in G.keys()}  # расстояния узлам присваиваем заведомо большие настоящих значений
    start_k = 'Адмиралтейская'  # стартовая вершина
    D[start_k] = 0  # расстояние от неё до самой себя равно нулю
    U = {k: False for k in G.keys()}  # флаги просмотра вершин
    P = {k: None for k in G.keys()}  # словарь узлов предков

    for _ in range(len(D)):
        # выбираем ключ среди непросмотренных наименьшее по расстоянию
        min_k = min([k for k in U.keys() if not U[k]], key=lambda x: D[x])

        for v in G[min_k].keys():  # проходимся по всем смежным вершинам
            if D[v] > D[min_k] + G[min_k][v]:
                D[v] = D[min_k] + G[min_k][v]
                P[v] = min_k
        U[min_k] = True  # просмотренную вершину помечаем
    # print(P)
    # кратчайший путь
    pointer = input('Введите нужную станцию: ')  # куда должны прийти
    path = []  # список с вершинами пути
    while pointer is not None:  # перемещаемся, пока не придём в стартовую точку
        path.append(pointer)
        pointer = P[pointer]

    path.reverse()  # разворачиваем путь
    for v in path:
        print(v)
