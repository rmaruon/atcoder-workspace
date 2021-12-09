#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, A, B = map(int, read().split())
count = 0

for num in range(N + 1):
    total = sum(map(int, list(str(num))))
    if A <= total <= B:
        count += num

print(count)
