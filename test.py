import insertion_sort as sort
import random
ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'



def random_strings(n, max_len=10):
    result = []
    for _ in range(n):
        length = random.randint(1, max_len)
        s = ''
        for _ in range(length):
            s += random.choice(ALPHABET)
        result.append(s)
    return result

def random_number_strings(n, min_val=-100, max_val=100):
    result = []
    for _ in range(n):
        num = random.randint(min_val, max_val)
        result.append(str(num))
    return result

def random_length_strings(n, max_len=20):
    result = []
    for _ in range(n):
        length = random.randint(1, max_len)
        result.append('a' * length)
    return result

data_abs = random_number_strings(1000)
expected_abs = sorted(data_abs, key = int)
if sort.insertion_sort(data_abs, sort.comparators["by_abs"]) == expected_abs:
    print('true by_abs')



data_len = random_length_strings(1000)
expected_len = sorted(data_len, key = len)
if sort.insertion_sort(data_len, sort.comparators["by_length"]) == expected_len:
    print('true by_length')

data_alpha = random_strings(1000)
expected_alpha = sorted(data_alpha, key = lambda s: s.lower())
if sort.insertion_sort(data_alpha, sort.comparators["by_english_alphabet"]) == expected_alpha:
    print('true by_english_alphabet')



assert sort.insertion_sort([], sort.comparators["by_abs"]) == [], "error"


assert sort.insertion_sort(["42"], sort.comparators["by_abs"]) == ["42"], "error"
assert sort.insertion_sort(["5", "5", "5"], sort.comparators["by_abs"]) == ["5", "5", "5"], "error"
assert sort.insertion_sort(["1", "2", "3"], sort.comparators["by_abs"]) == ["1", "2", "3"], "error"


assert sort.insertion_sort([1.111], sort.by_abs), "error"
assert sort.insertion_sort([1.111, 2.131, 3.152, 6.1101, 10.912], sort.by_abs), "error"
assert sort.insertion_sort([1.1, 1.11, 1.111, 1.1111], sort.by_abs), "error"
assert sort.insertion_sort([1.1111, 1.111, 1.11, 1.1], sort.by_abs), "error"



assert sort.insertion_sort([], sort.comparators["by_length"]) == []
assert sort.insertion_sort(["abc"], sort.comparators["by_length"]) == ["abc"]
assert sort.insertion_sort(["a", "aa", "aaa"], sort.comparators["by_length"]) == ["a", "aa", "aaa"]
assert sort.insertion_sort(["aaa", "aa", "a"], sort.comparators["by_length"]) == ["a", "aa", "aaa"]

assert sort.insertion_sort([], sort.comparators["by_english_alphabet"]) == []
assert sort.insertion_sort(["AbC"], sort.comparators["by_english_alphabet"]) == ["AbC"]

