from time import perf_counter


def solve():

    return sum(int(d) for d in str(2**1000))


if __name__ == "__main__":
    start = perf_counter()
    answer = solve()
    elapsed_ms = (perf_counter() - start) * 1000

    print(answer)
    print(f"Time: {elapsed_ms:.3f} ms")
