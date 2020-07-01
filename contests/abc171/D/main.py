#!/usr/bin/env python3
import sys
from collections import Counter
readline = sys.stdin.buffer.readline


def sum_d(d):
    total = 0
    for k, v in d.items():
        total += k * v
    return total


N = int(readline())
A = map(int, readline().split())
Q = int(readline())
d = Counter(A)

answer = [0] * Q

for i in range(Q):
    B, C = map(int, readline().split())

    if B in d:
        if C in d:
            d[C] = d[C] + d.pop(B)
        else:
            d[C] = d.pop(B)

    answer[i] = sum_d(d)

print(*answer, sep='\n')
