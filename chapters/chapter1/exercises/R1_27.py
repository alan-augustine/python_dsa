def factors(n):
    k = 1
    big_factors = []
    while k * k < n:
        if n % k == 0:
            yield k
            big_factors.append(n // k)
        k += 1
    big_factors.reverse()
    if k * k == n:
        yield k
    for i in big_factors:
        yield i

for i in factors(100):
    print(i)
