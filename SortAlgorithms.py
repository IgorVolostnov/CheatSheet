import random
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]


# Алгоритм сортировки вставками
def sort_insert(array_for_sort):
    count = 0
    for i in range(1, len(array_for_sort)):
        leading_element = array_for_sort[i]
        index = i
        while index > 0:
            count += 1
            if array_for_sort[index - 1] <= leading_element:
                break
            array_for_sort[index] = array_for_sort[index - 1]
            index -= 1
        array_for_sort[index] = leading_element
    return array_for_sort


# Алгоритм сортировки слиянием
def merge_sort(array_for_sort):  # «разделяй»
    if len(array_for_sort) < 2:  # если кусок массива равен 2,
        return array_for_sort[:]  # выходим из рекурсии
    else:
        middle = len(array_for_sort) // 2  # ищем середину
        left = merge_sort(array_for_sort[:middle])  # рекурсивно делим левую часть
        right = merge_sort(array_for_sort[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # «властвуй»
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Алгоритм быстрой сортировки
def qsort_random(array_for_sort, left, right):
    p = random.choice(array_for_sort[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            # count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array_for_sort, left, j)
    if right > i:
        qsort_random(array_for_sort, i, right)
    return array_for_sort
