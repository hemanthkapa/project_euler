cache = {1: 1}

def chain(n):
    seq = []
    while n not in cache:
        seq.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    length = cache[n]
    for x in reversed(seq):
        length += 1
        cache[x] = length
    return cache[seq[0]] if seq else cache[n]

best_start, best_len = max(
    ((n, chain(n)) for n in range(500_001, 1000000)),
    key = lambda t: t[1]

)
print(best_start, best_len)