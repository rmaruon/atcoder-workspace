#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, K = map(int, read().split())
count = 0

# [max(A, B), ..., 1]
for i in range(max(A, B), 0, -1):
    if A % i == 0 and B % i == 0:
        count += 1

    if count == K:
        print(i)
        exit()
