from time import perf_counter


def solve():
    N = 20
    grid = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        grid[0][i] = 1
        grid[i][0] = 1
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            grid[y][x] = grid[y - 1][x] + grid[y][x - 1]
    return grid[N][N]



if __name__ == "__main__":
    start = perf_counter()
    answer = solve()
    elapsed_ms = (perf_counter() - start) * 1000

    print(answer)
    print(f"Time: {elapsed_ms:.3f} ms")
