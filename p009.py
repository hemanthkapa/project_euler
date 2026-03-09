from time import perf_counter


def solve():
    target_sum = 1000

    # From:
    #   a + b + c = target_sum
    #   a^2 + b^2 = c^2
    # We can derive:
    #   b = target_sum * (target_sum - 2a) / (2 * (target_sum - a))
    for a in range(1, target_sum // 3):
        numerator = target_sum * (target_sum - 2 * a)
        denominator = 2 * (target_sum - a)

        if numerator % denominator != 0:
            continue

        b = numerator // denominator
        c = target_sum - a - b

        if a < b < c and a * a + b * b == c * c:
            return a * b * c

    return None

if __name__ == "__main__":
    start = perf_counter()
    answer = solve()
    elapsed_ms = (perf_counter() - start) * 1000

    print(answer)
    print(f"Time: {elapsed_ms:.3f} ms")
