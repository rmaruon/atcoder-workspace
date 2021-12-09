#!/usr/bin/env python3
import sys
from collections import Counter

readline = sys.stdin.buffer.readline

N = int(readline())
A = list(map(int, readline().split()))
Q = int(readline())
d = Counter(A)

total = sum(A)

for _ in range(Q):
    B, C = map(int, readline().split())

    total -= B * d[B]
    total += C * d[B]

    d[C] += d[B]
    d[B] = 0

    print(total)
