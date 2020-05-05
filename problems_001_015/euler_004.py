"""
Наибольшее произведение-палиндром

Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

[На входе — количество знаков в множителях.]
"""


def biggest_palindrome(depth):
    start = 10 ** (depth - 1)
    stop = 10 ** depth
    max_p = 0

    for i in range(start, stop):
        for j in range(start, stop):
            p = i * j
            if str(p) == str(p)[::-1] and p > max_p:
                max_p = p

    return max_p


n = 3
# n = int(input())
print(biggest_palindrome(n))
