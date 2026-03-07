def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result


print(smallest_multiple(20))