prime_numbers = [2]


def prime_gen(limit):
    for i in range(3, limit):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)


a = int(input('Введите число, до которого будет проводиться поиск\n'))
prime_gen(a)
print(prime_numbers)
