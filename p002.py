def sum_of_even_fibonacci(limit):
    total = 0
    a, b = 1, 2

    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b

    return total


print(sum_of_even_fibonacci(4_000_000))