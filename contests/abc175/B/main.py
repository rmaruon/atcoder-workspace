#!/usr/bin/env python3

import itertools


def is_triangle(a, b, c):
    return abs(b - c) < a < b + c


N = int(input())
L = map(int, input().split())
triangles = itertools.combinations(L, 3)
count = 0

for triangle in triangles:
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]

    if (a != b and b != c and c != a) and is_triangle(a, b, c):
        count += 1

print(count)
