"""
Особая тройка Пифагора

Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a^2 + b^2 = c^2

Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.

P. S. На вход подаётся число, найти тройку Пифагора для него
и вывести произведение abc.

P. P. S. Если число, полученно на входе, не является суммой
пифагоровой тройки — выводите Not found
"""


def triple(num):
    for a in range(1, num+ 1):
        for b in range(1, num + 1):
            c = num - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return 'Not found'


n = 1000
# n = int(input())
print(triple(n))
