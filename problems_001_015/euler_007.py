"""
10001-ое простое число

Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?
"""

import math


def simples_sieve(num):
    """ Решето Эратосфена """

    sieve = [i for i in range(num + 1)]
    sieve[1] = 0

    for i in range(2, num + 1):
        if sieve[i] != 0:
            j = i * 2
            while j <= num:
                sieve[j] = 0
                j += i

    return [i for i in sieve if i != 0]


n = 1001
# n = int(input())
simples_cnt = int(1.5 * n * math.log(n))  # n-е простое число не превосходит 1,5*n*ln(n)
simples_lst = simples_sieve(simples_cnt)
print(simples_lst[n - 1])
