#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

A.sort()
A_max = A[-1]
table = [0] * (A_max + 1)

for x in A:
    table[x] += 1
    for y in range(x * 2, A_max + 1, x):
        table[y] += 1

result = sum([1 for x in A if table[x] == 1])
print(result)
