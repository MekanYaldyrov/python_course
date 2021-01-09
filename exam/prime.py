def prime_gen(limit):
    for i in range(2, limit):
        j = 2
        while j < i:
            if i % j == 0:
                break
            j += 1
        else:
            yield i


a = int(input('Введите число, до которго будет проводиться поиск\n'))
print(list(prime_gen(a)))
