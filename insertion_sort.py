def insertion_sort(arr, comparator):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if comparator(arr[j], arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

def by_abs(a, b):
    return int(a) < int(b)

def by_length(a, b):
    return len(a) < len(b)

def by_english_alphabet(a, b):
    return a.lower() < b.lower()

comparators = {
    "by_abs": by_abs,
    "by_length": by_length,
    "by_english_alphabet": by_english_alphabet
}


strings = input().split()
method = input()

sorted_strings = insertion_sort(strings.copy(), comparators[method])
print(sorted_strings)