#!/usr/bin/env python3
import math
import sys

readline = sys.stdin.buffer.readline


def calc_dist(x, y):
    return math.sqrt(x ** 2 + y ** 2)


N, D = map(int, readline().split())
count = 0

for _ in range(N):
    X, Y = map(int, readline().split())

    if calc_dist(X, Y) <= D:
        count += 1

print(count)
