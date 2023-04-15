# Пирамидальная сортировка (HeapSort)

import random
# Создаем произвольный список
def create_list(count):
    list = [i for i in range(count)]
    for i in range(0, count):
        list[i] = random.randint(1, count*5)
    return list

list = create_list(19)
print(list)

# Функция для преобразования в двоичную кучу поддерева с корневым узлом root_index, 
# что является индексом в списке list. size - размер кучи
def max_heapify(list, root_index, size):
    left_child = 2 * root_index + 1     # индекс левого дочернего элемента
    right_child = 2 * root_index + 2    # индекс правого дочернего элемента
    # Если левый дочерний элемент больше корневого узла, то меняем их местами
    if left_child < size and list[root_index] < list[left_child]:
        list[root_index], list[left_child] = list[left_child], list[root_index]
        # Рекурсивно преобразуем в двоичную кучу затронутое поддерево
        max_heapify(list, left_child, size)
    # Если правый дочерний элемент больше корневого узла, то меняем их местами
    if right_child < size and list[root_index] < list[right_child]:
        list[root_index], list[right_child] = list[right_child], list[root_index]
        # Рекурсивно преобразуем в двоичную кучу затронутое поддерево
        max_heapify(list, right_child, size)

# Основная функция, выполняющая пирамидальную сортировку
def heap_sort(list):
    # Построение кучи (перегруппируем список)
    for i in range(len(list)//2-1, -1, -1):
        max_heapify(list, i, len(list))

    # Один за другим извлекаем элементы из кучи
    for i in range(len(list) - 1, 0, -1):
        # Перемещаем текущий корень в конец
        list[0], list[i] = list[i], list[0]
        # Вызываем функцию max_heapify на уменьшенной куче
        max_heapify(list, root_index=0, size=i)

heap_sort(list)
print(list)