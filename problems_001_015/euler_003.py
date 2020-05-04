"""
Наибольший простой делитель

Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?

[Каков самый большой натуральный делитель числа из входного потока?]
"""


def biggest_prime_factor(num):
    while True:
        spf = smallest_prime_factor(num)
        if spf < num:
            num //= spf
        else:
            return num


def smallest_prime_factor(num):
    for i in range(2, int(num ** 0.5 + 1)):
        if not num % i:
            return i
    return n


# n = 600851475143
n = int(input())
print(biggest_prime_factor(n))
