from time import perf_counter


def solve():
    limit = 2_000_000
    is_prime = [True] * limit
    is_prime[0] = False
    is_prime[1] = False

    for number in range(2, int(limit ** 0.5) + 1):
        if not is_prime[number]:
            continue

        multiple = number * number
        while multiple < limit:
            is_prime[multiple] = False
            multiple += number

    total = 0
    for number in range(limit):
        if is_prime[number]:
            total += number
    return total


if __name__ == "__main__":
    start = perf_counter()
    answer = solve()
    elapsed_ms = (perf_counter() - start) * 1000

    print(answer)
    print(f"Time: {elapsed_ms:.3f} ms")
