from time import perf_counter


def solve():
    n = 1
    triangle_number = 1

    while True:
        divisors = 0
        for i in range(1, int(triangle_number**0.5) + 1):
            if triangle_number % i == 0:
                divisors += 2 if i != triangle_number // i else 1

        if divisors > 500:
            return triangle_number

        n += 1
        triangle_number += n


if __name__ == "__main__":
    start = perf_counter()
    answer = solve()
    elapsed_ms = (perf_counter() - start) * 1000

    print(answer)
    print(f"Time: {elapsed_ms:.3f} ms")
