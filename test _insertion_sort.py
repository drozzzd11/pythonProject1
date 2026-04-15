import insertion_sort as sort
import random

data_assert_str = []
for i in range(1000):
    data_assert_str.append('a' * random.randint(1, 100))

if sort.insertion_sort(data_assert_str, sort.comparators["by_abs"]) == sorted(data_assert_str):
    print('true')

data_assert_float = [random.uniform(0, 10) for _ in range(1000)]
if sort.insertion_sort(data_assert_float, sort.comparators) == sorted(data_assert_float):
    print('true')

data_assert_int = []
for i in range(1000):
    data_assert_int.append(random.randint(1, 100))
if sort.insertion_sort(data_assert_int, sort.comparators) == sorted(data_assert_int):
    print('true')


assert sort.insertion_sort([], sort.by_abs) == [], "error"


assert sort.insertion_sort([0], sort.by_abs), "error"
assert sort.insertion_sort([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], sort.by_abs), "error"
assert sort.insertion_sort([1, 2, 3, 4, 5, 6], sort.by_abs), "error"
assert sort.insertion_sort([6, 5, 4, 3, 2, 1], sort.by_abs), "error"


assert sort.insertion_sort([1.111], sort.by_abs), "error"
assert sort.insertion_sort([1.111, 2.131, 3.152, 6.1101, 10.912], sort.by_abs), "error"
assert sort.insertion_sort([1.1, 1.11, 1.111, 1.1111], sort.by_abs), "error"
assert sort.insertion_sort([1.1111, 1.111, 1.11, 1.1], sort.by_abs), "error"


assert sort.insertion_sort(['a'], sort.by_length), "error"
assert sort.insertion_sort(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], sort.by_length), "error"
assert sort.insertion_sort(['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], sort.by_length), "error"
assert sort.insertion_sort(['aaaaa', 'aaaa', 'aaa', 'aa', 'a'], sort.by_length), "error"