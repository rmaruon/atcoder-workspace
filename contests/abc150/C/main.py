#!/usr/bin/env python3
from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

rank_P = rank_Q = 0

for i, t in enumerate(permutations(range(1, N + 1)), start=1):
    if t == P:
        rank_P = i
        if rank_Q:
            break

    if t == Q:
        rank_Q = i
        if rank_P:
            break

print(abs(rank_P - rank_Q))
