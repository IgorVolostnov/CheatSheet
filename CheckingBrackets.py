def par_checker(string):
    dict_brackets = {')': '(', ']': '[', '}': '{'}
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if s in dict_brackets.values():  # если открывающая скобка,
            stack.append(s)  # добавляем её в стек
        elif s in dict_brackets.keys():
            # если встретилась закрывающая скобка, то проверяем,
            # пуст ли стек и является ли верхний элемент открывающей скобкой
            if len(stack) > 0 and stack[-1] == dict_brackets[s]:
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0
