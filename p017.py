from time import perf_counter


ONES = [
    "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen",
]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def letter_count(n):
    if n == 1000:
        return len("onethousand")

    count = 0
    if n >= 100:
        count += len(ONES[n // 100]) + len("hundred")
        n %= 100
        if n:
            count += len("and")

    if n >= 20:
        count += len(TENS[n // 10]) + len(ONES[n % 10])
    else:
        count += len(ONES[n])

    return count


def solve():
    return sum(letter_count(n) for n in range(1, 1001))



if __name__ == "__main__":
    start = perf_counter()
    answer = solve()
    elapsed_ms = (perf_counter() - start) * 1000

    print(answer)
    print(f"Time: {elapsed_ms:.3f} ms")
