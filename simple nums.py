N = input()

def find_nums(N):
    divisors = []

    for s in range(2, N+1):
        is_simple = False
        for ind in divisors:
            if ind > s**(1/2):
                break
            check = s % ind
            if check == 0:
                is_simple = True
                break
        if not is_simple:
            divisors.append(s)
    for i in range(len(divisors)):
        divisors[i] = str(divisors[i])
    return divisors



try:
    number = int(N)
    print(' '.join(find_nums(number)))
except:
    print('error')
