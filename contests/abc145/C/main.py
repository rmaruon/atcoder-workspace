#!/usr/bin/env python3
import math
import sys
from itertools import permutations

readlines = sys.stdin.buffer.readlines

N = int(input())
patterns = [tuple(map(int, input().split())) for _ in range(N)]

total = 0
n = 0

for pattern in permutations(patterns):

    for i in range(len(pattern) - 1):
        town_a = pattern[i]
        town_b = pattern[i + 1]

        distance = math.sqrt(
            (town_a[0] - town_b[0]) ** 2 + (town_a[1] - town_b[1]) ** 2
        )
        total += distance

    n += 1

print(total / n)
