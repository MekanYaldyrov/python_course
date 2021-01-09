def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def prime_gen():
    num = 2
    while True:
        if IsPrime(num):
            yield num
        num += 1


k = prime_gen()
while True:
    print(next(k))
