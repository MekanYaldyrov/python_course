prime_numbers = []


def prime_gen(limit):
    for i in range(2, limit):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)


a = int(input('Введите число, до которго будет проводиться поиск\n'))
prime_gen(a)
print(prime_numbers)