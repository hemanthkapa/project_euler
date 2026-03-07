def largest_palindrom_prod(n):
    largest = 0
    for i in range(100, n):
        for j in range(100, n):
            product = i * j
            if str(product) == str(product)[::-1]:
                largest = max(largest, product)
    return largest

print(largest_palindrom_prod(999))