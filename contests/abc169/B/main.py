#!/usr/bin/env python3
import sys

readline = sys.stdin.buffer.readline

N = int(readline())
A = list(map(int, readline().split()))
A.sort(reverse=True)

if A[-1] == 0:
    print(0)
    exit()

for i, x in enumerate(A):
    if i == 0:
        result = x
        continue

    result = result * x

    if result > 10 ** 18:
        print(-1)
        exit()

else:
    print(result)
