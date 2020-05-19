#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, C, X = map(int, readlines())
count = 0

for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            total = 500 * i + 100 * j + 50 * k
            if total == X:
                count += 1

print(count)
