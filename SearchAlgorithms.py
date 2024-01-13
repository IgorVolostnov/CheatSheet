# Линейный поиск
def find(my_array, find_element):
    for i, a in enumerate(my_array):
        if a == find_element:
            return i
    return False


# Количество вхождений элемента в массив
def count(my_array, find_element):
    quantity = 0
    for a in my_array:
        if a == find_element:
            quantity += 1
    return quantity


# Двоичный поиск
def binary_search(my_array, my_element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит, элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if my_array[middle] == my_element:  # если элемент в середине
        return middle  # возвращаем этот индекс
    elif my_element < my_array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(my_array, my_element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(my_array, my_element, middle + 1, right)
