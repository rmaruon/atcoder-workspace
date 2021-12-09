#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, Y = map(int, read().split())

for i in range(N + 1):
    for j in range(N + 1 - i):
        if (i * 10000 + j * 5000 + (N - i - j) * 1000) == Y:
            print(i, j, N - i - j)
            exit()

print("-1 -1 -1")
