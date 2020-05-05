"""
Наименьшее кратное

2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?

[... от 1 до числа на входе включительно.]
"""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def smallest_mul(num):
    result = 1

    for i in range(1, num + 1):
        mul = i // gcd(i, result)
        result *= mul

    return result


# n = 20
n = int(input())
print(smallest_mul(n))
