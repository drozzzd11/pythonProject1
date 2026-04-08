def insertion_sort_int(arr, comparator):
    # Убираем str_sort(), так как его назначение неясно
    for i in range(len(arr)):
        # Проходим от i вниз до 0 и меняем местами, если comparator говорит,
        # что текущий элемент должен быть раньше предыдущего
        for j in range(i, 0, -1):
            if comparator(arr[j], arr[j-1]):   # используем компаратор
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr