def insertion_sort(data, comparator):
    if not data:
        return data
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if comparator(data[i], data[j]) > 0:
                data[i], data[j] = data[j], data[i]
    return data


def comparator_int(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

def comparator_float(a, b):
    if abs(a - b) < 1e-10:
        return 0
    elif a > b:
        return 1
    else:
        return -1

def comparator_str(a, b):
    if len(a) > len(b):
        return 1
    elif len(a) < len(b):
        return -1
    else:
        return 0