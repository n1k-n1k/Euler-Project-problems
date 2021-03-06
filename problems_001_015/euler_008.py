"""
Наибольшее произведение в последовательности

Наибольшее произведение четырех последовательных цифр
в нижеприведенном 1000-значном числе равно 9 × 9 × 8 × 9 = 5832.
...
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
...
Найдите наибольшее произведение тринадцати последовательных цифр в данном числе.
"""

import sys
from functools import reduce


def mul(seq: str, num: int) -> int:
    mul_max = 0

    for i in range(len(seq) - num + 1):
        mul_cur = reduce(lambda x, y: x * y, map(int, seq[i:i + num]))
        mul_max = max(mul_cur, mul_max)

    return mul_max


def get_data():
    data = sys.stdin.readlines()
    n = int(data[0].strip())
    s = ''.join([s.strip() for s in data[1:]])

    return n, s


# n, s = get_data()
n = 13
s = '53697817977846174064955149290862569321978468622482' \
    '83972241375657056057490261407972968652414535100474' \
    '82166370484403199890008895243450658541227588666881' \
    '16427171479924442928230863465674813919123162824586' \
    '17866458359124566529476545682848912883142607690042'

print(mul(s, n))
